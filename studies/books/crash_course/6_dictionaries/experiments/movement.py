#!/usr/bin/env python
import os

def main():

	position = {'x':0, 'y':0, 'fast':3, 'medium':2, 'slow':1}

	while True:
		print('Current position: {},{}'.format(position['x'], position['y']))
		print('Where would you like to move?\nUp = u\nDown = d\nRight = r\nLeft = l')
		
		move = input('Move: ')
		move = str(move)

		speed = input('At what speed?\nFast = f\nMedium = m\nSlow = s\nSpeed: ')
		speed == str(speed)

		playerSpeed = 0

		if speed == 'f':
			playerSpeed = position['fast']
		elif speed == 'm':
			playerSpeed = position['medium']
		elif speed == 's':
			playerSpeed = position['slow']

		if move == 'u':
			position['y'] = position['y'] + playerSpeed
		elif move == 'd':
			position['y'] = position['y'] - playerSpeed
		elif move == 'r':
			position['x'] = position['x'] + playerSpeed
		elif move == 'l':
			position['x'] = position['x'] - playerSpeed	

	

if __name__ == '__main__':
	main()
