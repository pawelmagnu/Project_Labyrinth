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
pygame.display.set_caption("Project Labyrinth")

grid = {(x,y):1 for x in range(1, int(s)+int('1')) for y in range(1, int(s)+int('1'))}

def MazeLoop(x, y):
    queue.append((x,y))
    visited.append((x,y))
    
    pygame.draw.rect(screen, (255,250,250), (0,0,20,20))
    pygame.display.update()

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

                pygame.draw.rect(screen, (255,250,250), ((x-1)*20-20,y*20-20,20,20))
                pygame.display.update()
                time.sleep(.007)

                pygame.draw.rect(screen, (255,250,250), (x*20-20,y*20-20,20,20))
                pygame.display.update()
                time.sleep(.007)

                queue.append((x,y))
                visited.append((x,y))

            elif random_neighb == "W":
                x = x - 2

                pygame.draw.rect(screen, (255,250,250), ((x+1)*20-20,y*20-20,20,20))
                pygame.display.update()
                time.sleep(.007)
                
                pygame.draw.rect(screen, (255,250,250), (x*20-20,y*20-20,20,20))
                pygame.display.update()
                time.sleep(.007)

                queue.append((x,y))
                visited.append((x,y))

            elif random_neighb == "N":
                y = y + 2
                
                pygame.draw.rect(screen, (255,250,250), (x*20-20,(y-1)*20-20,20,20))
                pygame.display.update()
                time.sleep(.007)

                pygame.draw.rect(screen, (255,250,250), (x*20-20,y*20-20,20,20))
                pygame.display.update()
                time.sleep(.007)

                queue.append((x,y))
                visited.append((x,y))

            elif random_neighb == "S":
                y = y - 2
                
                pygame.draw.rect(screen, (255,250,250), (x*20-20,(y+1)*20-20,20,20))
                pygame.display.update()
                time.sleep(.007)

                pygame.draw.rect(screen, (255,250,250), (x*20-20,y*20-20,20,20))
                pygame.display.update()
                time.sleep(.007)

                queue.append((x,y))
                visited.append((x,y))

        else:
            x, y = queue.pop()

MazeLoop(x,y)

exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
pygame.quit()