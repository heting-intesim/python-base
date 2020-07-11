import pygame,sys

def main():
    pygame.init()
    size = width,height = 800,600
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
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

        pygame.display.update()

if __name__ == "__main__":    main()