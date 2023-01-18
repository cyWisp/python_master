#!/usr/bin/env python
import sqlite3
from sqlite3 import Error

def create_connection(path):
	connection = None
	try:
		connection = sqlite3.connect(path)
	except Error as e: print(f"[x] Error: {e}")
	else:
		print("[+] Connection successful!")
		return connection

if __name__ == '__main__':
	db_conn = create_connection("./test.db")

