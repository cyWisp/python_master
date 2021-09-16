#!/usr/bin/env python
import os, sys
from class_person import *

def main():
	
	printBanner()
	newPerson = Person('Rob', '31')

	newPerson.sit()
	newPerson.walk()
	newPerson.sayMyName()

	newPerson.setJobs()

	print(str(newPerson.jobs))

if __name__ == '__main__':
	main()
