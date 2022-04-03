#!/usr/bin/env python
import mysql.connector
from mysql.connector import Error

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
	connection = create_connection(
		"192.168.251.138",
		'wisp',
		'ADMINforJUSTICE1220!',
	)

	print("[+] Done...")


