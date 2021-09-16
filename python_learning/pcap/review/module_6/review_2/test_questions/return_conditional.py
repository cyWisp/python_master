#!/usr/bin/env python

def fun(x):
	return 1 if x % 2 != 0 else 2

if __name__ == '__main__':
	print(fun(fun(1)))
