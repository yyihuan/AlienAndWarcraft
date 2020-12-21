import pygame
import game_functions as gf
from setting import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建窗口对象
    pygame.init()
    ai_settings = Settings()
    # 创建一个surface对象，surface是屏幕的一部分，用于显示游戏元素（外星人或飞船）
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()  # 在主循环外创建元素组，避免同时创建过多元素阻塞了主循环
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)
    pygame.display.set_caption("Alien Invasion")

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)  # 监控输入设备事件
        ship.update()
        gf.update_bullets(bullets)  # 更新子弹数据
        gf.update_screen(ai_settings, screen, ship, bullets, alien)  # 动态更新窗口（背景及元素）


run_game()
