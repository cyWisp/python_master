#!/usr/bin/env python

def get_speak_func(text, volume):
	def whisper():
		return text.lower() + '...'
	def yell():
		return text.upper() + '!'

	if volume > 5:
		return yell()
	else:
		return whisper()

if __name__ == '__main__':

	print(get_speak_func('hello world', 6))
