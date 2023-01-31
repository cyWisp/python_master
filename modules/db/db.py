#!/usr/bin/env python
import sqlite3
import logging
import sys
from sqlite3 import Error, IntegrityError
import json
from sqlite3 import Error
from enum import Enum

logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.DEBUG
)

log = logging.getLogger()

def read_verses_json():
    log.debug('Reading json file.')
    try:
        with open('verses.json', 'r') as  f:
            return json.load(f)
    except Exception as e:
        log.debug(f'Could not read json file:\n{e}')
        sys.exit()



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

    def insert_record(self, verse_reference, verse_text):
        log.debug(f'Inserting new record: {verse_reference} | {verse_text}')

        new_record = (verse_reference, verse_text)
        query = """
            INSERT INTO daily_verse (verse_ref, verse_text) values (?, ?);
        """

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


def read_books():
    log.debug('Reading books file.')

    try:
        with open('books.json') as f:
            content = json.load(f)
            return content
    except Exception as e:
        log.error(f'Something went wrong:\n{e}')



def clean_data(records):
    log.debug('Cleaning data')
    cleaned_records = list()
    books = read_books()

    for r in records:
        verse_reference = r[1].split('>')[1].split('<')[0] \
                if '<' in r[1] and '>' in r[1] else r[1]

        if verse_reference.split(' ')[0] in books \
            or verse_reference.split(' ')[:2] in books:

            if 'in' in verse_reference:
                cleaned_records.append((' '.join(verse_reference.split(' ')[:-1]), r[2].lstrip(' ')))
            else:
                cleaned_records.append((verse_reference, r[2].lstrip(' ').lstrip('\t')))
        else:
            continue

    return cleaned_records



if __name__ == '__main__':
    verses = read_verses_json()

    log.debug('Creating and Connecting to DB')
    new_db = DB(db_path='verses.db')
    new_db.execute_query(Queries.CREATE_TABLE.value)


    new_records = [[index + 1, k, v] for index, (k, v) in enumerate(verses.items())]

    cleaned_records = clean_data(new_records)


    for r in cleaned_records:
        log.debug(f'{r[0]} | {r[1]}')
        new_db.insert_record(r[0], r[1])

    # new_db.insert_record('test ref4', 'test text4')
    #
    # all_records = new_db.get_all_records()
    #
    # log.debug(all_records)

    new_db.disconnect()


    # for index, (k, v) in enumerate(verses.items()):
    #     log.debug(f'{index + 1}: {k}: {v}')