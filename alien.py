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

    def blitme(self):
        """绘制外星人的块层"""
        self.screen.blit(self.image, self.rect)