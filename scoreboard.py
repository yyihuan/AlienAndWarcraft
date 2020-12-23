import pygame.font


class Scoreboard():
    """记分牌, 其中可分割为独立区域（面板board）分别显示不同分数"""

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.set_score = self.prep_int_board("score", (self.screen.get_rect().width - 40, 20))
        self.set_score()  # 设置分数显示面板内容
        self.show_score = self.show_board("score")

    # 此处为了代码复用，将例程内一系列显示面板(board)函数用同一个生成函数生成
    def prep_int_board(self, name, pos):
        """用于定义一个可在指定位置生成board的函数"""

        def board():
            score_str = str(int(self.stats.score))
            msg_img = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
            msg_img_rect = msg_img.get_rect()
            msg_img_rect.left = pos[0]
            msg_img_rect.top = pos[1]
            self.__setattr__(name, (msg_img, msg_img_rect))

        return board

    # 与上同理，这是展示显示面板的生成函数
    def show_board(self, name):
        def board():  self.screen.blit(self.__getattribute__(name)[0], self.__getattribute__(name)[1])
        return board
