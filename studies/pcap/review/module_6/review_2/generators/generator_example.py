#!/usr/bin/env python

def asts(x):
	ast = "*"
	for i in x:
		ast += ast
		yield ast

if __name__ == '__main__':
	for i in asts(5):
		print(i)
	
