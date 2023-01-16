#!/usr/bin/env python
import mysql.connector
from mysql.connector import Error
from getpass import getpass

HOST = '10.0.0.4'
USER = input("User: ")
PASS = getpass("Password: ")

DB_NAME = "verses"
QUERIES = {
    "create_db": "CREATE DATABASE IF NOT EXISTS verses",
    "create_daily_verse_table": """
        CREATE TABLE IF NOT EXISTS daily_verse(
            id INT AUTO_INCREMENT,
            reference TEXT NOT NULL,
            verse TEXT,
            PRIMARY KEY (id)
        ) ENGINE = InnoDB
    """
}

# Connect to server
def connect(host, user, passwd):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )
    except Error as e:
        print("Error: {e.__class__.__name__}: {e}")
    else:
        print(f"[*] Connection to {host} as {user} succeeded!")
        return connection

# Connect to database
def connect_db(host, user, passwd, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=db_name
        )
    except Error as e:
        print("Error: {e.__class__.__name__}: {e}")
    else:
        print(f"[*] Connection to {db_name} on {host} succeeded!")
        return connection

# Execute query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print("Error: {e.__class__.__name__}: {e}")
    else:
        print("[*] Query executed successfully!")

# Create the database if it doesn't exist
def initial_setup():
    connection = connect(HOST, USER, PASS)
    execute_query(connection, QUERIES['create_db'])
    connection.close()

# Connect to the database 
def main():
    initial_setup()
    db_connection = connect_db(HOST, USER, PASS, DB_NAME)
    execute_query(db_connection, QUERIES['create_daily_verse_table'])
    
    db_connection.close()

if __name__ == '__main__':
    main()


