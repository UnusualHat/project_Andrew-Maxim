import sys

import pygame
from tiles import Tile
from settings_level import TILE_SIZE, screen_width, screen_height, MAP, level_loading
from Player_file import Player
from mobs import *
from teleport import *
from GAME_OVER import GAMEOVER


lastpos = 0
MONEY = 0


class LEVEL:
    def __init__(self, level_map, surface):
        self.display_surface = surface
        self.level_map(level_map)
        player = self.player.sprite
        self.movement = [player.direction.x, player.direction.y]
        self.gravity_ = 0.7
        self.move = player.direction.y

    def level_map(self, map):  #функция для введения текстур и мобов в уровень
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.teleport = pygame.sprite.GroupSingle()
        self.teleport.add(Teleport())
        self.basic_mobs = pygame.sprite.Group()

        for row_index, row in enumerate(map):
            for column_index, column in enumerate(row):
                if column == "t":
                    x = column_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    tile = Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile)
                if column == 'p':
                    x = column_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    self.player_sprite = Player((x, y), TILE_SIZE)
                    self.player.add(self.player_sprite)
                if column == 'w':
                    x = column_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    water = Water((x, y), TILE_SIZE)
                    self.basic_mobs.add(water)
                if column == 'l':
                    x = column_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    tornado = Tornado((x, y), TILE_SIZE)
                    self.basic_mobs.add(tornado)


    def cheking_horizontal_collisions(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed_x

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.x > 0:
                    player.rect.right = tile.rect.left
                elif player.direction.x < 0:
                    player.rect.left = tile.rect.right
            else:
                if player.direction.x > 0:
                    self.camera()
                elif player.direction.x < 0:
                    self.camera()


    def cheking_vertical_collisions(self):
        player = self.player.sprite
        player.apply_gravity()

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = tile.rect.bottom
                    player.direction.y = 0

                elif player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                    player.direction.y = 0

                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                        player.direction.y = -10 #jump_height

    def cheking_horizontal_collisions_tornado(self):
        for tile in self.tiles.sprites():
            for tornado in self.basic_mobs.sprites():
                if isinstance(tornado, Tornado):
                    if tile.rect.colliderect(tornado.rect):
                        tornado.direction *= -1

    def terminate(self):  # Просто выход
        self.display_surface.fill('black')
        game_over = GAMEOVER(self.display_surface, MONEY)
        game_over.update()
        pygame.display.flip()
        pygame.time.delay(2800)
        pygame.quit()
        sys.exit()

    def checking_mobs_collisions(self):
        for mobse in self.basic_mobs.sprites():
            if isinstance(mobse, Tornado):
                if pygame.sprite.collide_rect_ratio(0.3)(mobse, self.player.sprite):
                    self.terminate()
            else:
                if pygame.sprite.collide_rect_ratio(0.56)(mobse, self.player.sprite):
                    self.terminate()

    def checking_level_teleport(self):
        global MONEY
        teleport = self.teleport.sprite
        player = self.player.sprite
        if pygame.sprite.collide_rect_ratio(0.5)(teleport, player):
            self.level_map(level_loading())
            MONEY += 100



    def camera(self):#camera
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < TILE_SIZE * 4 and player_x > TILE_SIZE * 2 + 1 and direction_x < 0:
            self.movement[0] = 5
            player.speed_x = 0
            Tornado.direction = 0
        elif player_x > (screen_width - TILE_SIZE * 4) and direction_x > 0:
            self.movement[0] = -5
            player.speed_x = 0
            Tornado.direction = 0
        else:
            self.movement[0] = 0
            player.speed_x = 5
            Tornado.direction = random.choice((-3, 3))

        if player.rect.centery < TILE_SIZE * 1.5 and player.direction.y < 0:
            self.movement[1] = -player.direction.y
            player.rect.y -= player.direction.y
        elif  player.rect.centery > screen_height - TILE_SIZE * 1.5 and player.direction.y > 0:
            self.movement[1] = -player.direction.y
            player.rect.y -= player.direction.y
        else:
            self.movement[1] = 0


    def KEYS(self):#player
        keys = pygame.key.get_pressed()
        player = self.player.sprite

        if keys[pygame.K_RIGHT]:
            player.direction.x = 0.8
            if player.direction.y < 0:
                player.image = pygame.transform.scale(Player.jump_images['right'], (TILE_SIZE - 5, TILE_SIZE - 5))
            else:
                player.image = pygame.transform.scale(Player.standing_images['right'], (TILE_SIZE - 5, TILE_SIZE - 5))
        elif keys[pygame.K_LEFT]:
            player.direction.x = -0.8
            if player.direction.y < 0:
                player.image = pygame.transform.scale(Player.jump_images['left'], (TILE_SIZE - 5, TILE_SIZE - 5))
            else:
                player.image = pygame.transform.scale(Player.standing_images['left'], (TILE_SIZE - 5, TILE_SIZE - 5))
        else:
            player.direction.x = 0


    def run(self):
        self.tiles.draw(self.display_surface)
        self.basic_mobs.draw(self.display_surface)

        self.KEYS()
        self.player.update()
        self.player.draw(self.display_surface)
        self.cheking_horizontal_collisions()
        self.cheking_vertical_collisions()
        self.checking_mobs_collisions()
        self.cheking_horizontal_collisions_tornado()

        self.teleport.draw(self.display_surface)
        self.teleport.update(self.movement)
        #camera
        self.camera()
        self.tiles.update(self.movement)
        self.basic_mobs.update(self.movement)

        #teleport
        self.checking_level_teleport()



