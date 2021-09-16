#!/usr/bin/env python

if __name__=='__main__':

	some_func = lambda x, y: [i for i in range(x, y)]
	square = lambda x, y: x ** y

	for i in some_func(1, 10):
		print(i)

	print(square(2, 3))
