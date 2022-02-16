import pygame
import sys
from settings_level import *
from level import LEVEL
from MENU import Menu
from LOADING import load_image


pygame.init()
def terminate():#Просто выход
    pygame.quit()
    sys.exit()





size = screen_width, screen_height
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Программа')
fps = 70
clock = pygame.time.Clock()

level = LEVEL(MAP, screen)
menu_on = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
    if menu_on:
        screen.fill('black')
        menu = Menu(screen, size)
        menu.update()
        menu_on = menu.menu_on
        pygame.display.flip()
        if menu.exi:
            terminate()
    else:
        screen.fill('black')

        level.run()
        pygame.display.flip()
    clock.tick(fps)
