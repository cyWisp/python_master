#!/usr/bin/env python

def add(first_num, second_num):
	return first_num + second_num

def subtract(first_num, second_num):
	return first_num - second_num

def calculate(calc, first_num, second_num):
	return calc(first_num, second_num)

if __name__ == '__main__':

	print(calculate(add, 5, 3))
	print(calculate(subtract, 5, 3))
