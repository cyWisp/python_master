#!/usr/bin/env python
from os import strerror

if __name__ == '__main__':

	string_var = """this is a string
with multiple lines
that will be written to a file.
	"""

	try:
		with open("./output.txt", "w+") as test:
			for line in string_var:
				test.write(line)
	except IOError as e:
		print("[x] something went wrong: ", strerr(e.errno))
	finally:
		test.close()
		print("output file written!")
