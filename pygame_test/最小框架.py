import pygame,sys

def main():
    pygame.init()
    size = width,height = 800,600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("pygame最小框架")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
    
        screen.fill(pygame.Color('grey'))
        pygame.display.update()

if __name__ == "__main__":
    main()