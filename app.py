import pygame
import random


grid = []
choice = ('N','W')
white =(255, 255, 255)
black =(0, 0, 0)

size = int(input("Size of the maze: "))
in_pixels = int(input("Size of 1 cell: "))
dlay = int(input("Delay: "))

last = size*2 -2
dis = size*2*in_pixels-in_pixels
screen = pygame.display.set_mode(size=(dis, dis))
pygame.display.set_caption("Project Labyrinth")


# Creating a modified grid below
for i in range(1, size*2):
    grid.append([])

for x in range(1, size*2):
    for y in range(1, size*2):
        if x % 2 == 1:
            if y % 2 == 1:
                grid[x-1].append(1)
            elif y % 2 == 0:
                grid[x-1].append(0)
        elif x % 2 == 0:
            grid[x-1].append(0)

#End of grid creation

#Path carving
def Connect(a, b):
   # print(1 ,a , b)
    where = choice[random.randint(0, 1)]
    if a == 0 and b == 0:
        grid[0][b + 1] = 1
        grid[a + 1][0] = 1

    elif a == 0 and b != last:
        grid[0][b+1]=1

    elif b == 0 and a != last:
        grid[a+1][0]=1

    else:
        if where == 'N':
            grid[a-1][b]=1
        else:
            grid[a][b-1]=1
#End of path carving

#print(grid)
#print(last)

def Draw(a,b):
    if grid[a][b] == 1:
        pygame.draw.rect(screen,white,[a*in_pixels,b*in_pixels,in_pixels,in_pixels])
    elif grid[a][b]==0:
        pygame.draw.rect(screen,black,[a*in_pixels,b*in_pixels,in_pixels,in_pixels])
    pygame.display.update()
    pygame.time.delay(dlay)


for i in range(0,last+1,2):
    for j in range(0,last+1,2):
        Connect(i,j)

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    for i in range(last+1):
        for j in range(last+1):
            Draw(j,i)

pygame.quit()
