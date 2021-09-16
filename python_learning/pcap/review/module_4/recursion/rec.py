#!/usr/bin/env python
from time import sleep
from sys import exit

def time_rec(x):
	if x < 11:
		print(x)
		x += 1
		time_rec(x)
	else:
		exit(0)

if __name__ == '__main__':

	x = 0
	time_rec(x)
