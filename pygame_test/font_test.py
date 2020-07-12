import pygame,sys
import pygame.freetype

def main():
    pygame.init()
    size = width,height = 800,600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("pygame最小框架")
    GOLD = 255,251,0
    f1 = pygame.freetype.Font(r'C:\Windows\Fonts\msyh.ttc', 36)
    # f1rect = f1.render_to(screen, (200,160), '前程似锦', fgcolor=GOLD, size=50)
    f1surf, f1rect = f1.render('中国',fgcolor=(125,125,0),bgcolor=GOLD,size=50)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
    
        # screen.fill(pygame.Color('grey'))
        f1rect.left, f1rect.top = 100, 100
        screen.blit(f1surf,f1rect)
        pygame.display.update()

if __name__ == "__main__":
    main()