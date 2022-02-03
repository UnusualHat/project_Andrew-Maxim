from LOADING import *



class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.transform.scale(load_image('run_left1.png'), (size - 5, size - 5))
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed_x = 7
        self.gravity = 0.7
        self.jump_height = - 15





    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y



    def update(self):
        pass


