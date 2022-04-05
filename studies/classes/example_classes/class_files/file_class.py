#!/usr/bin/env python
import sys, os, time



class getStuff():

	def __init__(self):

		sendVar = ""	

	def getVars(self, gottenVar):
		
		gottenVar = input("give me something: ")
		self.sendVar = gottenVar

	def paintVars(self, varToPrint):
	
		varToPrint = self.sendVar
		print("this is the stuff: {}".format(str(varToPrint)))
		time.sleep(1)
		

		



class Simple():

	def __init__(self, var1, var2):
	
		self.var1 = var1
		self.var2 = var2

	def printVar(self):

		print(self.var1)
		print(self.var2)

		

def main():

	print("Just a test\n")

	v1 = input("var 1: ")
	v2 = input("var 2: ")

	newSimple = Simple(v1, v2)
	newSimple.printVar()


	placeholder = ""
	wantThings = getStuff()
	wantThings.getVars(placeholder)

	wantThings.paintVars(placeholder)

if __name__ == '__main__':
	main()
