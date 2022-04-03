#!/usr/bin/env python

def outer(par):
	loc = par
	def inner():
		return loc
	return inner

if __name__ == '__main__':
	var = 1	
	fun = outer(var)
	print(fun())
