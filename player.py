import pygame
import os
import sys
import random


pygame.init()

# Функция загрузки изображения >>>
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    img = pygame.image.load(fullname)
    if colorkey is not None:
        img = img.convert()
    if colorkey == -1:
        colorkey = img.get_at((0, 0))
        img.set_colorkey(colorkey)
    return img


# Сам класс игрока >>>
class Player(pygame.sprite.Sprite):
    walk_images = {'left': (load_image('walk_left1.png'), load_image('walk_left2.png'), load_image('walk_left3.png')),
                  'right': (load_image('walk_right1.png'), load_image('walk_right2.png'), load_image('walk_right3.png'))}

    run_images = {'left': (load_image('run_left1.png'), load_image('run_left2.png'), load_image('run_left3.png')),
                  'right': (load_image('run_right1.png'), load_image('run_right2.png'), load_image('run_right3.png'))}
    
    jump_images = {'left': (load_image('jump_left1.png'), load_image('jump_left2.png'), load_image('jump_left3.png')),
                   'right': (load_image('jump_right1.png'), load_image('jump_right2.png'), load_image('jump_right3.png'))}
    
    standing_images = {'left': load_image('stand_left.png'),
                       'right': load_image('stand_right.png')}
    
    def __init__(self):
        super().__init__(player_group)
        self.direction = 'right'    #<<< Направление, куда смотрит игрок
        self.image = Player.standing_images[self.direction]
        self.rect = self.image.get_rect()
        self.LEFT_KEY, self.RIGHT_KEY = False, False
        self.is_jumping, self.on_ground = False, False
        self.gravity, self.friction = 0.35, -0.1
        self.position, self.velocity = pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.gravity)
        self.posure, self.loop_counter = 0, 0   #<<< Поза отвечает за виды игрока в движении, а счётчик - за их смену

    def update(self, dt):
        self.horizontal_movement(dt)
        self.vertical_movement(dt)
        self.image_flip()   #<<< Анимация персонажа

    def image_flip(self):
        if self.LEFT_KEY or self.RIGHT_KEY:
            if abs(self.velocity.x) < 8:
                self.loop_counter += 1.25   #<<< При ходьбе кадры сменяются обычно
            elif abs(self.velocity.x) >= 8:
                self.loop_counter += 2.5    #<<< При беге кадры сменяются чаще

        # Смена позы при движении >>>
        if self.loop_counter > 10:
            self.posure = (self.posure + 1) % 3
            self.loop_counter = 0

        if self.RIGHT_KEY:
            self.direction = 'right'
        elif self.LEFT_KEY:
            self.direction = 'left'

        if self.on_ground:
            # Вид, когда игрок стоит >>>
            if not (self.LEFT_KEY or self.RIGHT_KEY):
                self.image = Player.standing_images[self.direction]
            
            # Вид при движени вправо >>>
            if self.RIGHT_KEY:
                if self.velocity.x <= 10:
                    self.image = Player.walk_images[self.direction][self.posure]
                elif self.velocity.x > 10:
                    self.image = Player.run_images[self.direction][self.posure]

            # Вид при движении влево >>>
            if self.LEFT_KEY:
                if self.velocity.x >= -10:
                    self.image = Player.walk_images[self.direction][self.posure]
                elif self.velocity.x < -10:
                    self.image = Player.run_images[self.direction][self.posure]

        else:
            # Вид в прыжке >>>
            if self.velocity.y < 0:
                self.image = Player.jump_images[self.direction][0]
            elif self.velocity.y > 0:
                self.image = Player.jump_images[self.direction][1]

    def horizontal_movement(self, dt):
        self.acceleration.x = 0
        if self.on_ground:  #<<< Ускорение (а значит и изменение скорости) меняется только на земле
            if self.LEFT_KEY:
                self.acceleration.x = -0.2
                if self.velocity.x > 0:
                    self.acceleration.x = -0.6

            elif self.RIGHT_KEY:
                self.acceleration.x = 0.2
                if self.velocity.x < 0:
                    self.acceleration.x = 0.6
            else:
                self.acceleration.x += self.velocity.x * self.friction

        self.velocity.x += self.acceleration.x * dt

        # Ограничение возрасатния скорости >>>
        if self.velocity.x > 12:
            self.velocity.x = 12
        elif self.velocity.x < -12:
            self.velocity.x = -12

        # Уход от бесконечого скольжения >>>
        if abs(self.velocity.x) < 0.1:
            self.velocity.x = 0
        self.position.x += self.velocity.x * dt + (self.acceleration.x * 0.5) * (dt * dt)
        self.rect.x = self.position.x

    def vertical_movement(self, dt):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7:
            self.velocity.y = 7
        self.position.y += self.velocity.y * dt + (self.acceleration.y * 0.5) * (dt * dt)

        # Временный невидимый пол (пока я чуть разбираюсь с генерацией карты) >>>
        if self.position.y > 200:
            self.on_ground = True
            self.velocity.y = 0
            self.position.y = 200
        self.rect.bottom = self.position.y

    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.velocity.y -= 10
            self.on_ground = False


player_group = pygame.sprite.Group()

DISPLAY_W, DISPLAY_H = 1200, 270
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
done = False
clock = pygame.time.Clock()
TARGET_FPS = 60
player = Player()
player.position.x, player.position.y = 100, 100

while not done:
    dt = clock.tick(60) * 0.001 * TARGET_FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY = True
            elif event.key == pygame.K_RIGHT:
                player.RIGHT_KEY = True
            elif event.key == pygame.K_SPACE:
                player.jump()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY = False
            elif event.key == pygame.K_RIGHT:
                player.RIGHT_KEY = False
            elif event.key == pygame.K_SPACE:
                if player.is_jumping:
                    player.velocity.y *= 0.5
                    player.is_jumping = False
            
    player.update(dt)
    canvas.fill((0, 0, 0))
    player_group.draw(canvas)
    window.blit(canvas, (0,0))
    pygame.display.flip()
pygame.quit()
