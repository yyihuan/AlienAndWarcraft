import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.moving_right = False
        self.moving_left = False
        self.ai_settings = ai_settings

        # 加载飞船图像并获取外接矩形
        # 通过操作矩形去操作实际元素，是一种更高效的做法。大部分情况下，用户不会发现他们操作的不是实际形状
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 设置新飞船位置，屏幕底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom-50
        self.center = float(self.rect.centerx)  # 设置中间变量center，以储存浮点型控制量centerx

    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """更新飞船位置"""
        # 如果标志位为真，即键盘处于按下状态，则改变位置。同时校验是否超出窗口范围
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed
        self.rect.centerx = self.center