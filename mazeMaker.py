import hexabyrinth
import pygame
import math
import pyautogui

(width,height) = pyautogui.size()
width = (int)(width*(9/10))
height = (int)(height*(9/10))


size = int(input("Podaj rozmiar labiryntu:"))

gr=1
colour = 0x458693

maze = hexabyrinth.Maze.generate(size)

radius_w = width/(2*(2*size-1))
radius_h = height/((size*3-1))

radius = int(min(radius_h,radius_w))

screen = pygame.display.set_mode((int(((2*size-1)*2*radius)*(9/10)), (size*3-1)*radius))

(x_0,y_0)=(radius,height/2)
for n in range(-(size-1),size):
    for m in range(0, 2*(size-1)-abs(n)+1):
        x_k = x_0 + radius*(abs(n)+2*m)*(7/8)
        y_k = y_0 - 3*radius*n/2
        cell = maze.get_cell(n, m)

        if hexabyrinth.NE in cell.walls:
            #NE
            pygame.draw.line(screen, colour, ((int)(x_k+radius*math.cos(math.pi/6)),(int)(y_k-radius*math.sin(math.pi/6))), ((int)(x_k),(int)(y_k-radius)), gr)

        if hexabyrinth.NW in cell.walls:
            #NW
            pygame.draw.line(screen, colour,((int)(x_k),(int)(y_k-radius)), ((int)(x_k+radius*math.cos(150*2*math.pi/360)),(int)(y_k-radius*math.sin(150*2*math.pi/360))), gr)

        if hexabyrinth.W in cell.walls:
            #W
            pygame.draw.line(screen, colour, ((int)(x_k+radius*math.cos(150*2*math.pi/360)),(int)(y_k-radius*math.sin(150*2*math.pi/360))), ((int)(x_k+radius*math.cos(210*2*math.pi/360)),(int)(y_k-radius*math.sin(210*2*math.pi/360))), gr)

        if hexabyrinth.SW in cell.walls:
            #SW
            pygame.draw.line(screen, colour, ((int)(x_k+radius*math.cos(210*2*math.pi/360)),(int)(y_k-radius*math.sin(210*2*math.pi/360))), ((int)(x_k+radius*math.cos(270*2*math.pi/360)),(int)(y_k-radius*math.sin(270*2*math.pi/360))), gr)

        if hexabyrinth.SE in cell.walls:
            #SE
            pygame.draw.line(screen, colour, ((int)(x_k+radius*math.cos(270*2*math.pi/360)),(int)(y_k-radius*math.sin(270*2*math.pi/360))), ((int)(x_k+radius*math.cos(330*2*math.pi/360)),(int)(y_k-radius*math.sin(330*2*math.pi/360))), gr)

        if hexabyrinth.E in cell.walls:
            #E
            pygame.draw.line(screen, colour, ((int)(x_k+radius*math.cos(330*2*math.pi/360)),(int)(y_k-radius*math.sin(330*2*math.pi/360))), ((int)(x_k+radius*math.cos(30*2*math.pi/360)),(int)(y_k-radius*math.sin(30*2*math.pi/360))), gr)

        pygame.display.update()

exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
pygame.quit()
