from LOADING import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.transform.scale(load_image('run_left1.png'), (size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed_x = 7
        self.gravity = 0.7
        self.jump_height = - 15

    def KEYS(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            self.JUMP()


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def JUMP(self):
        self.direction.y = self.jump_height

    def update(self):
        self.KEYS()
        self.apply_gravity()

        self.rect.x += self.direction.x * self.speed_x
