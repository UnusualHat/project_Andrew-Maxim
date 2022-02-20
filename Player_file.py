from LOADING import *



class Player(pygame.sprite.Sprite):
    walk_images = {'left': (load_image('walk_left1.png'), load_image('walk_left2.png'), load_image('walk_left3.png')),
                   'right': (
                   load_image('walk_right1.png'), load_image('walk_right2.png'), load_image('walk_right3.png'))}

    run_images = {'left': (load_image('run_left1.png'), load_image('run_left2.png'), load_image('run_left3.png')),
                  'right': (load_image('run_right1.png'), load_image('run_right2.png'), load_image('run_right3.png'))}

    jump_images = {'left': (load_image('jump_left1.png')),
                   'right': (load_image('jump_right1.png'))}

    standing_images = {'left': load_image('stand_left.png'),
                       'right': load_image('stand_right.png')}


    def __init__(self, pos, size):
        super().__init__()
        self.size = size
        self.image = pygame.transform.scale(Player.standing_images['right'], (size - 5, size - 5))
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2(0, 0)


        self.LEFT_KEY, self.RIGHT_KEY = False, False
        self.is_jumping, self.on_ground = False, False
        self.gravity, self.friction = 0.35, -0.1
        self.speed_x = 30
        self.jump_height = - 10





    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y



    def update(self):
        pass


