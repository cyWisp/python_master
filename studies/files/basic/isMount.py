#!/usr/bin/env python
import os

def main():
	
	path = '/mnt'
	isMount = os.path.ismount(path)
	print(isMount)

	#os.path.join() example
	firstPart = '/home/wisp'
	secondPart = 'python'

	joined = os.path.join(firstPart, secondPart)
	print(joined)
	
if __name__ == '__main__':
	main()
