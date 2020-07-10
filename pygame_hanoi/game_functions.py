import sys
import pygame

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

def check_events(dishes):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0) # 此处必须带有参数0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_m: # 运动测试
            dishes[-1].ismove = True
            # dishes[-2].ismove = True
        # elif event.type == pygame.KEYDOWN:
        #     check_keydown_events(event,ai_settings,screen,ship,bullets)
        # elif event.type == pygame.KEYUP:
        #     check_keyup_events(event, ship)

def update_screen(setting, screen, dishes):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环都重绘屏幕
    screen.fill(setting.bg_color)

    # # 在移动盘子之后重绘所有盘子
    for dish in dishes:
        dish.blitme()
    # 让最近的绘图屏幕可见
    pygame.display.flip()

# def update_dishes(dishes):
#     '''更新盘子的位置'''
#     dishes.update()

def move_disk(dishes):
    dishes[-1].move()
    dishes[-1].blitme()
# def fire_bullet(ai_settings, screen, ship, bullets):
#     '''如果还没有到达限制数量，则发射一颗子弹'''
#     if len(bullets) < ai_settings.bullet_allowed:
#         new_bullet = Bullet(ai_settings, screen, ship)
#         bullets.add(new_bullet)