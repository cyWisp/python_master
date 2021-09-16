#!/usr/bin/env python

def greet(func):
	greeting = func('hello, i am a python program')
	print(greeting)

def yell(text):
	return text.upper() + "!"
def whisper(text):
	return text.lower() + "..."

if __name__ == '__main__':

	greet(yell)
	greet(whisper)

	print(list(map(yell, ['hello', 'hey there', 'whats up'])))
	
