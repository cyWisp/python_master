#!/usr/bin/env/python
import os, sys
from class_bike import Bike

def main():

	bMake = input("Make: ")
	bModel = input("Model: ")
	
	thisBike = Bike(bMake, bModel)

	thisBike.displayInfo()

	thisBike.enterDateSold()

	print("This bike was sold on " + str(thisBike.dateSold))


if __name__=="__main__":
	main()
