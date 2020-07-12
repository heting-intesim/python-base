import pygame,sys

def main():
    pygame.init()
    size = width,height = 800,600
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    GOLD = 255,215,0
    RED = pygame.Color('red')

    r1 = pygame.draw.rect(screen, GOLD, (0,50,400,200))
    r2 = pygame.draw.rect(screen, RED, (400,400,400,200), 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.VIDEORESIZE:
                size = width,height = event.size[0],event.size[1]
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                if event.unicode == '':
                    print('key:', '#', event.key, event.mod)
                else:
                    print('key:', event.unicode, event.key,event.mod)
            elif event.type == pygame.MOUSEMOTION:
                print('MOUSEMOTION:',event.pos,event.rel,event.buttons)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('MOUSEBUTTONDOWN:',event.pos,event.button)
            elif event.type == pygame.MOUSEBUTTONUP:
                print('MOUSEBUTTONUP:',event.pos,event.button)

        
        screen.fill(pygame.Color('grey'))
        # screen.blit(r1,r1rect)
        pygame.draw.rect(screen, GOLD, (0,50,400,200))
        pygame.draw.rect(screen, RED, (400,400,400,200), 1)
        # pygame.display.update()
        pygame.display.flip()

if __name__ == "__main__":    main()