#!/usr/bin/env python
import mysql.connector
from mysql.connector import Error

# Connect to the server (note: user environment variables)
def server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
        )
    except Error as e: print(f"[x] Error: {e}")
    else:
        print(f"[+] Connection successful!")
        return connection

# Connect to a specific database
def db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
        )
    except Error as e: print(f"[x] Error: {e}")
    else:
        print(f"[+] Connection to {db_name} successful!")
        return connection

# Create the database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except Error as e: print(f"[x] Error: {e}")
    else: print("[+] Database created successfully...")

if __name__ == '__main__':
    # connection = server_connection(
    #     '192.168.251.138',
    #     'wisp',
    #     'ADMINforJUSTICE1220!',
    # )

    database_connection = db_connection(
        '192.168.251.138',
        'wisp',
        'ADMINforJUSTICE1220!',
        'sm_app'
    )


    # create_database_query = "CREATE DATABASE sm_app"
    # create_database(connection, create_database_query)

