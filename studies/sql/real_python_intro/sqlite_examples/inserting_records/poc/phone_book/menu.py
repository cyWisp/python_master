#!/usr/bin/env python
from sys import exit
from time import sleep
from os import system

MENU = [
	"1. View all",
	"2. Search",
	"3. Add record",
	"4. Delete record",
	"5. Edit record",
	"6. Exit",
]
CHOICE = None

def validate(choice):
	try:
		int(choice)
		assert len(choice) == 1
		assert int(choice) > 0 and int(choice) < 7
	except BaseException: 
		print("[x] Invalid input...")
		sleep(1)
		return True
	else:
		if choice == "6": exit()
		print(f"[+] {choice} Selected...")
		sleep(1)
		return False		

def main_menu():
	while True:
		system('clear')
		sleep(1)

		for i in MENU: print(i)
		CHOICE = input("\n[?] Select: ")
		if validate(CHOICE): continue
		else: return CHOICE

