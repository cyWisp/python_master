#!/usr/bin/env python

def yell(text):
	print(f"{text.upper()}!")

if __name__ == '__main__':

	yell("hello")
	bark = yell

	bark('woof')

	del yell
	bark('still bark...')

	
	
