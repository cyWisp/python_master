#!/usr/bin/env python
import logging
import sqlite3
from sqlite3 import Error
from enum import Enum

class Queries(Enum):
    CREATE_TABLE = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        location TEXT
    );
    '''


logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.DEBUG
)

log = logging.getLogger()


class DB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = self.db_connect()
        self.cursor = None

    def db_connect(self):
        log.debug(f'Connecting to {self.db_path}')

        try:
            conn = sqlite3.connect(self.db_path)
            log.debug('Connection successful!')

            return conn
        except Error as e:
            log.error(e)

    def execute_query(self, query: str) -> None:
        self.cursor = self.connection.cursor()
        log.debug(f'Executing: {query}')

        try:
            self.cursor.execute(query)
            self.connection.commit()

            log.debug('Query executed successfully!')
        except Error as e:
            log.error(e)



if __name__ == '__main__':
    new_db = DB('test.db')
    new_db.execute_query(Queries.CREATE_TABLE.value)
