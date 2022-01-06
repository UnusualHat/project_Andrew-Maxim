import pygame


def main():
    N, M = int(input()), int(input())
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

    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    #
    #

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        pygame.display.flip()


    pygame.quit()


if __name__ == '__main__':
    main()