#!/usr/bin/env python

def yell(text):
	return text.upper() + "!"

if __name__ == '__main__':

	greetings = ["hello", "hey", "hi"]
	greets = list(map(yell, greetings))

	print(greets)
