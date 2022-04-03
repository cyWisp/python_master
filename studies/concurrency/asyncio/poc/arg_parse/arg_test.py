#!/usr/bin/env python
import argparse

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--nprod", dest="p", type=int, default=5)
	parser.add_argument("-c", "--ncon", dest="c", type=int, default=10)
	ns = parser.parse_args()

	print(ns.p)
	
	
