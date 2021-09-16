#!/usr/bin/env python
import sys

def greet(text, person_type):
	def yell():
		return text.upper() + "!"
	def whisper():
		return text.lower() + "..."

	if person_type == 'friend':
		return whisper
	elif person_type == 'foe':
		return yell
	else:
		sys.exit(0)
		

if __name__ == '__main__':

	person = sys.argv[1]

	greet_function = greet("hello there", person)
	print(greet_function())
	
