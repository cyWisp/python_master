#!/usr/bin/env python
from os import system
from time import sleep
from sys import exit

TITLE = "CESAR CIPHER APP"
MENU_OPTIONS = ['1. Encode', '2. Decode', '3. Exit']

def show_menu(menu_options):
	print(f"{TITLE}\n")
	for option in menu_options:
		print(option)
	print()

def get_user_input():
	try:
		user_choice = int(input("[?] Select: "))
		assert user_choice >= 1 and user_choice <= 3
	except (ValueError, AssertionError):
		print("[x] Please enter a valid selection...")
		return None
	else:
		return user_choice

def cesar_ops():
	alpha = [x for x in range(97, 123)]



def main_menu():
	while True:
		system('clear')
		sleep(1)
	
		show_menu(MENU_OPTIONS)
		user_choice = get_user_input()
	
		if user_choice:
			cesar_ops()
			sleep(2)
		else:
			continue		
		
if __name__ == '__main__':

	main_menu()
