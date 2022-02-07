from LOADING import *
from settings_level import TILE_SIZE, screen_width, screen_height

class Menu(pygame.sprite.Sprite):
    def __init__(self, surface, size):
        super().__init__()
        self.display_surface = surface
        self.bottom = []
        self.bottom_play()
        self.bottom_rules()
        self.bottom_quit()
        self.menu_on = True
        self.exi = False
        self.image_rule = False

    def bottom_play(self):
        self.image_play = pygame.transform.scale(load_image('start.png'), ((TILE_SIZE * 3), (TILE_SIZE * 2)))
        self.rect_play = self.image_play.get_rect(topleft=(screen_width / 2 - TILE_SIZE * 1.5,
                                                           screen_height / 3 - TILE_SIZE * 3))
        self.bottom.append((screen_width / 2 - TILE_SIZE * 1.5, screen_height / 3 - TILE_SIZE * 3))

    def bottom_rules(self):
        self.image_rules = pygame.transform.scale(load_image('rule.png'), ((TILE_SIZE * 3), (TILE_SIZE * 2)))
        self.rect_rules = self.image_rules.get_rect(topleft=(screen_width / 2 - TILE_SIZE * 1.5,
                                                             screen_height / 3 * 2 - TILE_SIZE * 3))
        self.bottom.append((screen_width / 2 - TILE_SIZE * 1.5, screen_height / 3 * 2 - TILE_SIZE * 3))

    def bottom_quit(self):
        self.image_quit = pygame.transform.scale(load_image('quit.png'), ((TILE_SIZE * 3), (TILE_SIZE * 2)))
        self.rect_quit = self.image_quit.get_rect(topleft=(screen_width / 2 - TILE_SIZE * 1.5, screen_height - TILE_SIZE * 3))
        self.bottom.append((screen_width / 2 - TILE_SIZE * 1.5, screen_height - TILE_SIZE * 3))

    def collisions(self):
        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if pressed[0]:
            for bottom_coords in self.bottom:
                bottom_index = self.bottom.index(bottom_coords)
                x = (pos[0] >= bottom_coords[0] and pos[0] <= bottom_coords[0] + TILE_SIZE * 3)
                y = (pos[1] >= bottom_coords[1] and pos[1] <= bottom_coords[1] + TILE_SIZE * 2)
                if x is True and y is True:
                    if bottom_index == 0:
                        self.menu_on = False
                        break
                    if bottom_index == 1:
                        self.image_rule = True
                    if bottom_index == 2:
                        self.exi = True
                        break



    def update(self):
        self.display_surface.blit(self.image_play, self.rect_play)
        self.display_surface.blit(self.image_rules, self.rect_rules)
        self.display_surface.blit(self.image_quit, self.rect_quit)
        self.collisions()
        if self.image_rule:
            self.img = pygame.transform.scale(load_image('instructions.png'), ((screen_width), (screen_height)))
            self.rect_img = self.img.get_rect(
                topleft=(0, 0))
            self.display_surface.blit(self.img, self.rect_img)
            pygame.display.flip()
            pygame.time.delay(18000)
        else:
            self.display_surface.blit(self.image_play, self.rect_play)
            self.display_surface.blit(self.image_rules, self.rect_rules)
            self.display_surface.blit(self.image_quit, self.rect_quit)

