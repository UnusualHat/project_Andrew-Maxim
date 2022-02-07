from LOADING import *
from settings_level import screen_width, TILE_SIZE



class Teleport(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(load_image('teleport.png'), (TILE_SIZE * 2, TILE_SIZE * 10))
        self.rect = self.image.get_rect(topleft=(screen_width, 0))

    def update(self, xy_move):
        self.rect.x += xy_move[0]
        self.rect.y += xy_move[1]
