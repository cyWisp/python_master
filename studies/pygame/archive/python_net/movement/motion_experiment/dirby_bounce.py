#!/usr/bin/env python
import pygame

TITLE = "MOTION TEST"
RES = {"width": 800, "height": 600}
IMAGES = {"dirby": "./dirby.png"}
COLORS = {"grey": (125, 125, 125)}

global dirby_x, dirby_y, dirby_speed_x, dirby_speed_y
dirby_x, dirby_y, dirby_speed_x, dirby_speed_y = 100, 100, 5, 3

def draw_image(screen, image, x, y):
	loaded = pygame.image.load(image)
	screen.blit(loaded, (x, y))

def move():
	global dirby_x, dirby_y, dirby_speed_x, dirby_speed_y
	dirby_x = dirby_x + dirby_speed_x
	dirby_y = dirby_y + dirby_speed_y
	
	if dirby_x > RES['width']:
		dirby_speed_x = -(dirby_speed_x)
	if dirby_x < 0:
		dirby_speed_x = -(dirby_speed_x)
	if dirby_y > RES['height']:
		dirby_speed_y = -(dirby_speed_y)
	if dirby_y < 0:
		dirby_speed_y = -(dirby_speed_y)
		


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
			print(event)

		screen.fill(COLORS['grey'])
		draw_image(screen, IMAGES['dirby'], dirby_x, dirby_y)
		move()

		pygame.display.update()
		clock.tick(60)
