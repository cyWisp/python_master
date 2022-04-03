#!/usr/bin/env python
import os

def main():

	person = {'Name':'Rob','Age':'32','Race':'Hspanic'}

	print('Looping through all key-value pairs:\n\n')
	for key, value in person.items():
		print('{}:{}'.format(key, value))
	print('\nLooping through keys only:\n\n')
	for key in person.keys():
		print('{}'.format(key))
	print('\nLooping through values only:\n\n')
	for value in person.values():
		print('{}'.format(value))
	

if __name__ == '__main__':
	main()
