import pygame
import random
import time
import sys



#frame for Screen
tile = 30
frame_size_x, frame_size_y = 1680, 900
W, H = frame_size_x // tile, frame_size_y // tile

#trenger en True verdi for å la spillet fortsette
running = True
FPS = 10

#Starter pygame
pygame.init()
gameWindow = pygame.display.set_mode([frame_size_x, frame_size_y])
clock = pygame.time.Clock()

#Farger
white = pygame.Color(200, 200, 200)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(50, 50, 50)

def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1
    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else: 
        if count == 3:
            return 1
        return 0


while running:

    gameWindow.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #linjene for hver felt
    [pygame.draw.line(gameWindow, white, (x,0), (x, 300), for x in range(0, 300, tile))]
    [pygame.draw.line(gameWindow, white, (0,y), (300 y), for y in range(0, 300, tile))]



    pygame.display.flip()
    clock.tick(FPS)