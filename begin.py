import pygame
import os
import sys
import random


def terminate():  # Просто выход
    pygame.quit()
    sys.exit()


pygame.init()  # Без инициализации в начале load_image не будет работать


# Функция, которую будем использовать для загрузки изображений к спрайтам >>>
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
    if colorkey == -1:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# Функция, которую будем использовать для загрузки изображений к спрайтам ^^^


# Часть, что служит для загрузки текстур >>>
def load_level(filename):
    filename = "data/levels/" + filename

    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, 's'), level_map))


def generate_level(level):
    x, y = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 's':
                Tile('empty', x, y)
            elif level[y][x] == 't':
                Tile('wall', x, y)
    return x, y


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        if tile_type == 'wall':
            super().__init__(walls_group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        print(self.rect.x, self.rect.y)


# Часть, что служит для загрущки текстур ^^^


# Часть, в которой определяются свойства игрока >>>
class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__(player_group, all_sprites)

        self.image = load_image('stand_right', -1)
        self.moving_right = False
        self.moving_left = False
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.vx = 0
        self.vy = 0

    def collision_test(self, tiles):  # Вспомогательная функция, котороая при вызове
        hit_list = list()  # возвращает все объекты с которыми пересечен игрок в данный момент
        for tile in tiles:
            if self.rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def update(self, movement, tiles):
        collision_types = {'top': False, 'bottom': False,  # <<< Этот Словарь будет говрить какая грань
                           'left': False, 'right': False}  # <<< хитбокса игрока касается объектов текстур

        check_x = self.rect.x + movement[0]
        hit_list = collision_test(self.rect, tgroup)
        for tile in hit_list:
            if movement[0] > 0:
                check_x.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                check_x.left = tile.right
                collision_types['left'] = True

        check_y = self.rect.y + movement[1]
        hit_list = collision_test(self.rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                check_y.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                check_y.top = tile.bottom
                collision_types['top'] = True


# Часть, в которой определяются свойства игрока ^^^


# Сама программа, где прописываются действия с созднанными объектами >>>
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
player = None

size = width, height = 1200, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Программа')
fps = 60
clock = pygame.time.Clock()

tile_images = {
    'wall': pygame.transform.scale(load_image('metal.png', -1), (50, 50)),
    'empty': pygame.Surface((50, 50))
}

tile_width = tile_height = 50
level_x, level_y = generate_level(load_level('level1.txt'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

    screen.fill((0, 0, 0))
    tiles_group.draw(screen)
    pygame.display.flip()