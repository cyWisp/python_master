#!/usr/bin/env python
import pygame
from sys import exit

RES = (800, 600)

if __name__ == '__main__':
	
	pygame.init()
	screen = pygame.display.set_mode(RES)
	pygame.display.set_caption("Testing...")
	clock = pygame.time.Clock()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

			print(event)

		pygame.display.update()
		clock.tick(60)

	pygame.quit()
	exit()
