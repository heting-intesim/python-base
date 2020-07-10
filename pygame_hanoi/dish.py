import pygame
from pygame.sprite import Sprite

class Dish(Sprite):
    '''一个对汉诺塔上的盘子进行管理的类'''
    def __init__(self, screen, setting, pos_x, pos_y,width):
        '''创建一个盘子对象'''
        super().__init__()
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width

        # 设置盘子颜色
        self.color = setting.dish_color

        # 在（0，0）处创建一个表示盘子的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,self.width,setting.dish_height)
        
        # self.screen_rect = screen.get_rect()
        # self.rect.bottom = self.screen_rect.bottom
        self.rect.bottom = self.pos_y
        self.rect.centerx = self.pos_x

        # 存储小数表示盘子的位置
        self.y = float(self.rect.y)

    def update(self):
        '''向上移动盘子'''
        # # 更新表示盘子y位置的小数值
        # if self.y >=100:
        #     self.y -= 1.5
        # # # 更新表示盘子的rect的位置
        # self.rect.y = self.y
        pass

    def move(self):
        '''向上移动盘子'''
        # # 更新表示盘子y位置的小数值
        if self.y >=100:
            self.y -= 1.5
        # # # 更新表示盘子的rect的位置
        self.rect.y = self.y

    def draw_dish(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)