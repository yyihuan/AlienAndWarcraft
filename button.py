import pygame.font

class Button():
    """每个按钮都是该类的一个实例"""
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen.get_rect().center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """填充按钮文字，并渲染为图像"""
        # pygame.font.Font.render(): 在一个新Surface 对象上绘制文本, True为开启反锯齿
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个颜色填充的按钮，再绘制文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
