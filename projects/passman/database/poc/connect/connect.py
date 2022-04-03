import sqlite3, os
from sqlite3 import Error

DB_PATH = "./test.db"

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e: print(f"Error: {e}")
    else: print("Connection successful!")

    return connection

if __name__ == '__main__':

    if not os.path.exists(DB_PATH):
        print("Database does not exist... creating it.")
        connection = create_connection("./test.db")
    else:
        print("Database exists...")