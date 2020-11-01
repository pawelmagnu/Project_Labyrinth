import pygame
import random
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (255, 0, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Maze:
    def __init__(self, width, height):
        # upewniamy się, że liczba kolumn i wierszy jest nieparzysta, a jak parzysta to +1
        self.width = width // 2 * 2 + 1
        self.height = height // 2 * 2 + 1
        # wypełnia tablece WxH np dla (2, 2): [[True, True, True], [True, True, True], [True, True, True]]
        # True to sciana, False to ścieżka
        self.cells = [
            [True for x in range(self.width)]
            for y in range(self.height)
        ]

    # tworzy sciezke w [,x y]
    def set_path(self, x, y):
        self.cells[y][x] = False

    # tworzy sciane w [x, y]
    def set_wall(self, x, y):
        self.cells[y][x] = True

    # sprawdza czy "miesicimy sie" w macierzy
    def is_wall(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[y][x]
        else:
            return False

    # tworzy rekursywnie labirynt o podanym początku (x,y)
    def create_maze(self, x, y):
        self.set_path(x, y)
        # losowe kierunki
        all_directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        random.shuffle(all_directions)
        # probuje poruszac sie w kazdym kierunku dopoki nie zostanie mi 0 opcji
        while len(all_directions) > 0:

            direction_to_try = all_directions.pop()
            # mnozymy razy 2 gdyż poruszamy sie co 2 komorki zawsze
            node_x = x + (direction_to_try[0] * 2)
            node_y = y + (direction_to_try[1] * 2)
            # sprawdazmy czy nasz aktualny node to sciana(nie zostal odwiedzony)
            if self.is_wall(node_x, node_y):
                link_cell_x = x + direction_to_try[0]
                link_cell_y = y + direction_to_try[1]
                self.set_path(link_cell_x, link_cell_y)

                self.create_maze(node_x, node_y)
        return

    # takie do wypisywania ladnej macierzy
    def __str__(self):
        string = ""
        conv = {
            True: "XX",
            False: "  "
        }
        for y in range(self.height):
            for x in range(self.width):
                string += conv[self.cells[y][x]]
            string += "\n"
        return string


def main():
    maze = Maze(20, 20)
    maze.create_maze(1, 1)

    # maze = Maze(20, 20)
    # maze.create_maze(1, 1)
    # print(maze)
    # print('\n \n \n ')
    # for row in maze.cells:
    #     print(row, '\n')

    # Initialize the pygame
    pygame.init()
    WIDTH = 600
    once = False
    HEIGHT = 600
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Generator labiryntów")
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((BLACK))
        if once == False:
            for y in range(maze.height):
                for x in range(maze.width):
                    if maze.cells[y][x] == 0:
                        pygame.draw.rect(screen, WHITE, (x * 32 - 32, y * 32 - 32, 32, 32))
                        pygame.display.update()
                        time.sleep(.003)
                        once = True

       # pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
