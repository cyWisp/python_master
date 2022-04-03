#!/usr/bin/env python
import os, sys, test

def main():

	l = input("Length: ")
	w = input("Width: ")

	res = test.area(int(l), int(w))

	print("The area is {}".format(int(res)))

if __name__=='__main__':
	main()
