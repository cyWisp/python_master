#!/usr/bin/env python

def add_two(x):
	return x + 2

if __name__ == '__main__':
	nums = [1, 2, 3, 4, 5]
	added = map(add_two, nums)

	for i in added:
		print(i)
	
