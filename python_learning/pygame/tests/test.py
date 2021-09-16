#!/usr/bin/env python
import pygame, random
from settings import SCREEN_SETTINGS, COLORS
import game_functions as gf
from player import Player
from ground import Ground

def start():
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SETTINGS['RES'])
	pygame.display.set_caption(SCREEN_SETTINGS['TITLE'])
	clock = pygame.time.Clock()

	player = Player(screen, COLORS['WHITE'])
	ground = Ground(screen, COLORS['RED'])

	return screen, clock, player, ground

def update(screen, clock, player, ground):
	while True:
		gf.check_events(player)


		screen.fill(COLORS['BLACK'])
		player.move()
		player.draw()

		ground.draw()

		pygame.display.flip()
		clock.tick(SCREEN_SETTINGS['FPS'])

if __name__ == '__main__':
	screen, clock, player, ground = start()
	update(screen, clock, player, ground)


