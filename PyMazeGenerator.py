import random
import pygame
import time

white = (255,250,250)
red =  (255,0,0)

visited = []
queue = []
x = 1
y = 1

print("Podaj rozmiar labiryntu")
s = input()

screen = pygame.display.set_mode((int(s)*int('20'),int(s)*int('20')))
pygame.display.set_caption("Project Labyrinth")

grid = {(x,y):1 for x in range(1, int(s)+int('1')) for y in range(1, int(s)+int('1'))}

def CheckNeighbours():
    if (x + 2, y) not in visited and (x+2,y) in grid:
        neighb.append("E")

    if (x - 2, y) not in visited and (x-2,y) in grid:
        neighb.append("W")
            
    if (x, y + 2) not in visited and (x,y+2) in grid:
        neighb.append("N")

    if (x, y - 2) not in visited and (x,y-2) in grid:
        neighb.append("S")

def DrawLeft():
    pygame.draw.rect(screen, white, ((x+1)*20-20,y*20-20,20,20))
    pygame.display.update()
    time.sleep(.007)
    
def DrawRight():
    pygame.draw.rect(screen, white, ((x-1)*20-20,y*20-20,20,20))
    pygame.display.update()
    time.sleep(.007)

def DrawUp():
    pygame.draw.rect(screen, white, (x*20-20,(y-1)*20-20,20,20))
    pygame.display.update()
    time.sleep(.007)

def DrawDown():
    pygame.draw.rect(screen, white, (x*20-20,(y+1)*20-20,20,20))
    pygame.display.update()
    time.sleep(.007)

def DrawPosition():
    pygame.draw.rect(screen, red, (x*20-20,y*20-20,20,20))
    pygame.display.update()
    time.sleep(.03)

    pygame.draw.rect(screen, white, (x*20-20,y*20-20,20,20))
    pygame.display.update()
    time.sleep(.007)

queue.append((x,y))
visited.append((x,y))
pygame.draw.rect(screen, white, (0,0,20,20))
pygame.display.update()

exit = False
while not exit:
    while len(queue) > 0:
        neighb = []
        CheckNeighbours()

        if len(neighb) > 0:
            random_neighb = (random.choice(neighb))

            if random_neighb == "E":
                x = x + 2
                DrawRight()
                DrawPosition()
                queue.append((x,y))
                visited.append((x,y))

            elif random_neighb == "W":
                x = x - 2
                DrawLeft()
                DrawPosition()
                queue.append((x,y))
                visited.append((x,y))

            elif random_neighb == "N":
                y = y + 2
                DrawUp()
                DrawPosition()
                queue.append((x,y))
                visited.append((x,y))

            elif random_neighb == "S":
                y = y - 2
                DrawDown()
                DrawPosition()
                queue.append((x,y))
                visited.append((x,y))

        else:
            x, y = queue.pop() 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
pygame.quit()