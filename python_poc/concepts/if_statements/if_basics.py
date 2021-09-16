#!/usr/bin/env python
import os, sys

def main():
	
	cars = ['honda', 'bmw', 'volkswagon', 'toyota', 'ferrari']
	print("Original list:\n")
	for car in cars:
		print(car, end=', ')
	print('\n')

	print('\n The name BMW should be capitalized')
	print('printing the list again:\n')
	
	for car in cars:
		if car == 'bmw':
			print(car.upper())
		else:
			print(car)
	

	
if __name__ == '__main__':
	main()
