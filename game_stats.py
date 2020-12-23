class GameStats():
    """跟踪游戏信息"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息
        不放在__init__中，是因为游戏期间该类只实例化一个实例
        """
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1