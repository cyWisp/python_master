#!/usr/bin/env python

def yell(text):
	return text.upper() + "!"

if __name__ == '__main__':

	# Demonstrating the usage of the map() function
	
	greetings = list(map(yell, ['hello', 'hey', 'hi']))
	for g in greetings:
		print(g)
	
