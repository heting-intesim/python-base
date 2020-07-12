import pygame,sys
import pygame.freetype

def main():
    pygame.init()
    size = width,height = 800,600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("弹力文字——pygame")
    speed = [1,1]
    BLACK = 0,0,0
    GOLD = 255,215,0
    pos = [0,0]
    f1 = pygame.freetype.Font(r'C:\Windows\Fonts\msyh.ttc',36)
    f1rect = f1.render_to(screen, pos, '中国', fgcolor=GOLD, size=50)
    
    fps = 300
    fclock = pygame.time.Clock()
    bgcolor = pygame.Color('grey')
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
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

        if pos[0] < 0 or pos[0] + f1rect.width > width:
            speed[0] = - speed[0]
        if pos[1] < 0 or pos[1] + f1rect.height > height:
            speed[1] = - speed[1]
        pos[0] = pos[0] + speed[0]
        pos[1] = pos[1] + speed[1]

        # if pygame.display.get_active(): # 屏幕最小化后 暂停运动
        #     f1rect = f1rect.move(speed[0], speed[1])

        # if f1rect.left < 0 or f1rect.right > width:
        #     speed[0] = -speed[0]
        # if f1rect.top < 0 or f1rect.bottom > height:
        #     speed[1] = -speed[1]

        screen.fill(bgcolor)
        # 重新绘制文字
        f1rect = f1.render_to(screen, pos, '中国', fgcolor=GOLD, size=50)
        pygame.display.update()
        fclock.tick(fps)

if __name__ == "__main__":
    main()