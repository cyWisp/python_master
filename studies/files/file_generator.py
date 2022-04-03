#!/usr/bin/env python
import time, os, sys, os.path

def title():
	os.system('clear')
	print("  _____.__.__  ")               
	print("_/ ____\__|  |   ____   ______")
	print("\   __\|  |  | _/ __ \ /  ___/")
	print(" |  |  |  |  |_\  ___/ \___ \ ")
	print(" |__|  |__|____/\___  >____  >")
	print("                    \/     \/ ")
	print("\n")	

def menu():

	print("1. choice 1")
	print("2. choice 2")
	print("3. choice 3")
	print("4. exit")
	print("\n")

def programLogic():
		
	sentinel = 0
	while sentinel == 0:
		title()
		menu()
		choice = input("Selection: ")
		if choice == str(1):
			writeFile()
			#test: print("\nchoice 1 selected")
			input("Press Enter to Continue...")
			os.system('clear')
		elif choice == str(2):
			print("\nchoice 2 selected")
			input("Press Enter to Continue...")
			os.system('clear')
		elif choice == str(3):
			print("\nchoice 3 selected")
			input("Press Enter to Continue...")
			os.system('clear')
		elif choice == str(4):
			os.system("clear")
			print("Program now exiting...")
			input("Press Enter to Continue...")
			time.sleep(1)
			sys.exit()
		else:
			os.system('clear')
			print("\nPlease enter a number between 1 and 4...")
			input("Press Enter to Continue...")
			
def writeFile():
	
	fileName = input("Enter new file name: ")
	#fileName = str(fileName) + '.txt'
	try:
		with open(fileName, 'w') as writeFile:
			fileData = input("Write: ")
			writeFile.write(fileData)
	except:
		print("Could not open file :(")
	finally:
		writeFile.close()
		print("Data has been written!")
		os.system('clear')
def main():

	title()
	programLogic()

if __name__ == '__main__':
	main()
