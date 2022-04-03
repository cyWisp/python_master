#!/usr/bin/env python
from os import mkdir
from sys import argv

if __name__ == '__main__':

	mkdir(argv[1])
	mkdir(f"{argv[1]}/{argv[1]}_second_level")
