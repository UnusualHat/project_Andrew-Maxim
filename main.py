import pygame
import sys
from settings_level import *
from level import LEVEL


pygame.init()
def terminate():  # Просто выход
    pygame.quit()
    sys.exit()


size = screen_width, screen_height
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Программа')
fps = 60
clock = pygame.time.Clock()

level = LEVEL(MAP, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()

    screen.fill('black')

    level.run()
    pygame.display.flip()
    clock.tick(fps)
