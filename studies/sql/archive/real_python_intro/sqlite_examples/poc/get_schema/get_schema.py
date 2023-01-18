#!python
import sqlite3
from sqlite3 import Error

CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        nationality TEXT
    );
"""
PRINT_SCHEMA = """
    SELECT sql FROM sqlite_master WHERE TYPE = 'table';
"""

def create_connection(path):
    db_conn = None
    try: db_conn = sqlite3.connect(path)
    except Error as e: print(f"[x] Error: {e}")
    else:
        print("[+] Connection successful!")
        return db_conn

def execute_query(db_conn, query):
    global cursor
    cursor = db_conn.cursor()
    try:
        cursor.execute(query)
        db_conn.commit()
    except Error as e: print(f"[x] Error: {e}")
    else: print("[+] Query executed successfully!")
        
def get_schema():
    schema = cursor.fetchall()
    for item in schema:
        print("\n".join(item))

if __name__ == '__main__':
    db_conn = create_connection(".\\test.db")
    execute_query(db_conn, CREATE_TABLE)
    execute_query(db_conn, PRINT_SCHEMA)
    get_schema()
    
    db_conn.close()
