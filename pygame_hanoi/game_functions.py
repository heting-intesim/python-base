import sys
import pygame
from time import sleep

def hanoi(gan1,gan2,gan3,n):
    if n == 1:
        move_disk(gan1,gan3)
        gan3.flush()
        sleep(0.3)
    else:
        hanoi(gan1,gan3,gan2,n-1)
        move_disk(gan1,gan3)
        gan3.flush()
        sleep(0.3)
        hanoi(gan2,gan1,gan3,n-1)

# def check_keydown_events(event, ai_settings,screen,ship,bullets):
#     '''响应按下按键'''
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = True
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = True
#     elif event.key == pygame.K_SPACE:
#         fire_bullet(ai_settings, screen, ship, bullets)
#     elif event.key == pygame.K_ESCAPE:
#         sys.exit(0)

# def check_keyup_events(event, ship):
#     '''响应松开按键'''
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = False

def check_events(setting, gans):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0) # 此处必须带有参数0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_m: # 运动测试
            # move_disk(gans[0], gans[1])
            hanoi(gans[0], gans[1], gans[2],setting.dishes_n)
            
            
        # elif event.type == pygame.KEYDOWN:
        #     check_keydown_events(event,ai_settings,screen,ship,bullets)
        # elif event.type == pygame.KEYUP:
        #     check_keyup_events(event, ship)

def update_screen(setting, screen, gans):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环都重绘屏幕
    screen.fill(setting.bg_color)
    # 绘制杆子
    for g in gans:
        g.draw_gan()
        for dish in g.dishes:
            dish.blitme()

    pygame.display.update()

def move_disk(gan1,gan2):
    gan_moving = gan1.dishes.pop()
    gan_moving.gan = gan2
    gan2.dishes.append(gan_moving)
    # gan2.flush()
    '''执行运动动画'''
    pass