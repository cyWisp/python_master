#!/usr/bin/env python
import pygame

RES = {
	"width": 800,
	"height": 600,
}

TITLE = "dirby!"
COLORS = {
	"black": (0, 0, 0),
	"white": (255, 255, 255)
}

IMAGES = {
	"dirby": "./dirby.png"
}

def draw_image(screen, image, x, y):
	loaded_image = pygame.image.load(image)
	screen.blit(loaded_image, (x, y))

if __name__ == '__main__':

	pygame.init()
	screen = pygame.display.set_mode((RES['width'], RES['height']))
	pygame.display.set_caption(TITLE)
	clock = pygame.time.Clock()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		# "log" all events to console
		print(event)

		# draw dirby
		draw_image(screen, IMAGES["dirby"], 100, 100)

		pygame.display.update()
		clock.tick(60)


