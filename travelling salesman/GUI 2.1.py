import pygame
import sys
import math
from itertools import permutations
import time
pygame.init()

#Constants
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
size = width,height = 705,705
Cities = []
draw = False
#Display screen
screen = pygame.display.set_mode(size)
grid =[]
list_of_routes = []
minimum_distance = 999999999
#Functions
def distance_calc(List):
    distance =0
    for i in range(len(List)):
        if i == len(List)-1:
            distance += grid[List[i]][List[0]]
        else:
            distance += grid[List[i]][List[i+1]]
    return distance

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
def create_grid():
    for i in range(len(Cities)):
        temp=[]
        for j in range(len(Cities)):
            temp.append(distance_btw_points(Cities[i],Cities[j]))
        grid.append(temp)


def draw_line(route):
    for i in range(len(route)):
        if i == len(route)-1:
            pygame.draw.line(screen,Red,Cities[route[i]],Cities[route[0]],3)
        else:
            pygame.draw.line(screen,Red,Cities[route[i]],Cities[route[i+1]],3)


def distance_btw_points(x1y1,x2y2):
    return int(math.sqrt((x1y1[0] - x2y2[0])**2+ (x1y1[1] - x2y2[1])**2))

def display_grid():
    for i in grid:
        print(i)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
##        elif pygame.mouse.get_pressed()[0]:
##            pos = pygame.mouse.get_pos()
##            Cities.append(pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and draw == False:
            pos = event.pos
            print(pos)
            Cities.append(pos)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space pressed")
                create_grid()
                display_grid()
                combinations = fact(len(Cities))
                draw = True

    #Backgground
    screen.fill(Black)

    #Drawing
    for i in Cities:
        pygame.draw.circle(screen,White,i,5)
    
    if draw:
        print("done {}".format((len(list_of_routes)/combinations)*100))
        permlist = permutations([int(i) for i in range(len(Cities))])
        for per in list(permlist):
            if per not in list_of_routes and distance_calc(per) < minimum_distance:
                list_of_routes.append(per)
                break
        draw_line(list_of_routes[-1])

    pygame.display.flip()

pygame.quit()
