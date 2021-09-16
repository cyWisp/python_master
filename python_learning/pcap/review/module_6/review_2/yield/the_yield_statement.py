#!/usr/bin/env python

def fun(n):
	for i in range(n):
		if i % 2 == 0:
			yield i

if __name__ == '__main__':
	nums = list(fun(10))

	print(type(nums))
