#!/usr/bin/env python
import os

if __name__ == '__main__':

	with open('./test', 'r+') as input_file:
		text = list(input_file.read())
	input_file.close()

	stripped = [x for x in text]
	str_var = ''.join(stripped)

	print(str_var)
	
