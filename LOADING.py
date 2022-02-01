import os
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
    img = pygame.image.load(fullname)
    if colorkey is not None:
        img = img.convert()
    if colorkey == -1:
        colorkey = img.get_at((0, 0))
        img.set_colorkey(colorkey)
    return img