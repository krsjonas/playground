# -*- coding: utf-8 -*-

# locale: en-US

import pygame, sys, random
from pygame.locals import *
pygame.init()

AREA = pygame.display.set_mode((320, 320))
pygame.display.set_caption("Cube")

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
P1 = ((160, 160))
P2 = ((60, 60))
P3 = ((160, 60))
P4 = ((260, 60))
P5 = ((60, 260))
P6 = ((160, 260))
P7 = ((260, 260))
mainloop = True

print("Tap any key to roll the dice, tap [Esc] to exit.")

while mainloop:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            mainloop = False
        if event.type == KEYDOWN:
            AREA.fill(BLUE)
            NUMBER = random.randrange (1, 7)
            print(NUMBER)
            if NUMBER == 1:
                pygame.draw.circle(AREA, WHITE, P1, 40)
            if NUMBER == 2:
                pygame.draw.circle(AREA, WHITE, P2, 40)
                pygame.draw.circle(AREA, WHITE, P7, 40)
            if NUMBER == 3:
                pygame.draw.circle(AREA, WHITE, P1, 40)
                pygame.draw.circle(AREA, WHITE, P4, 40)
                pygame.draw.circle(AREA, WHITE, P5, 40)
            if NUMBER == 4:
                pygame.draw.circle(AREA, WHITE, P2, 40)
                pygame.draw.circle(AREA, WHITE, P4, 40)
                pygame.draw.circle(AREA, WHITE, P5, 40)
                pygame.draw.circle(AREA, WHITE, P7, 40)
            if NUMBER == 5:
                pygame.draw.circle(AREA, WHITE, P1, 40)
                pygame.draw.circle(AREA, WHITE, P2, 40)
                pygame.draw.circle(AREA, WHITE, P4, 40)
                pygame.draw.circle(AREA, WHITE, P5, 40)
                pygame.draw.circle(AREA, WHITE, P7, 40)
            if NUMBER == 6:
                pygame.draw.circle(AREA, WHITE, P2, 40)
                pygame.draw.circle(AREA, WHITE, P3, 40)
                pygame.draw.circle(AREA, WHITE, P4, 40)
                pygame.draw.circle(AREA, WHITE, P5, 40)
                pygame.draw.circle(AREA, WHITE, P6, 40)
                pygame.draw.circle(AREA, WHITE, P7, 40)
    pygame.display.update()
pygame.quit()
