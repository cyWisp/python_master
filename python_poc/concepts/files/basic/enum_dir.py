#!/usr/bin/env python
import os

def main():
	
	fileNameList = []
	
	for root, dirs, files in os.walk('.'):
		for name in files:
			stripName = name.strip('./')
			fileNameList.append(stripName)
	print(fileNameList)

	print("\n\n")

	for fName in fileNameList:
		print(fName)
				

if __name__=='__main__':
	main()
