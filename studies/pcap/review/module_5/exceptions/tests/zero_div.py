#!/usr/bin/env python
from sys import exit, argv

if __name__ == '__main__':

	try:
		assert len(argv) == 3
		print(int(argv[1]) / int(argv[2]))
	except AssertionError:
		print("Please provide two arguments...")
	except ZeroDivisionError:
		print("You cannot divide by zero...")
	except IndexError:
		print("Not enough arguments")
	except ValueError:
		print("Please provide integers to divide")
	else:
		exit(0)


