#!/usr/bin/env python
import os, sys

def main():
	
	names = ['rob', 'jess', 'john', 'sam', 'benji', 'martin']
	
	print("outputting the last 3 names:\n")
	print(names[-3:])

	print("\noutputtin the last 3 names again in a different way:\n")
	print(names[3:])


	print("\noutputting the first 3 names:\n")
	print(names[:3])

	print("\noutputting the first 3 names in a different way\n")
	print(names[:-3])


	print("\n copying the list:\n")
	newList = names[:]
	newList.append('new entry')
	
	print("\noriginal list:\n")
	for name in names:
		print(name)	
	
	print("\nNew list:\n")
	for name in newList:
		print(name)
	

if __name__ == '__main__':
	main() 
