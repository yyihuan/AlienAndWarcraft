import pygame
import sys, time
from bullet import Bullet
from alien import Alien

"""-------------------------事件响应----------------------"""


def keyup_events(event, ai_settings, screen, ship, bullets):
    """松开键盘按键时的操作"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def keydown_events(event, ai_settings, screen, ship, bullets):
    """按下键盘时的操作"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, ship)
    if event.key == pygame.K_q:  # K_q字段不区分大小写怎么处理？
        sys.exit()


def check_events(ai_settings, screen, stats, ship, bullets, play_button):
    """响应鼠标和屏幕事件"""
    for event in pygame.event.get():  # 监控鼠标和键盘事件
        if event.type == pygame.QUIT:  # 监控到退出事件退出，疑问，使用exit方法是否合适？
            sys.exit()
        # 监控键盘事件，并设置标志位，用于控制飞船元素
        if event.type == pygame.KEYDOWN:
            keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyup_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, play_button, (mouse_x, mouse_y))


def update_screen(ai_settings, screen, stats, ship, bullets, aliens, buttons, score_board):
    """动态更新屏幕图像

    Args:
        ai_settings:配置对象
        screen:surface对象
        ship:飞船元素
        bullets: sprite.Group对象，子弹元素组
    """
    screen.fill(ai_settings.bg_color)  # 绘制背景
    ship.blitme()  # 绘制飞船
    aliens.draw(screen)  # 此时无需上一版本的blitme方法了，draw是Sprite对象的内置方法，会自动绘制，并且可以被Group对象调用
    # 另一种历遍整个Group内sprite对象并调用对应方法的方案, 其实内置方法就是在抽象类AbstractGroup里实现了这个过程
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    if not stats.game_active:
        buttons.draw_button()
        # print("Play Button")

    score_board.show_score()
    pygame.display.flip()  # 让最近一帧绘制的屏幕可见，即覆盖隐藏之前绘制的屏幕


"""----------------子弹相关处理------------------"""


def update_bullets(bullets):
    bullets.update()  # 历遍每一颗有效子弹的update方法
    # 检查子弹是否超出窗口，超出删除
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, bullets, screen, ship):
    if len(bullets) >= ai_settings.bullet_allowed:
        return "Out of bullets range"
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)


"""----------------碰撞相关处理------------------"""


def check_bullet_alien_collisions(ai_settings, screen, stats, ship, aliens, bullets, score_board):
    # 参数：组a，组b，碰撞时删除a，碰撞时删除b --> dict：key-组a， value-组b
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # 碰撞处理，自己的实现
    for i in collisions:
        for j in range(len(collisions[i])):
            stats.score += ai_settings.alien_point
            score_board.set_score()
    # 例程的实现，更优雅点
    # if collisions:
    #     for i in collisions.values():
    #         stats.score += ai_settings.alien_point * len(i)
    #         score_board.prep_score()

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.update_settings()
        create_fleet(ai_settings, screen, ship, aliens)


def check_alien_ship_collisions(ai_settings, stats, screen, aliens, ship, bullets):
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, aliens, ship, bullets)


def ship_hit(ai_settings, stats, screen, aliens, ship, bullets):
    stats.ship_left -= 1
    aliens.empty()
    bullets.empty()

    if stats.ship_left > 0:
        create_fleet(ai_settings, screen, ship, aliens)
        ship.reset_ship()
        time.sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        print("GAME OVER")


"""----------------外星人相关------------------"""


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width  # 可供创建外星人的屏幕宽度
    number_aliens_x = int(available_space_x / (2 * alien_width))  # 一行可容纳的外星人数量
    return number_aliens_x


def get_number_aliens_rows(ai_settings, ship_height, alien_height):
    """计算可容纳多少行外星人"""
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height  # 屏幕可空间
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并确定其位置"""
    alien = Alien(ai_settings, screen)
    alien.rect.x = alien.rect.width + 2 * alien.rect.width * alien_number  # 根据第几个外星人，确定外星人x轴位置
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    # 注意，python采用值传递，但传递/copy的值是对象的引用/地址（赋值操作），这种方式也称为Call by sharing
    # 所以操作Group对象aliens时，是直接修改了原来的aliens
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建一堆外星人目标（外星舰队）"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_row = get_number_aliens_rows(ai_settings, ship.rect.height, alien.rect.height)

    for alien_number in range(number_aliens_x):
        for row_number in range(number_row):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, stats, screen, aliens, ship, bullets):
    """舰队触屏屏幕边缘的行为
    触及边缘则整体改变移动方向,触及底部则进入碰撞结算环节
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
        if alien.rect.bottom >= screen.get_rect().bottom:
            ship_hit(ai_settings, stats, screen, aliens, ship, bullets)
            break


def change_fleet_direction(ai_settings, aliens):
    """改变舰队运动方向，并令舰队整体向下运动"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, aliens, ship, bullets):
    check_fleet_edges(ai_settings, stats, screen, aliens, ship, bullets)
    aliens.update()


"""----------------按钮相关------------------"""


def check_play_button(ai_settings, stats, play_button, pos):
    """开始新游戏"""
    if play_button.rect.collidepoint(pos[0], pos[1]) and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
