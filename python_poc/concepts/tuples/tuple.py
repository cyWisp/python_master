#!/usr/bin/env python
import os, sys

def main():

	print("This is a tuple with 5 values")
	thisTuple = ('tuna', 'salad', 'burgers', 'fries', 'brains')
	for tup in thisTuple:
		print(tup)

	print("try to change one of the values: ")
	thisTuple = ('brownie', 'face', 'nine', 'jams', 'petunias')

	for tup in thisTuple:
		print(tup)	

if __name__ == '__main__':
	main()
