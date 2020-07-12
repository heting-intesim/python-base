import pygame,sys

def main():
    pygame.init()
    # vInfo = pygame.display.Info()
    # size = width,height = vInfo.current_w,vInfo.current_h
    size = width,height = 800,600
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    # screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.display.set_caption("壁球——pygame")
    speed = [1,1]
    BLACK = 0,0,0
    ball = pygame.image.load('ball.png')
    ballrect = ball.get_rect()
    # ballrectx = ballrect.centerx
    # ballrecty = ballrect.centery
    fps = 300
    fclock = pygame.time.Clock()
    bgcolor = pygame.Color('grey')
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.VIDEORESIZE:
                size = width,height = event.size[0],event.size[1]
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.key == pygame.K_UP:
                    speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
                elif event.key == pygame.K_DOWN:
                    speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1)*int(speed[1]/abs(speed[1]))
                elif event.key == pygame.K_RIGHT:
                    speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
                elif event.key == pygame.K_LEFT:
                    speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1)*int(speed[0]/abs(speed[0]))


        if pygame.display.get_active():
            ballrect = ballrect.move(speed[0], speed[1])
        # ballrectx += speed[0]
        # ballrecty += speed[1]
        # ballrect.centerx = ballrectx
        # ballrect.centery = ballrecty

        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        
        bgcolor.r = int(ballrect.left*255/width)
        bgcolor.g = int(ballrect.top*255/height)
        bgcolor.b = int(min(abs(speed[0]),abs(speed[1]))/max(abs(speed[0]),abs(speed[1])))
        screen.fill(bgcolor)
        screen.blit(ball, ballrect)
        pygame.display.update()
        fclock.tick(fps)

if __name__ == "__main__":
    main()