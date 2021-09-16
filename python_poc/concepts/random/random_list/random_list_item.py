#!/usr/bin/env python
import random

def main():
	new_list = ['first', 'second', 'third', 'fourth', 'fifth']

	random_item = random.choice(new_list)

	print('List item: {}'.format(random_item))

if __name__ == '__main__':
	main()
