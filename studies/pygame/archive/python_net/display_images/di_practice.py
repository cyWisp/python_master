#!/usr/bin/env python
import pygame

TITLE = "ANOTHER TEST"
RES = (800, 600)
IMAGES = {"dirby": "./examples/dirby.png"}
COLORS = {"blue": (0, 0, 255)}

def draw_image(screen, image, x, y):
    loaded = pygame.image.load(image)
    screen.blit(loaded, (x, y))

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
            print(event)

        screen.fill(COLORS['blue'])
        draw_image(screen, IMAGES['dirby'], 100, 100)

        pygame.display.update()
        clock.tick(60)