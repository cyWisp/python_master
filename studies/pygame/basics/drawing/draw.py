#!/usr/bin/env python
import sys, pygame
from pygame.locals import *

if __name__ == '__main__':

    # Set up window
    DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
    pygame.display.set_caption('Drawing...')

    # Set up colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # Draw on the surface object
    DISPLAYSURF.fill(WHITE)
    pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
    pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
    pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
    pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)

    pixObj = pygame.PixelArray(DISPLAYSURF)
    pixObj[480][380] = BLACK
    pixObj[482][382] = BLACK
    pixObj[484][384] = BLACK
    pixObj[486][386] = BLACK
    pixObj[488][388] = BLACK

    del pixObj

    # Run game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    
