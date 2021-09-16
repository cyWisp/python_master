#!/usr/bin/env python
import sys

def main():

	current_users = ['rdaglio', 'ecarlsson', 'epineda', 'ralbury', 'jgonzalez']
	new_users = ['bfandino', 'lcozy', 'ralbury', 'mgalvez', 'rdaglio']

	for user_name in new_users:

		if user_name in current_users:
	
			print("the username {} is already being used...".format(str(user_name)))

		else:

			print("the username {} is available...".format(str(user_name)))
	

if __name__ == '__main__':
	main()
