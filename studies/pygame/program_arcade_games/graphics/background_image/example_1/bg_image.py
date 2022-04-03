#!/usr/bin/env python
import pygame

IMAGE = pygame.image.load("./pixeal_art_background_1.jpg")
RES = (800, 600)
TITLE = "Background Image Test"
ORIGIN = (0, 0)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(RES)
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(IMAGE, ORIGIN)

        pygame.display.flip()
        clock.tick(60)
        
    

