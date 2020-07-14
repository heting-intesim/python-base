import pygame
class Wave():
    def __init__(self, screen, settings, pos):
        self.screen = screen
        self.settings = settings
        self.pos = pos
        self.radiuses = [0,-20,-40]
    
    def spread(self):
        self.radiuses[0] += 3
        self.radiuses[1] += 3
        self.radiuses[2] += 3

    def blitme(self):
        for r in self.radiuses:
            pygame.draw.circle(self.screen,self.settings.wave_color,self.pos,r,1)