#!/usr/bin/env python
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
	connection = None

	try:
		connection = mysql.connector.connect(
			host=host_name,
			user=user_name,
			passwd=user_password
		)
	except Error as e: print(f"[x] Error: {e.__class__.__name__}: {e}")
	else:
		print("[*] Connection successful!")
		return connection

if __name__ == '__main__':
	connection = create_connection('<host>', '<user>', '<password>')
	connection.close()
	
