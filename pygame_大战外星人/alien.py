import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # 表示单个外星人的类
    def __init__(self, ai_settings, screen):
        # 初始化外星人 设置初始位置
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像并获取外部矩形
        self.image = pygame.image.load('images/a2.jpg')
        self.rect = self.image.get_rect()
        # self.screen_rect = screen.get_rect()

        # 将每个外星人放在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

        # # 移动标志
        # self.moving_right = False
        # self.moving_left = False
    def check_edges(self):
        '''如果外星人位于屏幕边缘，就返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''向右或左移动外星人'''
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        # 在指定位置绘制外星人
        self.screen.blit(self.image, self.rect)