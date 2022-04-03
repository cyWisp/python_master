#!/usr/bin/env python
import pygame

BG_COLOR = (120, 120, 120)

if __name__ == '__main__':

	pygame.init()

	screen = pygame.display.set_mode((800, 600))
	rect_color = (120, 0, 0)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		screen.fill(BG_COLOR)
		pygame.draw.rect(screen, rect_color, pygame.Rect(100, 30, 100, 80))
	
		pygame.display.flip()
	
