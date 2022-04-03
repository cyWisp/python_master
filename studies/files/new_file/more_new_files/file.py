#!/usr/bin/env python
import sys

def main():

	numFiles = input("Number of files: ")
	numFiles = int(numFiles)
	fileName = input("File Name: ")
	contents = input("Contents: ")
	nameList = []
	origName = fileName

	#content = "Content: "

	for numFile in range(1, (numFiles + 1)):
		
		fileName = str(fileName) + "_" + str(numFile) + ".txt"
		nameList.append(fileName)
		
		try:
			with open(fileName, 'w') as newFile:
				newFile.write(contents)
		except: 
			print("could not open file...")
		finally:
			newFile.close()
			print("Finished write...")
				

		fileName = origName
		

		#test print(numFile)

	for name in nameList:
		print(str(name))
	
		

	

if __name__ == '__main__':
	main()
