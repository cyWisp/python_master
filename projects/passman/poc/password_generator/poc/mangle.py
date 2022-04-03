#!/usr/bin/env python

if __name__ == '__main__':
	alpha = [chr(x) for x in range(65, 91)]
	with open('./alpha.txt', "w+") as alpha_file:
		for a in alpha:
			alpha_file.write(f"'{a}': ''," + "\n")
