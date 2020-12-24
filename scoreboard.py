import pygame.font


class Scoreboard():
    """记分牌, 其中可分割为独立区域（面板board）分别显示不同分数"""

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.set_score = self.prep_int_board("score", (self.screen.get_rect().width / 2 - 80, 20))
        self.set_level = self.prep_int_board("level", (self.screen.get_rect().width - 80, 20))
        self.set_score()  # 设置分数显示面板内容
        self.set_level()

    # 此处为了代码复用，将例程内一系列显示面板(board)函数用同一个生成函数生成
    def prep_int_board(self, name, pos):
        """用于定义一个可在指定位置生成board的函数, 该函数会把msg转换为img"""

        def board():
            # int为不可变对象，运行过程中赋值会改变id，故不能直接传入方法，需要使用get方法获取同名字段的值
            msg = self.stats.__getattribute__(name)
            score_str = str(int(msg))
            msg_img = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
            msg_img_rect = msg_img.get_rect()
            msg_img_rect.left = pos[0]
            msg_img_rect.top = pos[1]
            self.__setattr__(name, (msg_img, msg_img_rect))

        return board

    # 修改例程为接受一个board的name的list，逐一刷新
    def show_board(self, name_list):
        for name in name_list:
            self.screen.blit(self.__getattribute__(name)[0], self.__getattribute__(name)[1])
