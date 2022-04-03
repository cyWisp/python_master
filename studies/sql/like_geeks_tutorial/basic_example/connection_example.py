#!/usr/bin/env python
import os, sqlite3, sys

if __name__ == '__main__':

	# Create a connection to the database
	# connection = sqlite3.connect('example.db')

	# Create a cursor object (method of the connection object)
	# cursor_object = connection.cursor()

	# Using error checking, attempt to connect to the database
	# and throw an error if unable to do so


	try:
		if os.path.exists('./example.db'):
			print("[*] Database exists- now connecting...")
			conn = sqlite3.connect('./example.db')
		else:
			while True():
				create_db = str(input("[?] Database './example.db' does not exist- create it? y or n"))
				if create_db == 'y':
					conn = sqlite3.connect('./example.db')
					break
				elif create_db == 'n':
					print("[!] Now exiting the application...")
					sys.exit(0)
	except:
		print("[x] Something went wrong...")
	finally:
		print("[*] Connection made successfully- now closing...")
	

	conn.close()			
	
	
	
