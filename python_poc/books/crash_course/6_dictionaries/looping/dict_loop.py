#!/usr/bin/env python
import os

def main():

	user = {'username':'rdaglio','first_name':'Rob','last_name':'Daglio'}

	for key, value in user.items():
		print('{}: {}\n'.format(key, value))

if __name__ == '__main__':
	main()
