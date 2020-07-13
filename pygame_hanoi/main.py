import pygame
import setting
from dish_1 import Dish
import game_functions as gf
from gan import Gan

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption("汉诺塔")

    #创建杆子对象
    gans = []
    gans.append(Gan(setting, 200,10,350,screen))
    gans.append(Gan(setting, 500,10,350,screen))
    gans.append(Gan(setting, 800,10,350,screen))

    # 创建盘子的编组
    screen_x = screen.get_rect().centerx
    screen_bottom = screen.get_rect().bottom
    # dish_widthes = [setting.dish_width_0- for i in range(setting.dishes_n)]  # 可以首先计算出各个盘子的宽 的数组
    for i in range(setting.dishes_n):
        new_dish = Dish(screen, setting, gans[0], setting.dish_width_0-20*i)
        gans[0].dishes.append(new_dish)

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(setting, gans)

        # 刷新盘子状态
        # dishes[-1].move(3)
        # dishes[-2].move(2)


        # 每次循环都重绘屏幕, 让最近的绘图屏幕可见
        gf.update_screen(setting, screen, gans)


if __name__ == "__main__":
    run_game()