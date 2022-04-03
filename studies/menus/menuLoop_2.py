#!/usr/bin/env python
import time, os, sys

def main():
	
	sentinel = 0
	while sentinel == 0:
		
		os.system('clear')
		
		print("menu test 2")
		print("1. item 1")
		print("2. item 2")
		print("3. item 3")
		print("4. item 4")
		
		choice = input("input: ")
		choice = int(choice)
		
		if choice == 1:
			choice = str(choice)
			print("choice {} selected".format(choice))
			time.sleep(2)
		elif choice == 2:
			choice = str(choice)
			print("choice {} selected".format(choice))
			time.sleep(2)
		elif choice == 3:
			choice = str(choice)
			print("choice {} elected".format(choice))
			time.sleep(2)
		elif choice == 4:
			sys.exit()


if __name__ == '__main__':
	main()
