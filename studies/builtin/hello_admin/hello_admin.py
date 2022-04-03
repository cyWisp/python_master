#!/usr/bin/env python
import time, os, sys

def main():

	names = ['rdaglio', 'albury', 'admin', 'edson', 'julio']

	for name in names:

		if name == 'admin':
			
			print("Welcome {}, click on 'menu' for admin tools...\n".format(str(name)))
		else:

			print("Hello " + str(name) + " welcome to the site!\n" )

	

if __name__=='__main__':
	main()
