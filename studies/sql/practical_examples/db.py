#!/usr/bin/env python
import sqlite3
import logging
import sys
from sqlite3 import Error

logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.DEBUG
)

log = logging.getLogger()

class DB:
    def __init__(self, db_path: str = None) -> None:
        self.db_path = db_path
        self.connection = None

        self.connect()

    def connect(self):
        log.debug(f'Connecting to {self.db_path}')

        try:
            self.connection = sqlite3.connect(self.db_path)
            log.debug('Connection succeeded!')
        except Error as e:
            log.error(f'Could not connect to database:\n{e}')
            sys.exit()

if __name__ == '__main__':
    log.debug('Starting.')
    new_db = DB(db_path='test.db')