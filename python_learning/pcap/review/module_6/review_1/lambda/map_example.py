#!/usr/bin/env python

list_1 = [x for x in range(5)]

# saving the mapped lambda in a list
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

# using the mapped lambda in iteration
for x in map(lambda x: x * 2, list_2):
	print(x, end=', ')
print()
