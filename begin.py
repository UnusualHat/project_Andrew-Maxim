import pygame
import os
import sys


def main():
    #константы, всё , что может потом пригодиться
    N, M = 700, 700
    WIDTH = N
    HEIGHT = M
    FPS = 60

    # Задаем цвета
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    pygame.init()

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


    IMAGE_PLAYER =  load_image("daxbotsheet.png")
    '''
    
    
    '''


    class Board:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            # SELF.BOARD  - это список координат, связанных с доской (в список можно добавлять удобные параметры)
            self.board = [[0] * width for _ in range(height)]
            self.left = 1
            self.top = 1
            self.cell_size = 20
        # SET_VIEW даёт возможность изменять вид доски
        def set_view(self, left, top, cell_size):
            self.left = left
            self.top = top
            self.cell_size = cell_size
        # добавление в список SELF.BOARD параметров (координат);    прорисовка
        def render(self, screen):
            for y in range(self.height):
                for x in range(self.width):
                    self.board[y][x] = [[x * self.cell_size + self.left, y * self.cell_size + self.top],
                                        [x * self.cell_size + self.left + self.cell_size,
                                         y * self.cell_size + self.top + self.cell_size], 1
                                        ]
                    pygame.draw.rect(screen, pygame.Color(WHITE), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 1)



    '''



        '''
    #класс основного игрока
    class Player:
        def __init__(self, x, y):
            self.image = IMAGE_PLAYER
            self.rect = self.image.get_rect()
            self.rect_x = x
            self.rect_y = y



    '''



    '''
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    #
    #
    screen = pygame.display.set_mode(size)
    board = Board(10, 10)
    board.set_view(25, 25, 60)
    #
    #

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()


    pygame.quit()


if __name__ == '__main__':
    main()