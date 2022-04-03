#!/usr/bin/env python
import os

def main():

	word = input('String: ')
	index = input('String position: ')
	index =  int(index)
	length = len(word)

	print('Index: {}, Length: {}'.format(index, length))		



if __name__ == '__main__':
	main()
