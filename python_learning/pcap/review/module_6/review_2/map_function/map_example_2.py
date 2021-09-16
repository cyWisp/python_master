#!/usr/bin/env python

if __name__ == '__main__':
	list1 = [x for x in range(5)]
	list2 = list(map(lambda x: 2 ** x, list1))

	print(list2)

	for x in map(lambda x: x * x, list2):
		print(x, end=' ')
	print()
