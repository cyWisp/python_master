#!/usr/bin/env python
import os, sys
from class_dog import Dog

def main():

	myDog = Dog('lassie', '5')

	print("My dog's name is " + myDog.name)
	print(myDog.name + " is " + myDog.age + " years old.")

	myDog.rollover()


if __name__=='__main__':
	main()
