#!/usr/bin/env python
import pygame, sys

RES = (800, 600)

if __name__ == '__main__':

	pygame.init()

	screen = pygame.display.set_mode((RES))					# Tuple (width, height)
	pygame.display.set_caption('This is just a test...')	# Sets the title of the window

	clock = pygame.time.Clock()								# Sets in-game time

	# Main game loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			# Print any event registered to the console
			print(event)

		pygame.display.update()
		clock.tick(60)

	pygame.quit()
	quit()

