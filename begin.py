import pygame
import os
import sys
import random



def main():
    #константы, всё , что может потом пригодиться
    N, M = 700, 700
    WIDTH = N
    HEIGHT = M
    FPS = 60


    ACC = 0.5 #ускорение
    FRIC = -0.12 #трение


    # Задаем цвета
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)


    with open(str(os.getcwd()) + '\data\levels' + '\\' +
              random.choice(os.listdir(str(os.getcwd()) + '\data\levels')), 'r', encoding='UTF-8') as file_level:
        data_level = file_level.readlines()
        level_full = []
        for i in data_level:
            textures = []
            for j in i.replace('\n', ''):
                textures.append(j)
            level_full.append(textures)



    LEVEL_TEXTURES = level_full





    pygame.init()

    CLOCK = pygame.time.Clock()
    '''
    

    '''
    #загрузка изображений
    def load_image(name):
        fullname = os.path.join('data', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image


    '''
    
    
    '''
    TEXTURE_IMAGE = pygame.transform.scale(load_image('metal.png'), (60, 60))

    class Texture(pygame.sprite.Sprite):
        def __init__(self, group, center):
            super().__init__(group)
            self.image = TEXTURE_IMAGE
            self.rect = self.image.get_rect()
            self.rect.centerx = center[0]
            self.rect.centery = center[1]



    SPIKE_IMAGE = pygame.transform.scale(load_image(str(os.getcwd()) + '\data\spikes' + '\\' +
              random.choice(os.listdir(str(os.getcwd()) + '\data\spikes'))), (60, 60))

    class Spike(pygame.sprite.Sprite):
        def __init__(self, group, center):
            super().__init__(group)
            self.image = SPIKE_IMAGE
            self.rect = self.image.get_rect()
            self.rect.centerx = center[0]
            self.rect.centery = center[1]


    class Board:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.board = []
            # SELF.BOARD  - это список координат, связанных с доской (в список можно добавлять удобные параметры)
            for i in range(len(LEVEL_TEXTURES)):
                zapolnenie = []
                for j in LEVEL_TEXTURES[i]:
                    zapolnenie.append(j)
                self.board.append(zapolnenie)
            self.left = 1
            self.top = 1
            self.cell_size = 20
        # SET_VIEW даёт возможность изменять вид доски
        def set_view(self, left, top, cell_size):
            self.left = left
            self.top = top
            self.cell_size = cell_size
        # добавление в список SELF.BOARD параметров (координат);    прорисовка
        def render(self):
            for y in range(self.height):
                for x in range(self.width):
                    self.board[y][x] = [self.board[y][x],
                                        [x * self.cell_size + self.left, y * self.cell_size + self.top],
                                        [x * self.cell_size + self.left + self.cell_size,
                                         y * self.cell_size + self.top + self.cell_size]
                                        ]




    '''



        '''

    IMAGE_PLAYER = pygame.transform.scale(load_image("daxbotsheet.png"), (50, 50))

    #класс основного игрока
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = IMAGE_PLAYER

            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.centery = WIDTH / 2

            self.vel = 1 #скорость
            self.acc = ACC * 10
            self.fric = FRIC

        #физику надо добавить
        def GAME_OVER(self):
            print('game over')
            pygame.quit()


        def update(self):
            global running
            #game over
            for i in all_sprites:
                if isinstance(i, Spike):
                    if (self.rect.collidepoint(i.rect.topleft[0], i.rect.topleft[1])) or (
                        self.rect.collidepoint(i.rect.topright[0], i.rect.topright[1])) or (
                        self.rect.collidepoint(i.rect.bottomleft[0], i.rect.bottomleft[1])) or (
                            self.rect.collidepoint(i.rect.bottomright[0], i.rect.bottomright[1])):
                        self.GAME_OVER()








            jumps = False
            keystate = pygame.key.get_pressed()


            if keystate[pygame.K_LEFT]:
                STOP_L = 0
                for i in all_sprites:
                    if isinstance(i, Texture):
                        if i.rect.right > self.rect.left - 5 and i.rect.left < self.rect.right - 5\
                                and i.rect.top < self.rect.bottom and i.rect.bottom > self.rect.top:
                            STOP_L = i.rect.right
                if self.rect.x - 3 > STOP_L:
                    self.rect.x -= 5



            if keystate[pygame.K_RIGHT]:
                STOP_R = 0
                for i in all_sprites:
                    if isinstance(i, Texture):
                        if i.rect.left < self.rect.right + 5 and i.rect.right > self.rect.right + 5 \
                                and i.rect.top < self.rect.bottom and i.rect.bottom > self.rect.top:
                            STOP_R = i.rect.right
                if self.rect.x - 3 > STOP_R:
                    self.rect.x += 5



            if keystate[pygame.K_UP]:
                jumps = True
                self.rect.y -= 14

            STOP = HEIGHT
            for i in all_sprites:
                if isinstance(i, Texture):
                    if i.rect.right > self.rect.left and i.rect.left < self.rect.right\
                            and self.rect.bottom + 5 > i.rect.top and self.rect.bottom + 5 < i.rect.bottom:
                        STOP = i.rect.top
            if self.rect.bottom < HEIGHT and self.rect.bottom < STOP - 4:
                if not jumps:
                    self.rect.y += self.acc - 9
                    self.acc += 0.13
                else:
                    self.rect.y += self.acc
                    self.acc += 0.13
            else:
                self.acc = ACC * 10



    #класс для тестирования физики игрока
    class platform(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((WIDTH, 20))
            self.surf.fill((255, 0, 0))
            self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))

        def draw(self, screen):
            pygame.draw.rect(screen, pygame.Color(WHITE), (0, HEIGHT - 10, WIDTH, HEIGHT))

    plat = platform()

    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    board = Board(len(LEVEL_TEXTURES[0]), len(LEVEL_TEXTURES))
    board.set_view(5, 5, 60)
    board.render()

    for y in range(board.height):
        for x in range(board.width):
            if board.board[y][x][0] == 't':
                Texture(all_sprites, ((board.board[y][x][1][0] + board.board[y][x][2][0]) / 2,
                                      (board.board[y][x][1][1] + board.board[y][x][2][1]) / 2))


    for y in range(board.height):
        for x in range(board.width):
            if board.board[y][x][0] == 'h':
                Spike(all_sprites, ((board.board[y][x][1][0] + board.board[y][x][2][0]) / 2,
                                      (board.board[y][x][1][1] + board.board[y][x][2][1]) / 2))
    '''



    '''

    size = WIDTH, HEIGHT

    #
    #
    screen = pygame.display.set_mode(size)

    #
    #

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Рендеринг
        all_sprites.update()
        screen.fill(BLACK)
        all_sprites.draw(screen)
        plat.draw(screen)
        board.render()
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()
        CLOCK.tick(FPS)

    pygame.quit()




if __name__ == '__main__':
    main()