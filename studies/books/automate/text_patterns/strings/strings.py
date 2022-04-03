#!/usr/bin/env python
import os

def main():

	word = input('string: ')
	length = len(word)

	for i in range(0, length):
		print(str(i) + ' ' + word[i])

	print('\nLength was: {}'.format(str(length)))	

if __name__ == '__main__':
	main()
