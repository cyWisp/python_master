#!/usr/bin/env python
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

TITLE = "Bouncing Rectangle Demo"
RES = (800, 600)

def quit_game():
    pygame.quit()
    quit()

# Starting position of the rectangle
rect_x = 50
rect_y = 50

# Speed and direction of rectangle
rect_change_x = 2
rect_change_y = 2

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(RES)
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        
        # --- Logic --- #
        # Move the rectangle starting point
        rect_x += rect_change_x
        rect_y += rect_change_y

        # Bounce the rectangle off the walls
        if rect_y > 580 or rect_y < 0:
            rect_change_y = rect_change_y * -1  # make it negative
        if rect_x > 780 or rect_x < 0:
            rect_change_x = rect_change_x * -1  # make it negative

        # --- Drawing --- #
        # Set the screen background
        screen.fill(BLACK)

        # Draw the rectangle
        pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 20, 20])

        pygame.display.flip()
        clock.tick(60)
    quit_game()
