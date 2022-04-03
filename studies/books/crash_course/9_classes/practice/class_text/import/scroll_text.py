#!/usr/bin/env python
import os, time

class TextScroll():

	def __init__(self, text):
		self.text = text

	def marquee(self):
		os.system('clear')
		time.sleep(1)

		given_text = str(self.text)
		text_arr = []
	
		for character in given_text:
			text_arr.append(character)

		while True:
			for letter in text_arr:
				print(letter, end='', flush=True)
				time.sleep(.003)
		
				
			
				
			
