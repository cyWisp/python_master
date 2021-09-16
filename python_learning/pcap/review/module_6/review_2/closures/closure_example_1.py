#!/usr/bin/env python

def add_two(n):
	def inner():
		return n + 2
	return inner

if __name__ == '__main__':
	var = add_two(3)
	print(var())
