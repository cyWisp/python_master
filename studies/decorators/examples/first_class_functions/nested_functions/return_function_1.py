#!/usr/bin/env python

def get_speak_func(volume):
	def whisper(text):
		return text.lower() + "..."
	def yell(text):
		return text.upper() + "!"

	if volume > 0.5:
		return yell
	else:
		return whisper

if __name__ == '__main__':


	r_function = get_speak_func(.7)
	print(r_function("hello person"))
	
