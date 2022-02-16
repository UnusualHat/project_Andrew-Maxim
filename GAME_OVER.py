from LOADING import *
from settings_level import screen_width, screen_height, TILE_SIZE


pygame.font.init()
font = pygame.font.Font(os.path.join('data', 'pixel.ttf'), 100)
class GAMEOVER(pygame.sprite.Sprite):
    def __init__(self, surface, money):
        super().__init__()
        self.display_surface = surface
        self.bottom_game_over()
        self.bottom_score()
        self.money = money


    def bottom_game_over(self):
        self.image_game_over = pygame.transform.scale(load_image('game_over.png'), ((TILE_SIZE * 6), (TILE_SIZE * 6)))
        self.rect_game_over = self.image_game_over.get_rect(topleft=(screen_width / 2 - TILE_SIZE * 3,
                                                           screen_height / 3 - TILE_SIZE * 4))


    def bottom_score(self):
        self.image_score = pygame.transform.scale(load_image('score.png'), ((TILE_SIZE * 3), (TILE_SIZE * 2)))
        self.rect_score = self.image_score.get_rect(topleft=(screen_width / 2 - TILE_SIZE * 1.5,
                                                             screen_height / 3 * 2 - TILE_SIZE * 3))




    def update(self):
        self.display_surface.blit(self.image_game_over, self.rect_game_over)
        self.display_surface.blit(self.image_score, self.rect_score)
        self.display_surface.blit(font.render(str(self.money), True, pygame.Color('white')), (screen_width / 2 + TILE_SIZE * 2, screen_height / 2 - TILE_SIZE))
