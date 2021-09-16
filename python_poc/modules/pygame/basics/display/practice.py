#!/usr/bin/env python
import pygame, sys
from pygame.locals import *

if __name__ == '__main__':

    pygame.init()
    DISPLAY = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('practice')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()