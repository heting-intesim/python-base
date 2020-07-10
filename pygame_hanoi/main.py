import pygame
import setting
from dish_1 import Dish
import game_functions as gf

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption("汉诺塔游戏")

    # 创建盘子的编组
    dishes = []
    screen_x = screen.get_rect().centerx
    screen_bottom = screen.get_rect().bottom
    # dish_widthes = [setting.dish_width_0- for i in range(setting.dishes_n)]  # 可以首先计算出各个盘子的宽 的数组
    for i in range(setting.dishes_n):
        new_dish = Dish(screen, setting, screen_x-250, screen_bottom-setting.dish_height*i, setting.dish_width_0-20*i)
        dishes.append(new_dish)

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(dishes)
        # 刷新盘子状态
        dishes[-1].move(3)
        dishes[-2].move(2)

        # 每次循环都重绘屏幕, 让最近的绘图屏幕可见
        gf.update_screen(setting, screen,dishes)


if __name__ == "__main__":
    run_game()