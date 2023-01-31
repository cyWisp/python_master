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
    CREATE_TABLE = """
        CREATE TABLE IF NOT EXISTS random_data (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          chain_name TEXT NOT NULL,
          location TEXT,
          total_sales TEXT,
          total_waste TEXT,
          total_units_sold,
          UNIQUE(chain_name)
        );
    """

    SELECT_ALL = "SELECT * FROM random_data"
    INSERT_RECORD = """
        INSERT INTO random_data (
            chain_name,
            location,
            total_sales,
            total_waste,
            total_units_sold
        ) values (?, ?, ?, ?, ?);
    """

class QDB:
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
        log.debug(f'Inserting new record: {record[0]} | {record[1]} | {record[2]} | {record[3]} | {record[4]}')

        try:
            self.db_cursor.execute(Queries.INSERT_RECORD.value, record)
            self.connection.commit()

            log.debug('Inserted record successfully!')
        except IntegrityError as e:
            log.debug(f'Value already exists: {e}')
        except Exception as e:
            log.exception(f'Unable to insert record:\n{e} | {e.__class__.__name__}')

    def get_column_names(self):
        return list(map(lambda x: x[0], self.db_cursor.description))

    def get_all_records(self):
        log.debug('Retrieving all records.')

        try:
            if not self.db_cursor:
                self.db_cursor = self.connection.cursor()

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
    new_db = QDB(db_path='random_data.db')
    new_db.execute_query(Queries.CREATE_TABLE.value)

    new_records = [
        ("Some Chain", "Miami, FL", "$120000", "2323", "12445"),
        ("Another Chain", "Orlando, FL", "$125500", "454566", "13545"),
        ("My Chain", "Los Anegles, CA", "$12454500", "555", "13545"),
        ("Your Chain", "Atalanta, GA", "$145450", "111323", "12545"),
        ("Goin Bananas", "Mars", "$1245454", "233434", "12435"),
        ("Sam I am", "Venus", "$120", "2323", "1243"),
        ("More chain", "China", "$34340", "233434", "1244564645"),
        ("off the chain", "Italy", "$1344433", "22233", "124345"),
        ("Chain gang", "Something else", "$14", "555", "1243343"),
        ("Chained together", "Broward", "$3463463", "23", "12435443"),
        ("Ball and Chain", "yeah", "$15555", "4343", "4445"),
        ("Restaurant A", "Something", "$222233", "1", "1234345"),
        ("Seymour Butts", "Something else", "$12034", "12", "12676745")
]
    #
    # for r in new_records:
    #     new_db.insert_record(r)

    all_records = new_db.get_all_records()
    col_names = new_db.get_column_names()

    log.debug(col_names)
    log.debug(all_records)

    new_db.disconnect()