#!/usr/bin/env python
import sys, os, subprocess

def main():

	subprocess.run(["ls", "-l"]) #does not capture input

if __name__ == '__main__':
	main() 
