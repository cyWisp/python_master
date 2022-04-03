#!/usr/bin/env python

def squared(num):
	return num ** 2

if __name__ == '__main__':

	nums = [2, 5, 6]

	squares = list(map(squared, nums))
	[print(x) for x in squares]
	
