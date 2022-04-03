#!/usr/bin/env python
import os

def main():

	string = 'Robert Daglio'
	print(string[0])
	print(string[0:6])
	print(string[:6])
	print(string[6:])


	
	if ('Rob' in string) == True:
		print('Interesting...')


if __name__ == '__main__':
	main() 
