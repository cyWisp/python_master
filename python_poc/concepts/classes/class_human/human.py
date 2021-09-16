#!/usr/bin/env python
import os, sys
from class_human import Human

def main():
	
	newHuman = Human('rob', '31')

	newHuman.talk()
	print(newHuman.name + " is " + newHuman.age + " years old.")
	
if __name__=='__main__':
	main()
