# 游戏的常规设置 在此文件中定义
class Settings():
    '''存储《大战外星人》的所有设置的类'''
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (200, 200, 200)
        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 2
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 5 # 限制屏幕上最多能出现几个子弹

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示右移，-1表示左移
        self.fleet_direction = 1