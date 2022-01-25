import pygame
from tiles import Tile
from settings_level import TILE_SIZE
from Player_file import Player


class LEVEL:
    def __init__(self, level_map, surface):
        self.display_surface = surface
        self.level_map(level_map)

    def level_map(self, map):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

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
                    player_sprite = Player((x, y), TILE_SIZE)
                    self.player.add(player_sprite)

    def run(self):
        self.tiles.draw(self.display_surface)

        self.player.update()
        self.player.draw(self.display_surface)


