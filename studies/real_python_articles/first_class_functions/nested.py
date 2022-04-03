#!/usr/bin/env python


def get_speak_func(volume, text):
	def whisper(text):
		return text.lower() + '...'
	def yell(text):
		return text.upper() + '!'

	if volume >= 5:
		return yell(text)
	elif volume < 5:
		return whisper(text)

if __name__ == '__main__':

	greeting = get_speak_func(6, 'this is some text')
	print(greeting)

