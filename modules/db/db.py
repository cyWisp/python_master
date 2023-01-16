#!/usr/bin/env python
import sqlite3
import logging
import sys
from sqlite3 import Error
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
          verse_image TEXT
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

    def insert_record(self, record_id, verse_reference, verse_text, verse_image_path):
        log.debug(f'Inserting new record: {record_id} | {verse_reference} | {verse_text} | {verse_image_path}')

        new_record = (record_id, verse_reference, verse_text, verse_image_path)
        query = "INSERT INTO daily_verse (id, verse_ref, verse_text, verse_image) values (?, ?, ?, ?);"

        try:
            self.db_cursor.execute(query, new_record)
            self.connection.commit()

            log.debug('Inserted record successfully!')
        except Error as e:
            log.error(f'Unable to insert record:\n{e}')
            sys.exit()

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
        (5, 'test ref5', 'test text5', 'test image5'),
        (6, 'test ref6', 'test text6', 'test image6'),
        (7, 'test ref7', 'test text7', 'test image7')
    ]

    for r in new_records:
        new_db.insert_record(r[0], r[1], r[2], r[3])

    # new_db.insert_record(4, 'test ref4', 'test text4', 'test image4')

    all = new_db.get_all_records()

    log.debug(all)

    new_db.disconnect()