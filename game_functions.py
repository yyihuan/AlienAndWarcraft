import pygame
import sys
from bullet import Bullet


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


def check_events(ai_settings, screen, ship, bullets):
    """响应鼠标和屏幕事件"""
    for event in pygame.event.get():  # 监控鼠标和键盘事件
        if event.type == pygame.QUIT:  # 监控到退出事件退出，疑问，使用exit方法是否合适？
            sys.exit()
        # 监控键盘事件，并设置标志位，用于控制飞船元素
        if event.type == pygame.KEYDOWN:
            keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyup_events(event, ai_settings, screen, ship, bullets)


def update_screen(ai_settings, screen, ship, bullets, alien):
    """动态更新屏幕图像

    Args:
        ai_settings:配置对象
        screen:surface对象
        ship:飞船元素
        bullets: sprite.Group对象，子弹元素组
    """
    screen.fill(ai_settings.bg_color)  # 绘制背景
    ship.blitme()  # 绘制飞船
    alien.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()  # 让最近一帧绘制的屏幕可见，即覆盖隐藏之前绘制的屏幕


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


def create_fleet(ai_settings, screen, aliens):
    