# -*- coding: utf-8 -*-

# locale: de-DE

import pygame, sys, random
from pygame.locals import *
pygame.init()

FELD = pygame.display.set_mode((320, 320))
pygame.display.set_caption("Würfel")

BLAU = (0, 0, 255)
WEISS = (255, 255, 255)
P1 = ((160, 160))
P2 = ((60, 60))
P3 = ((160, 60))
P4 = ((260, 60))
P5 = ((60, 260))
P6 = ((160, 260))
P7 = ((260, 260))
mainloop = True

print("Beliebige Taste drücken, um zu würfeln, [Esc] beendet das Spiel.")

while mainloop:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            mainloop = False
        if event.type == KEYDOWN:
            FELD.fill(BLAU)
            ZAHL = random.randrange (1, 7)
            print(ZAHL)
            if ZAHL == 1:
                pygame.draw.circle(FELD, WEISS, P1, 40)
            if ZAHL == 2:
                pygame.draw.circle(FELD, WEISS, P2, 40)
                pygame.draw.circle(FELD, WEISS, P7, 40)
            if ZAHL == 3:
                pygame.draw.circle(FELD, WEISS, P1, 40)
                pygame.draw.circle(FELD, WEISS, P4, 40)
                pygame.draw.circle(FELD, WEISS, P5, 40)
            if ZAHL == 4:
                pygame.draw.circle(FELD, WEISS, P2, 40)
                pygame.draw.circle(FELD, WEISS, P4, 40)
                pygame.draw.circle(FELD, WEISS, P5, 40)
                pygame.draw.circle(FELD, WEISS, P7, 40)
            if ZAHL == 5:
                pygame.draw.circle(FELD, WEISS, P1, 40)
                pygame.draw.circle(FELD, WEISS, P2, 40)
                pygame.draw.circle(FELD, WEISS, P4, 40)
                pygame.draw.circle(FELD, WEISS, P5, 40)
                pygame.draw.circle(FELD, WEISS, P7, 40)
            if ZAHL == 6:
                pygame.draw.circle(FELD, WEISS, P2, 40)
                pygame.draw.circle(FELD, WEISS, P3, 40)
                pygame.draw.circle(FELD, WEISS, P4, 40)
                pygame.draw.circle(FELD, WEISS, P5, 40)
                pygame.draw.circle(FELD, WEISS, P6, 40)
                pygame.draw.circle(FELD, WEISS, P7, 40)
    pygame.display.update()
pygame.quit()
