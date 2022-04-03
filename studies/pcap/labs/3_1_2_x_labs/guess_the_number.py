#!/usr/bin/env python
from random import randint

if __name__ == '__main__':

	magic_number = randint(1, 30)

	print("Guess a number from 1 to 30...")
	print("If you guess wrong, you'll be stuck in an eternal loop...FOREVER!!!")
	
	while True:
		guess = int(input("Your guess: "))
		if guess < magic_number:
			print("Higher")
		elif guess > magic_number:
			print("Lower")
		
		if guess == magic_number:
			print("Correct!")
			break
	


