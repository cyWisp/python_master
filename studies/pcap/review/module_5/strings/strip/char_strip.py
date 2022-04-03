#!/usr/bin/env python
from sys import argv


def import_file(file_name):
	try:
		with open(file_name, 'r+') as input_file:
			str_message = "".join(input_file.readlines())
	except:
		print("Unable to read file")
	else:
		return str_message
	finally:
		input_file.close()

def delete_quotes(string_var):

	p = ["\'", "\"", ".", ","]

	no_punc = [x for x in string_var if x not in p]
	print("".join(no_punc))

if __name__ == '__main__':

	read_file = import_file(argv[1])
	delete_quotes(read_file)
	
