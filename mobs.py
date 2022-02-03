from LOADING import *
import random


class Water(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.transform.scale(load_image('water.png'), (size, size))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, xy_move):
        self.rect.x += xy_move[0]
        self.rect.y += xy_move[1]




class Tornado(pygame.sprite.Sprite):
    tornadoes = [load_image('tornado.png'), load_image('tornado1.png'), load_image('tornado2.png'),
                 load_image('tornado3.png'), load_image('tornado5.png')]

    def __init__(self, pos, size):

        super().__init__()
        self.size = size
        self.image = pygame.transform.scale(random.choice(self.tornadoes), (size, size))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = random.choice((-3, 3))

    def update(self, xy_move):
        self.rect.x += xy_move[0] + self.direction
        self.rect.y += xy_move[1]
        self.image = pygame.transform.scale(random.choice(self.tornadoes), (self.size, self.size))


