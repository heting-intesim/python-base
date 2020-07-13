import pygame

class Dish():
    '''一个对汉诺塔上的盘子进行管理的类'''
    def __init__(self, screen, setting, gan, width):
        '''创建一个盘子对象'''
        self.screen = screen
        self.gan = gan
        self.width = width

        self.ismove = False
        self.isturn = False

        # 设置盘子颜色
        self.color = setting.dish_color

        # 在（0，0）处创建一个表示盘子的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,self.width,setting.dish_height)
        self.rect.bottom = setting.screen_height-len(self.gan.dishes)*setting.dish_height
        self.rect.centerx = self.gan.pos_c

        # 存储小数表示盘子的位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # def update(self):
    #     '''向上移动盘子'''
    #     # # 更新表示盘子y位置的小数值
    #     # if self.y >=100:
    #     #     self.y -= 1.5
    #     # # # 更新表示盘子的rect的位置
    #     # self.rect.y = self.y
    #     pass

    def move(self,n_topole):
        '''移动盘子到其他柱子'''
        # # 更新表示盘子y位置的小数值
        if self.ismove:
            if not self.isturn:
                if self.y >=100:
                    self.y -= 1.5
                elif self.x <= n_topole*250:
                    self.x += 1.5
                else:
                    self.isturn = True
            else:
                if self.y <= 580:
                    self.y += 1.5
            
        # # # 更新表示盘子的rect的位置
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        '''在屏幕上绘制盘子'''
        pygame.draw.rect(self.screen, self.color, self.rect)