import pygame
import random

class Dish():
    '''一个对汉诺塔上的盘子进行管理的类'''
    def __init__(self, screen, setting, gan, width):
        '''创建一个盘子对象'''
        self.screen = screen
        self.gan = gan
        self.width = width
        self.colors = [(102, 255, 255),(102, 204, 255),(102, 102, 255,),(102, 0, 255),(51, 204, 255),(51, 102, 255)]

        self.ismove = False
        self.isturn = False

        # 设置盘子颜色
        self.color = random.choice(setting.dish_colors)

        # 在（0，0）处创建一个表示盘子的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,self.width,setting.dish_height)
        self.rect.bottom = setting.screen_height-len(self.gan.dishes)*setting.dish_height
        self.rect.centerx = self.gan.pos_c


    def blitme(self):
        '''在屏幕上绘制盘子'''
        # pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.ellipse(self.screen, self.color, self.rect)