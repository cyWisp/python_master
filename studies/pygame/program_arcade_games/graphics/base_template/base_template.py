#!/usr/bin/env python
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
RES = (800, 600)

if __name__ == '__main__':

    pygame.init()                                           # initiate pygame
    screen = pygame.display.set_mode(RES)                   # set window size (RES)
    pygame.display.set_caption("Introduction to Graphics")  # set title of pygame window
    clock = pygame.time.Clock()                             # frame rate

    # Main Program Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # --- Game logic should go here --- #

        # --- Screen clearing code goes here --- #

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit-ing the
        # background image
        screen.fill(RED)

        # --- Drawing code should go here --- #

        # Update the screen with what we've drawn.
        pygame.display.flip()

        # Limit the game to 60 frames per second
        clock.tick(60)
    