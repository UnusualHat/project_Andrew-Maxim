import pygame, os


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")

    image = pygame.image.load(fullname)
    return image


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.transform.scale(load_image('metal.png'), (size, size))
        self.rect = self.image.get_rect(topleft = pos)
