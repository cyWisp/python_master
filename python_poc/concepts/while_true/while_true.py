#!/usr/bin/env python
import time, os

def main():

	counter = 0
	check = True

	while check == True:
		print(counter)
		counter = counter + 1
		if counter == 10:
			check = False

if __name__=='__main__':
	main()
