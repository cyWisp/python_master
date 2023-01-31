#!/usr/bin/env python
import sqlite3
import logging
import sys
from sqlite3 import Error, IntegrityError
from enum import Enum

logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.DEBUG
)

log = logging.getLogger()


class Queries(Enum):
    CREATE_TABLE = '''
        CREATE TABLE IF NOT EXISTS daily_verse (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          verse_ref TEXT NOT NULL,
          verse_text TEXT,
          UNIQUE(verse_ref, verse_text)
        );
    '''

    SELECT_ALL = 'SELECT * FROM daily_verse'


class DB:
    def __init__(self, db_path: str = None) -> None:
        self.db_path = db_path
        self.connection = None
        self.db_cursor = None

        self.connect()

    def connect(self):
        log.debug(f'Connecting to {self.db_path}')

        try:
            self.connection = sqlite3.connect(self.db_path)
            log.debug('Connection succeeded!')
        except Error as e:
            log.error(f'Could not connect to database:\n{e}')
            sys.exit()

    def execute_query(self, query):
        log.debug(f'Executing: {query}.')

        try:
            if not self.db_cursor:
                self.db_cursor = self.connection.cursor()

            self.db_cursor.execute(query)
            self.connection.commit()
            log.debug('Query ran successfully.')
        except Error as e:
            log.error(f'Query failed to execute:\n{e}')

    def insert_record(self, record):
        log.debug(f'Inserting new record: {record[0]} | {record[1]}')
        query = f"INSERT INTO daily_verse (verse_ref, verse_text) values (?, ?);"

        try:
            self.db_cursor.execute(query, (record[0], record[1]))
            self.connection.commit()

            log.debug('Inserted record successfully!')
        except IntegrityError as e:
            log.debug(f'Value already exists: {e}')
        except Exception as e:
            log.exception(f'Unable to insert record:\n{e} | {e.__class__.__name__}')


    def get_all_records(self):
        log.debug('Retrieving all records.')

        try:
            self.db_cursor.execute(Queries.SELECT_ALL.value)
            result = self.db_cursor.fetchall()

            log.debug('Success!')
            return result
        except Error as e:
            log.error(f'Unable to retrieve records:\n{e}')
            sys.exit()


    def disconnect(self):
        log.debug(f'Disconnecting from {self.db_path}.')

        try:
            self.connection.close()
            log.debug('Connection closed successfully.')
        except Error as e:
            log.error(f'Something went wrong:\n{e}')
            sys.exit()

if __name__ == '__main__':
    log.debug('Starting.')
    new_db = DB(db_path='/mnt/l/repos/python_master/modules/db/verses.sqlite')
    new_db.execute_query(Queries.CREATE_TABLE.value)

    new_records = [
        ('test ref1', 'test text1'),
        ('test ref2', 'test text2'),
        ('test ref3', 'test text3'),
        ('test ref4', 'test text4'),
        ('test ref5', 'test text5')
    ]

    for r in new_records:
        new_db.insert_record(r)

    # new_db.insert_record(4, 'test ref4', 'test text4', 'test image4')

    all = new_db.get_all_records()

    log.debug(all)

    new_db.disconnect()