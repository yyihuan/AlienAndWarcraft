class Settings():
    """该类用于储存游戏的所有设置"""
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200  # 原点在窗口左上角（和opencv一致）
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 设置屏幕的背景色，苹果灰（大雾.jpg）
        self.ship_speed = 2
        self.bullet_speed = 2
        self.bullet_width, self.bullet_height = 3, 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5