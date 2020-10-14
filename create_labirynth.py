"""First attempt to create dfs algorithm which creates labirynth."""

import random

# 4 x 4 for getting a grasp of what happens
DIM = 4

cells = [i for i in range(1, DIM*DIM+1)]

def left(cell):
    return cell-1

def right(cell):
    return cell+1

def up(cell):
    return cell-DIM

def down(cell):
    return cell+DIM

def neighbours(cell):
    neighbours = set()
    if cell % DIM != 1:
        neighbours.add(left(cell))

    if cell % DIM != 0:
        neighbours.add(right(cell))
    
    if cell - DIM > 0:
        neighbours.add(up(cell))

    if cell - DIM*(DIM-1) <= 0:
        neighbours.add(down(cell))

    return neighbours


def create_edge(cell1, cell2, graph):

    pass


def create(cells, start):
    #neighbours_of_cells = {cell : neighbours(cell) for cell in cells}   # probably not useful
    visited = {start}
    stack = [start]
    graph = {cell : set() for cell in cells}

    while stack:
        current_cell = stack.pop()
        unvisited_neighbours = neighbours(current_cell) - visited

        if unvisited_neighbours:
            stack.append(current_cell)
            [chosen_cell] = random.sample(unvisited_neighbours, 1) #### tutaj zrobić wybieranie losowo
            
            #print(graph[current_cell])
            #print(chosen_cell)
            #print(graph[chosen_cell])
            #print(current_cell)
            graph[current_cell].add(chosen_cell)
            graph[chosen_cell].add(current_cell)
            
            visited.add(chosen_cell)
            stack.append(chosen_cell)

    print(graph)

create(cells, 1)








    