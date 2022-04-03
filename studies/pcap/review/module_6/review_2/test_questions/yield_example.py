#!/usr/bin/env python

def yield_sum(x):
	yield [i for i in range(x)]

if __name__ == '__main__':
	for i in yield_sum(5):
		print(i)
