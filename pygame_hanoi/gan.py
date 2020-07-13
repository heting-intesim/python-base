import pygame
class Gan():
    def __init__(self,setting,pos_c,width,height,screen):
        self.setting = setting
        self.dishes = []
        self.pos_c = pos_c
        self.width = width
        self.height = height
        self.screen = screen
    
    def flush(self):
        if len(self.dishes) == 1:
            self.dishes[-1].rect.bottom = self.setting.screen_height
        else:
            self.dishes[-1].rect.bottom = self.setting.screen_height-(len(self.dishes)-1)*self.setting.dish_height
        self.dishes[-1].rect.centerx = self.pos_c

    def draw_gan(self):
        pygame.draw.rect(self.screen, (0,0,0), (int(self.pos_c-self.width/2), self.setting.screen_height-self.height, self.width, self.height))
