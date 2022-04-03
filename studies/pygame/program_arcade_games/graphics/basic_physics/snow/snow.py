#!/usr/bin/env python
import pygame, random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

TITLE = "Snow"
RES = (800, 600)

def quit_game():
    pygame.quit()
    quit()

snow_list = list()

for i in range(50):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    snow_list.append([x, y])

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(RES)
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        
        screen.fill(BLACK)

        for i in range(len(snow_list)):
            pygame.draw.circle(screen, WHITE, snow_list[i], 2)
            snow_list[i][1] += 1
        
            if snow_list[i][1] > 600:
                y = random.randrange(-50, -10)
                snow_list[i][1] = y
                # Give it a new x position
                x = random.randrange(0, 800)
                snow_list[i][0] = x

        pygame.display.flip()
        clock.tick(60)
    quit_game()
