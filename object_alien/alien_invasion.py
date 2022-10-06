import sys
import pygame
def run_game():
    #初始化游戏并且创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("外星人大战")
    bg_color = (230,230,230)
    while True:
        #监控键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        #让最近绘制的屏幕可见
        pygame.display.flip()
    
run_game()