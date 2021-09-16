#!/usr/bin/env python
import time, os, sys

def menu():

	print("\tJust a menu")
	print("1. item 1")
	print("2. item 2")
	print("3. item 3")
	print("4. exit")

def logic():
	
	sentinel = 0
	while sentinel == 0:
		menu()
		choice = userInput()
		if choice == 1:
			print("choice {} selected").format(choice)
			time.sleep(1)
		elif choice == 2:
			print("choice {} selected").format(choice)
			time.sleep(1)
		elif choice == 3:
			print("choice {} selected").format(choice)
			time.sleep(1)
		elif choice == 4:
			input("press enter to exit...")
			sys.exit()
		os.system('clear')
		time.sleep(1)
	
def userInput():	
	
	uInput = input("Input[1-4]: ")
	return uInput
	
def main():
	
	logic()	

if __name__=='__main__':
	main()
