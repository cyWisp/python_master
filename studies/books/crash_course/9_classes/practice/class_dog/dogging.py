#!/usr/bin/env python
import os, sys
sys.path.insert(0, './test') #this will insert the gien path to other modules
from dog import Dog

def main():

	newDog = Dog('spot', 12)

	print('{} is {} years old...'.format(newDog.name, str(newDog.age)))

if __name__ == '__main__':
	main()
