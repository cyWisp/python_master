#!/usr/bin/env python

import os, sys

def main():
	
	originalName = "fileName"
	appendName = input("add file extension: ")

	concatName = str(originalName) + str(appendName)	

	print("concatenated name: " + concatName)
	

if __name__=='__main__':
	main()
