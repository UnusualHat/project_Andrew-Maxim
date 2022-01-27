import sys

import pygame
from tiles import Tile
from settings_level import TILE_SIZE
from Player_file import Player
from mobs import Water


class LEVEL:
    def __init__(self, level_map, surface):
        self.display_surface = surface
        self.level_map(level_map)

    def level_map(self, map):  #функция для введения текстур и мобов в уровень
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
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

    def cheking_horizontal_collisions(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed_x

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.x > 0:
                    player.rect.right = tile.rect.left
                elif player.direction.x < 0:
                    player.rect.left = tile.rect.right

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
                        player.direction.y = -22 #jump_height

    def checking_mobs_collisions(self):
        for mobse in self.basic_mobs.sprites():
            if mobse.rect.colliderect(self.player.sprite.rect):
                pygame.quit()
                sys.exit()


    def run(self):
        self.tiles.draw(self.display_surface)
        self.basic_mobs.draw(self.display_surface)

        self.player.update()
        self.player.draw(self.display_surface)
        self.cheking_horizontal_collisions()
        self.cheking_vertical_collisions()
        self.checking_mobs_collisions()
