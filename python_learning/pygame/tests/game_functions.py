#!/usr/bin/env python
import pygame
from sys import exit

def key_down(player, event):
	if event.key == pygame.K_a:
		player.moving_left = True
	elif event.key == pygame.K_d:
		player.moving_right = True
	elif event.key == pygame.K_w:
		player.jump = True

def key_up(player, event):
	if event.key == pygame.K_a:
		player.moving_left = False
	elif event.key == pygame.K_d:
		player.moving_right = False
	elif event.key == pygame.K_w:
		player.jump = False

def check_events(player):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN:
			key_down(player, event)
		elif event.type == pygame.KEYUP:
			key_up(player, event)

				
