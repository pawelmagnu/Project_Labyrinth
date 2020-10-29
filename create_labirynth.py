"""First attempt to create dfs algorithm which creates labirynth."""

import random
import pygame


DIM = 15
GRID_SIZE = 20

cells = [i for i in range(1, DIM * DIM + 1)]


def left(cell):
    return cell - 1


def right(cell):
    return cell + 1


def up(cell):
    return cell - DIM


def down(cell):
    return cell + DIM


def neighbours(cell):
    neighbours = set()
    if cell % DIM != 1:
        neighbours.add(left(cell))

    if cell % DIM != 0:
        neighbours.add(right(cell))

    if cell - DIM > 0:
        neighbours.add(up(cell))

    if cell - DIM * (DIM - 1) <= 0:
        neighbours.add(down(cell))

    return neighbours


def create_edge(cell1, cell2, graph):
    graph[cell1].add(cell2)
    graph[cell2].add(cell1)


def generate_maze(cells, start):
    list_of_edges = []
    visited = {start}
    stack = [start]
    graph = {cell: set() for cell in cells}

    while stack:
        current_cell = stack.pop()
        unvisited_neighbours = neighbours(current_cell) - visited

        if unvisited_neighbours:
            stack.append(current_cell)
            chosen_cell = random.sample(unvisited_neighbours, 1)[0]

            create_edge(chosen_cell, current_cell, graph)
            list_of_edges.append((current_cell, chosen_cell))

            visited.add(chosen_cell)
            stack.append(chosen_cell)

    return list_of_edges, graph


def which_row(number):
    for i in range(1, DIM + 1):
        number -= DIM
        if number <= 0:
            break
    row = 2 * i - 1
    return row


def which_col(number):
    if number % DIM == 0:
        mod = DIM
    else:
        mod = number % DIM
    col = 2 * mod - 1
    return col


def rows_to_draw(edge):
    return [
        which_row(edge[0]),
        which_row(edge[1]),
        int((which_row(edge[0]) + which_row(edge[1])) / 2),
    ]


def cols_to_draw(edge):
    return [
        which_col(edge[0]),
        which_col(edge[1]),
        int((which_col(edge[0]) + which_col(edge[1])) / 2),
    ]


def get_x_coordinates(cols):
    x_cords = []
    for i in range(3):
        x_cords.append((cols[i] - 1) * GRID_SIZE)
    return x_cords


def get_y_coordinates(rows):
    y_cords = []
    for i in range(3):
        y_cords.append((rows[i] - 1) * GRID_SIZE)
    return y_cords


maze_dim = 2 * DIM - 1
screen = pygame.display.set_mode((maze_dim * GRID_SIZE, maze_dim * GRID_SIZE))


edges_to_draw, graph = generate_maze(cells, 1)
counter = 0

color = (255, 255, 255)


done = False
while not done:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if counter < len(edges_to_draw):
        edge = edges_to_draw[counter]
        rows = rows_to_draw(edge)
        cols = cols_to_draw(edge)
        x_cords = get_x_coordinates(cols)
        y_cords = get_y_coordinates(rows)
        for i in range(3):
            pygame.draw.rect(
                screen,
                color,
                pygame.Rect((x_cords[i], y_cords[i], GRID_SIZE, GRID_SIZE)),
            )
        counter += 1
        pygame.display.update()


pygame.quit()
