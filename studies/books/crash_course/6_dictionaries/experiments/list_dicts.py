#!/usr/bin/env python
import os

def main():

	dict_1 = {'Name':'Rob','Age':'32'}
	dict_2 = {'Name':'Evert','Age':'32'}

	listDict = [dict_1, dict_2]

	for dictionary in listDict:
		for key, value in dictionary.items():
			print('{}: {}'.format(key, value))
	

if __name__ == '__main__':
	main()
