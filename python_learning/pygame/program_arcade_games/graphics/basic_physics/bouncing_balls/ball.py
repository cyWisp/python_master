#!/usr/bin/env python
import pygame

# Colors
RED = (255, 0, 0)
BLUE = (0,255, 0)
GREEN = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Settings
TITLE = "Bouncing Ball"
RES = (800, 600)
FPS = 60

# Ball Settings
ball_x, ball_y = 50, 50
speed_x, speed_y = 10, 5


if __name__ == '__main__':
    pygame.init
    screen = pygame.display.set_mode(RES)
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # Move
        ball_x += speed_x
        ball_y += speed_y

        # Bounce
        if ball_x > 780 or ball_x < 0:
            speed_x = speed_x * -1
        if ball_y > 580 or ball_y < 0:
            speed_y = speed_y * -1

        # Fill background
        screen.fill(BLACK)

        # Draw ellipse
        pygame.draw.ellipse(screen, WHITE, [ball_x, ball_y, 20, 20])

        pygame.display.flip()
        clock.tick(FPS)