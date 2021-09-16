#!/usr/bin/env python
import sqlite3, os
from sqlite3 import Error

class TestDB:
	queries = {
		"create_table": """
			CREATE TABLE IF NOT EXISTS users (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT NOT NULL,
				age INTEGER,
				gender TEXT,
				nationality TEXT
			);
		"""
	}
	def __init__(self, path):
		self.path = path
		self.db_conn = None

	def close_connection(self):
		print("[+] Closing database...")
		self.db_conn.close()

	def check_path(self):
		if os.path.exists(self.path): print("[+] Database exists...")
		else: print("[+] Database does not exist- creating...")

	def create_connection(self):
		try: self.db_conn = sqlite3.connect(self.path)
		except Error as e: print(f"[x] Error: {e}")
		else: print("[+] Connection successful!")

	def execute_query(self, query):
		cursor = self.db_conn.cursor()
		try:
			cursor.execute(query)
			self.db_conn.commit()
		except Error as e: print(f"[x] Error: {e}")
		else: print("[+] Query executed successfully!")

if __name__ == '__main__':

	new_db = TestDB("./test.db")
	new_db.check_path()
	new_db.create_connection()
	
	new_db.execute_query(new_db.queries['create_table'])

	new_db.close_connection()
	
