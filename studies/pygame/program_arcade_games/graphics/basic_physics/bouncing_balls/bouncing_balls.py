#!/usr/bin/env python
"""
This example shows having multiple balls bouncing around
at the same time. You can hit the space bar to spawn more balls.
"""

import pygame, random

# Colors
RED = (255, 0, 0)
BLUE = (0,255, 0)
GREEN = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game Settings
TITLE = "Bouncing Balls"
RES = (800, 600)
FPS = 60

# Ball Settings
BALL_SIZE = 10

class Ball:
    # Class to keep track of a ball's location and vector
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

def make_ball():
    # Function to make a new, random ball
    ball = Ball()
    # Starting position of the ball
    # Take into account the ball size, so we don't spawn on the edge.
    ball.x = random.randrange(BALL_SIZE, RES[0] - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, RES[1] - BALL_SIZE)

    # Speed and direction of the ball
    ball.change_x = random.randrange(-5, 5)
    ball.change_y = random.randrange(-5, 5)

    return ball

if __name__ == '__main__':
    # Main
    pygame.init()
    screen = pygame.display.set_mode(RES)
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    # Create a ball list and a starter ball
    # Append it to the list
    ball_list = []
    ball = make_ball()
    ball_list.append(ball)

    font = pygame.font.SysFont('Calibri', 16, True, False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                # Space bar = spawn a new ball
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_list.append(ball)
        
        for ball in ball_list:
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y

            if ball.x > (RES[0] - BALL_SIZE) or ball.x < 0:
                ball.change_x *= -1
            if ball.y > (RES[1] - BALL_SIZE) or ball.y < 0:
                ball.change_y *= -1
        
        screen.fill(BLACK)
        
        num_balls = f"Count: {str(len(ball_list))}"
        ball_count = font.render(num_balls, True, RED)
        screen.blit(ball_count, [20, 580])

        instructions = font.render("Press space to make more balls! :D", True, GREEN)
        screen.blit(instructions, [20, 20])

        # Draw balls
        for ball in ball_list:
            pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)

        

        pygame.display.flip()
        clock.tick(FPS)