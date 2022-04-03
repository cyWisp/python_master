#!/usr/bin/env python
import pygame

TITLE = "Movement Example 1"
RES = {"width": 800, "height": 600}
COLORS = {"background": (125, 125, 125)}
IMAGES = {"dirby": "../images/dirby.png"}

global dirby_x, dirby_y, dirby_speed_x, dirby_speed_y
dirby_x, dirby_y = 100.0, 100.0
dirby_speed_x, dirby_speed_y = 0.0, 0.0

def draw_image(screen, image, x, y):
	loaded_image = pygame.image.load(image)
	screen.blit(loaded_image, (x, y))

def check_events():
	global dirby_x, dirby_y, dirby_speed_x, dirby_speed_y

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()			
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				dirby_speed_x = -5
			elif event.key == pygame.K_d:
				dirby_speed_x = 5
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				dirby_speed_x = 0
	
		# print(event)
	dirby_x += dirby_speed_x
	

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((RES['width'], RES['height']))
	pygame.display.set_caption(TITLE)
	clock = pygame.time.Clock()

	while True:

		check_events()

		screen.fill(COLORS['background'])
		draw_image(screen, IMAGES['dirby'], dirby_x, dirby_y)

		pygame.display.update()
		clock.tick(60)
