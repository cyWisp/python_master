#!/usr/bin/env python
from time import sleep
from os import system
from random import randint
from sys import exit

BANNER = """___________________________ 
\\_____   \\_____   \\_____   \\
   /   __/  /   __/  /   __/
  |   |    |   |    |   |   
  |___|    |___|    |___|   
  <___>    <___>    <___>   
"""

def get_user_input():	
	try:
		guess = int(input("[?] Guess: "))
	except TypeError as type_error:
		print("[x] Please enter a valid integer...")
	except ValueError as val_error:
		print("[x] Please enter a valid integer...")
	else:
		if guess < 1 and guess > 10:
			print("[x] Please enter a value between 1 and 10 (inclusive)...")
		else:
			return guess

def play_again():
	while True:
		choice = input("[?] Play again? [y or n]: ")
		choice = choice.upper()
		if choice != "Y" and choice != "N":
			print("[x] Please enter either 'y' or 'n'...")
			continue
		else:
			if choice == "Y":
				print("[!] Reset!")
				return 3, randint(1, 10)
			else:
				exit(0)

def play():
	num = randint(1, 10)
	tries = 3

	print("[+] Guess the number- 1-10: ")

	while True:
		guess = get_user_input()
		tries -= 1
		if tries == 0:
			print("[x] You lose :(")
			tries, num = play_again()	
		else:
			if guess == num:
				print("[!] You guessed it!!!")
				tries, num = play_again()
			else:
				print(f"Nope, you got {tries} tries left...")

		

if __name__ == '__main__':

	system('clear')
	sleep(1)

	print(BANNER)
	play()
