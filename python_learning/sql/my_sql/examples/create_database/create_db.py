#!/usr/bin/env python
import mysql.connector
from mysql.connector import Error

HOST = '10.0.0.4'
USER = 'wisp'
PASSWD = ''

def connect(host="", user="", passwd=""):
	connection = None
	try:
		connection = mysql.connector.connect(
			host=host,
			user=user,
			passwd=passwd
		)
	except Error as e:
		print(f"[x] Error: {e.__class__.__name__}: {e}")
	else:
		print(f"[*] Connection to {host} as {user} successful...")
		return connection

def create_database(connection, query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
	except Error as e: print(f"[x] Error: {e.__class__.__name__}: {e}")
	else:
		print("Database created successfully!")

if __name__ == '__main__':
	connection = connect(HOST, USER, PASSWD)

	create_database_query = "CREATE DATABASE IF NOT EXISTS test;"
	create_database(connection, create_database_query)


	
