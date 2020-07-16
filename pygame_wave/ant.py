import pygame, math, random
class Ant():
    ''''定义蚂蚁类'''
    def __init__(self, screen, settings, pos, speed):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('ant.png')
        self.pos = pos
        self.speed = 3
        self.vector = 1.75 * math.pi
        self.rect = self.image.get_rect()
        self.rect.centerx,self.rect.centery = pos[0],pos[1]
        self.x = self.rect.centerx
        self.y = self.rect.centery
    
    def move(self):
        if self.rect.left < 0 or self.rect.right > self.settings.screen_width:
            self.vector = math.pi - self.vector
        if self.rect.top < 0 or self.rect.bottom > self.settings.screen_height:
            self.vector = - self.vector

        if random.random() < 0.3:
            self.vector += 0.3 * (-1 if random.random() < 0.5 else 1)
        # 实现旋转必须建立新image才可以，否则变化会累积
        self.new_image = pygame.transform.rotate(self.image, -(self.vector*180)/math.pi)

        self.x += self.speed*math.cos(self.vector)
        self.y += self.speed*math.sin(self.vector)
        self.rect.centerx = self.x
        self.rect.centery = self.y
        
    def blitme(self):
        self.screen.blit(self.new_image, self.rect)
