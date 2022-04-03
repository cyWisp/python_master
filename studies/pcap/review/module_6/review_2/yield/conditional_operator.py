#!/usr/bin/env python

def fun(a):
	return True if a > 5 else False

if __name__ == '__main__':

	print(fun(6))

	test = list()

	for x in range(10):
		test.append(x if x % 2 == 0 else "nope")

	for i in test: print(i)
