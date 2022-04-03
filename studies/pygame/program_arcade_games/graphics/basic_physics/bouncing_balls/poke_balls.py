#!/usr/bin/env python
import pygame, random

# Colors
BLACK = (0 ,0 ,0)

# Image
IMAGE = pygame.image.load("./poke_ball_3_scaled.png")

# Settings
TITLE = "Pokeballs!"
RES = (800, 600)
FPS = 60

# Ball Settings
BALL_SIZE = IMAGE.get_rect().size

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        
        self.speed_x = 5
        self.speed_y = 5

        self.size = BALL_SIZE

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(RES)
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    # Make a ball
    ball = Ball()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # Move
        ball.x += ball.speed_x
        ball.y += ball.speed_y

        # Bounce
        if ball.x > (RES[0] - ball.size[0]) or ball.x < 0:
            ball.speed_x *= -1
        if ball.y > (RES[1] - ball.size[1]) or ball.y < 0:
            ball.speed_y *= -1

        screen.fill(BLACK)
        screen.blit(IMAGE, (ball.x, ball.y))

        pygame.display.flip()
        clock.tick(FPS)
