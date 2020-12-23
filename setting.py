class Settings():
    """该类用于储存游戏的所有设置"""
    def __init__(self):
        """初始化静态参数和动态参数"""
        # 屏幕设置
        self.screen_width = 1200  # 原点在窗口左上角（和opencv一致）
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 设置屏幕的背景色，苹果灰（大雾.jpg）

        self.ship_limit = 3

        self.bullet_width, self.bullet_height = 3000, 15
        self.bullet_color = 60, 60, 60

        self.speedup_scale = 1.2  # 玩家升级后，玩家和舰队移动速度升级比例

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化动态参数"""
        self.ship_speed = 2

        self.bullet_allowed = 5
        self.bullet_speed = 2

        self.alien_speed = 15
        self.fleet_drop_speed = 6
        self.alien_point = 10

        self.fleet_direction = 1  # 舰队移动方向，1右，-1左

    def update_settings(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.fleet_drop_speed *= 1+(self.speedup_scale-1)/2
        self.alien_point *= self.speedup_scale

        self.bullet_allowed += 1
