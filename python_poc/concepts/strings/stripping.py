#!/usr/bin/env python
import os, sys

def main():

	wordToStrip = "//this is a string with slashes"
	print("This is the string with slashes: {}".format(wordToStrip))	

	wordToStrip = wordToStrip.lstrip('/')
	print("This is the string without slashes: {}".format(wordToStrip))


if __name__ == '__main__':
	main()
