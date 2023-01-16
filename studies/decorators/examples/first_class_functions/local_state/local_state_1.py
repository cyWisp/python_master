#!/usr/bin/env python

def get_speak_func(text, volume):
	def whisper():
		return text.lower() + '...'
	def yell():
		return text.upper() + "!"

	if volume > 0.5:
		return yell
	else:
		return whisper

if __name__ == '__main__':

	# Take note of the call, and the extra () at the end of the function call
	# The returned function is being evaluated after the initial function call
	# to get_speak_func()
	print(get_speak_func("Hello, world", 0.7)())
	
