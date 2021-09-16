#!/usr/bin/env python

if __name__ == '__main__':

	word = "Spathiphyllum"

	while True:
		user_input = input("Plant: ")
		
		if user_input == word.lower():
			print(f"No, I want a big {word}")
		elif user_input == word:
			print(f"Yes - {word} is the best plant ever!")
			break
		else:
			print(f"{word}! Not {user_input}!")
	
