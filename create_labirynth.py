"""First attempt to create dfs algorithm which creates labirynth."""

import random
import pygame
#import time

# 4 x 4 for getting a grasp of what happens
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
    for i in range(1, DIM+1):
        number -= DIM
        if number <= 0:
            break
    row = 2*i - 1
    return row


def which_col(number):
    if number % DIM == 0:
        mod = DIM
    else:
        mod = number % DIM
    col = 2*mod - 1
    return col


def rows_to_draw(edge):
    return [which_row(edge[0]), which_row(edge[1]), int((which_row(edge[0])+which_row(edge[1]))/2)]


def cols_to_draw(edge):
    return [which_col(edge[0]), which_col(edge[1]), int((which_col(edge[0])+which_col(edge[1]))/2)]



maze_dim = 2*DIM-1
screen = pygame.display.set_mode((maze_dim*GRID_SIZE,maze_dim*GRID_SIZE))


edges_to_draw, graph = generate_maze(cells, 1)

color = (255,255,255)

# edge = (10,11)
# row1 = which_row(edge[0])
# col1 = which_col(edge[0])
# row2 = which_row(edge[1])
# col2 = which_col(edge[1])
# row3 = int((row1+row2)/2)
# col3 = int((col1+col2)/2)


# pygame.draw.rect(screen, color, pygame.Rect((col1-1)*GRID_SIZE, (row1-1)*GRID_SIZE, GRID_SIZE, GRID_SIZE)) # arguments in Rect : x,y, dim, dim
# pygame.display.update()

# pygame.draw.rect(screen, color, pygame.Rect((col2-1)*GRID_SIZE, (row2-1)*GRID_SIZE, GRID_SIZE, GRID_SIZE)) # arguments in Rect : x,y, dim, dim
# pygame.display.update()

# pygame.draw.rect(screen, color, pygame.Rect((col3-1)*GRID_SIZE, (row3-1)*GRID_SIZE, GRID_SIZE, GRID_SIZE)) # arguments in Rect : x,y, dim, dim
# pygame.display.update()
# print(edges_to_draw)


#clock = pygame.time.Clock()


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for edge in edges_to_draw:
        rows = rows_to_draw(edge)
        cols = cols_to_draw(edge)
        for i in range(3):
            pygame.draw.rect(screen, color, pygame.Rect((cols[i]-1)*GRID_SIZE, (rows[i]-1)*GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.display.update()
        # pygame.time.delay(500)
        # pygame.display.flip()

    #pygame.display.flip()
    #clock.tick(30)


pygame.quit()

