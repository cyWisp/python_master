#!/usr/bin/env python

def yell(text):
	return text.upper() + "!"

def whisper(text):
	return text.lower() + "..."

def address(text):
	return text.title() + " :)"

def greet(func, text):
	greeting = func(text)
	print(greeting)

if __name__ == '__main__':

	greet(yell, "hi there")
	greet(whisper, "IM WHISPERING")
	greet(address, "Why hello there sir")
