#!/usr/bin/env python
import pygame

IMAGE = pygame.image.load("./custom_background_1.png")
ORIGIN = (0, 0)
RES = (800, 600)
TITLE = "Custom Background Test"

def quit_game():
    pygame.quit()
    quit()

if __name__ == '__main__':
    pygame.init()
    
    screen = pygame.display.set_mode(RES)
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        
        screen.blit(IMAGE, ORIGIN)
        pygame.display.flip()
        clock.tick(60)
    quit_game()