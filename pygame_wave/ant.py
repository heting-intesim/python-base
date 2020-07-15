import pygame, math
class Ant():
    ''''定义蚂蚁类'''
    def __init__(self, screen, settings, pos, speed):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('ant.jpg')
        self.pos = pos
        self.speed = speed
        self.vector = 0.1*math.pi
        self.rect = self.image.get_rect()
        self.x = self.rect.centerx
        self.y = self.rect.centery
    
    def move(self):
        if self.rect.right > self.settings.screen_width or self.rect.left < 0:
            self.vector = 2*(math.pi/2-self.vector)
        if self.rect.top < 0 or self.rect.bottom > self.settings.screen_height:
            self.vetctor = 2*(math.pi/2-self.vector)
        speed_x = self.speed * math.cos(self.vector)
        speed_y = self.speed * math.sin(self.vector)
        self.x += speed_x
        self.y += speed_y
        self.rect.centerx = self.x
        self.rect.centery = self.y


    def blitme(self):
        self.screen.blit(self.image, self.rect)
