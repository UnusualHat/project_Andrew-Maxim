from LOADING import *


class Water(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.transform.scale(load_image('water.png'), (size, size))
        self.rect = self.image.get_rect(topleft = pos)

