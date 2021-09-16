#!/usr/bin/env python

def add(num_1, num_2):
	return num_1 + num_2

def mult(num_1, num_2):
	return num_1 * num_2

def div(num_1, num_2):
	return num_1 / num_2

def sub(num_1, num_2):
	return num_1 - num_2

def print_result(func):
	result = func(10, 6)
	print(result)

if __name__ == '__main__':

	print_result(add)
	print_result(mult)
	print_result(div)
	print_result(sub)
	
