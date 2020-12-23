import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """单个外星人/飞船的类"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # rect.x, rect.y == rect.left, rect.top, 即另alien出现在窗口左上角空出一个alien图标的边距
        self.rect.x, self.rect.y = self.rect.width, self.rect.height
        self.x = float(self.rect.x)
    '''
    def blitme(self):
        """绘制外星人的块层"""
        self.screen.blit(self.image, self.rect)
    '''


    def check_edges(self):
        """边缘碰撞判断"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:  return True
        elif self.rect.left <= 0:  return True


    def update(self):
        # self.rect.x += self.ai_settings.alien_speed
        """ 一个见鬼的bug， 使用中间变量self.x会只保留每行第一个外星人，但是下方的判断上又认为两个操作等价
        # self.x += self.ai_settings.alien_speed  # 容纳小数位的速度
        # self.rect.x = self.x
        self.rect.x += self.ai_settings.alien_speed
        self.x += self.ai_settings.alien_speed
        print(type(int(self.x)) == type(self.rect.x))
        """
        self.rect.x += (self.ai_settings.alien_speed*self.ai_settings.fleet_direction)