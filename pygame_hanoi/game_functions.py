import sys
import pygame
from time import sleep
import pygame.freetype

def hanoi(gan1,gan2,gan3,n,n_step):
    if n == 1:
        move_disk(gan1,gan3,n_step)
        sleep(0.5)
    else:
        hanoi(gan1,gan3,gan2,n-1,n_step)
        move_disk(gan1,gan3,n_step)
        sleep(0.5)
        hanoi(gan2,gan1,gan3,n-1,n_step)

def check_events(setting, gans, t1):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0) # 此处必须带有参数0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # 运动测试
            t1.start()  # 将hanoi操作加入线程
            

def update_screen(setting, screen, gans,n_step,f1):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环都重绘屏幕
    screen.fill(setting.bg_color)
    # 显示步数信息
    f1rect = f1.render_to(screen, (0,0), f'第{n_step[0]}次移动', fgcolor=(255,0,0), size=30)
    # 绘制杆子
    for g in gans:
        g.draw_gan()
        for dish in g.dishes:
            dish.blitme()

    pygame.display.update()

def move_disk(gan1,gan2,n_step):
    gan_moving = gan1.dishes.pop()
    gan_moving.gan = gan2
    gan2.dishes.append(gan_moving)
    gan2.flush()
    n_step[0] += 1
    '''执行运动动画'''
    pass