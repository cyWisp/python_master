#!/usr/bin/env python
import mysql.connector
from mysql.connector import Error

HOST = "10.0.0.4"
USER = "wisp"
PASSWD = ""
DB_NAME = "test"

def connect(host="", user="", passwd="", db_name=""):
	print(f"[!] Connecting to {db_name} on Host: {host}")	
	connection = None
	try:
		mysql.connector.connect(
			host=host,
			user=user,
			passwd=passwd,
			database=db_name
		)
	except Error as e: print(f"[x] Error: {e.__class__.__name__}: {e}")
	else:
		print(f"[*] Connection to {db_name} on {host} as {user} successful!")
		return connection

def execute_query(connection, query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
	except Error as e: print(f"[x] Error: {e.__class__.__name__}: {e}")
	else:
		print("[*] Query executed successfully!") 

if __name__ == '__main__':
	connection = connect(HOST, USER, PASSWD, DB_NAME)
	

