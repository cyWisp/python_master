#!/usr/bin/env python
import os, sys


def showMenu():

	print("*--===|test menu|===--*\n")
	print("1. choice 1")
	print("2. choice 2")
	print("3. choice 3")
	print("4. exit")

def getChoice():

	choice = input("Selection: ")
	choice = str(choice)
	return choice

def menuLogic():

	sentinel = 0
	while sentinel == 0:
		showMenu()
		choice = getChoice()
		if choice == '1':
			print("choice 1 selected")
			input("enter to continue")
			os.system('clear')	
		elif choice == '2':
			print("choice 2 selected")
			input("enter to continue")
			os.system('clear')	
		elif choice == '3':
			print("choice 3 selected")
			input("enter to continue")
			os.system('clear')	
		elif choice == '4':
			print("choice 4 selected")	
			sys.exit()



def main():

	menuLogic()

if __name__ == '__main__':
	main()
