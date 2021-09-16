#!/usr/bin/env python
import os

def main():
	
	path = '/home/wisp/python'
	pathExists = os.path.exists(path)
	print(pathExists) #should return true

if __name__=='__main__':
	main()
