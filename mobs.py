from LOADING import *


class Water(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.transform.scale(load_image('water.png'), (size, size))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, xy_move):
        self.rect.x += xy_move[0]
        self.rect.y += xy_move[1]

