import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
# from alien import Alien

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("大战外星人")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建飞船
    ship = Ship(ai_settings, screen)
    # 创建存储子弹的编组
    bullets = Group()
    # 创建外星人
    # alien = Alien(ai_settings, screen)
    # 创建外星人群
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active:
            # 刷新飞船状态
            ship.update()
            # 刷新子弹     # 删除已经消失的子弹
            gf.update_bullets(ai_settings,screen,ship, aliens, bullets)
            # 刷新外星人
            gf.update_aliens(ai_settings, stats,screen, ship, aliens,bullets)
        # 每次循环都重绘屏幕, 让最近的绘图屏幕可见
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == "__main__":
    run_game()