#!/usr/bin/env python

# Demonstrating the fact that functions can be nested

def speak(text):
	def whisper(t):
		return t.lower() + "..."
	return whisper(text)

if __name__ == '__main__':

	print(speak("HI THERE"))
