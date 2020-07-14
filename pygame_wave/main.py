import pygame,sys
from settings import Settings
import pygame.freetype
from wave import Wave

def main():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # icon = pygame.image.load('image/icon.png')
    # pygame.display.set_icon(icon)
    pygame.display.set_caption("水波")

    font1 = pygame.freetype.Font(r'C:\Windows\Fonts\msyh.ttc', 36)

    fps = 10
    fclock = pygame.time.Clock()

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0) # 此处必须带有参数0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                w = Wave(screen, settings, pos)
                    
        screen.fill(settings.bg_color)
        try:
            w.spread()
            w.blitme()
        except Exception as e:
            pass
        pygame.display.update()
        fclock.tick(fps)


if __name__ == "__main__":
    main()