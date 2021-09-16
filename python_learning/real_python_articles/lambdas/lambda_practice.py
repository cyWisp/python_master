#!/usr/bin/env python

if __name__ == '__main__':

	list_1 = [x for x in range(5)]
	sqaured = list(map(lambda x: x ** 2, list_1))

	print(sqaured)
