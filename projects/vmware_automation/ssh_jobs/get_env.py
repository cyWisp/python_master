#!/usr/bin/env python
from os import environ

if __name__ == '__main__':

#	for k, v in environ.items():
#		print(f"{k}: {v}")

	print(environ['VM_USER'])
