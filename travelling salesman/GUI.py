import pygame
import sys
import math
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

#Functions

def create_grid():
    for i in range(len(Cities)):
        temp=[]
        for j in range(len(Cities)):
            temp.append(distance_btw_points(Cities[i],Cities[j]))
        grid.append(temp)


def draw_line():
    for i in range(len(Cities)):
        if i == len(Cities)-1:
            pygame.draw.line(screen,Red,Cities[i],Cities[0],3)
        else:
            pygame.draw.line(screen,Red,Cities[i],Cities[i+1],3)


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
                draw = True

    #Backgground
    screen.fill(Black)

    #Drawing
    for i in Cities:
        pygame.draw.circle(screen,White,i,5)

    if draw:
        draw_line()

    pygame.display.flip()

pygame.quit()
