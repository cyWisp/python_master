#!/usr/bin/env python
import mysql.connector
from mysql.connector import Error

HOST = ""
USER = ""
PASSWD = ""

def create_connection(host, user, passwd):
	connection = None
	try:
		connection = mysql.connector.connect(
			host=host,
			user=user,
			passwd=passwd
		)
	except Error as e: print("[x] Error: {e.__class__.__name__}: {e}")
	else:
		print(f"[*] Connection to {host} as {user} successful!")
		return connection

if __name__ == '__main__':
	connection = create_connection(HOST, USER, PASSWD)
	print("[!] Closing connection...")
	connection.close()
	
