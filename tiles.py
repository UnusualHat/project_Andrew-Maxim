from LOADING import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.transform.scale(load_image('metal.png'), (size, size))
        self.rect = self.image.get_rect(topleft = pos)
