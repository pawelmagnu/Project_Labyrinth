import random
import pygame
import time

visited = []
queue = []
x = 1
y = 1

print("Podaj rozmiar labiryntu")
s = input()
screen = pygame.display.set_mode((int(s)*int('20'),int(s)*int('20')))

grid = {(x,y):1 for x in range(1, int(s)+int('1')) for y in range(1, int(s)+int('1'))}

def MazeLoop(x, y):
    queue.append((x,y))
    visited.append((x,y))
    grid[(1,1)] = 0
    while len(queue) > 0:
        neighb = []

        if (x + 2, y) not in visited and (x+2,y) in grid:
            neighb.append("E")

        if (x - 2, y) not in visited and (x-2,y) in grid:
            neighb.append("W")
        
        if (x, y + 2) not in visited and (x,y+2) in grid:
            neighb.append("N")

        if (x, y - 2) not in visited and (x,y-2) in grid:
            neighb.append("S")
        if len(neighb) > 0:
            random_neighb = (random.choice(neighb))

            if random_neighb == "E":
                x = x + 2
                grid[(x,y)] = 0
                grid[(x-1,y)] = 0
                queue.append((x,y))
                visited.append((x,y))

            elif random_neighb == "W":
                x = x - 2
                grid[(x,y)] = 0
                grid[(x+1,y)] = 0
                queue.append((x,y))
                visited.append((x,y))

            elif random_neighb == "N":
                y = y + 2
                grid[(x,y)] = 0
                grid[(x,y-1)] = 0
                queue.append((x,y))
                visited.append((x,y))

            elif random_neighb == "S":
                y = y - 2
                grid[(x,y)] = 0
                grid[(x,y+1)] = 0
                queue.append((x,y))
                visited.append((x,y))

        else:
            x, y = queue.pop()

MazeLoop(x,y)

for x in range(1, int(s)+int('1')):
    for y in range(1, int(s)+int('1')):
        if grid[(x,y)] == 0:
            pygame.draw.rect(screen, (255,250,250), (x*20-20,y*20-20,20,20))
            pygame.display.update()
            time.sleep(.001)
        else:
            pygame.draw.rect(screen, (20,20,20), (x*20-20,y*20-20,20,20))
            pygame.display.update()
            time.sleep(.001)

exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
pygame.quit()