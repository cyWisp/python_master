#!/usr/bin/env python
from sys import argv, exit
import mysql.connector
from mysql.connector import Error

def usage():
	print(f"Usage: python {argv[0]} <host> <user> <password>")
	exit(0)

def validate():
	if len(argv) != 4:
		usage()
	else: pass

def create_connection(host_name, user_name, user_password):
	connection = None
	try:
		connection = mysql.connector.connect(
			host=host_name,
			user=user_name,
			passwd=user_password,
		)
	except Error as e: print(f"[x] MySQL Error: {e}")
	else:
		print("[+] Connection successful!")
		return connection

if __name__ == '__main__':
	validate()
	connection = create_connection(argv[1], argv[2], argv[3])

