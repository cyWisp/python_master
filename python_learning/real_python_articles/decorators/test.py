#!/usr/bin/env python

def greet(func):
	def yell():
		return func().upper() + "!"
	def whisper():
		return func().lower() + "..."
	
	if func() == "hi":
		return whisper
	else:
		return yell

@greet
def greeting():
	return "hello"

if __name__ == '__main__':

	print(greeting())

