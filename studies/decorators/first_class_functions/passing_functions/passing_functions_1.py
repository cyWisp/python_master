#!/usr/bin/env python

def greet(func):
	greeting = func("Hi, I am a python program")
	print(greeting)

def yell(text):
	return text.upper() + "!"

def whisper(text):
	return text.lower() + "..."

if __name__ == '__main__':

	greet(yell)
	greet(whisper)	
