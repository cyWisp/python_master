#!/usr/bin/env python

def speak(text):
	def whisper(t):
		return t.lower() + "..."
	return whisper(text)

if __name__ == '__main__':

	spoken = speak("Hello there")
	print(spoken)
