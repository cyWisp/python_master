import logging
import psycopg2
import json

from enum import Enum
from psycopg2 import OperationalError


logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


class Queries(Enum):
    create_simple_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        location TEXT
    )
    '''


class PsyDB:
    def __init__(self, **kwargs):
        self.db = kwargs.get('db')
        self.user = kwargs.get('user')
        self.pw = kwargs.get('pw')
        self.host = kwargs.get('host')
        self.port = kwargs.get('port')

        self.connection, self.cursor = None, None

    def __str__(self):
        return self.__dict__

    def __enter__(self):
        try:
            log.info(f'Connecting to {self.db} on {self.host}:{self.port}')

            self.connection = psycopg2.connect(
                database=self.db,
                user=self.user,
                password=self.pw,
                host=self.host,
                port=self.port
            )

            log.info('Connection succeeded.')

            return self
        except OperationalError as e:
            log.error(f'Connection failed:\n{e}')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        try:
            log.info('Closing database connection.')
            self.connection.close()

        except OperationalError as e:
            log.error(f'Unable to close connection.')

    def execute_query(self, query):
        if self.connection:
            if not self.connection.autocommit:
                self.connection.autocommit = True

            try:
                if not self.cursor:
                    self.cursor = self.connection.cursor()

                log.info(f'Executing: {query}')
                self.cursor.execute(query)

            except OperationalError as e:
                log.error(f'Query failed:\n{e}')



if __name__ == '__main__':
    # db_object = PsyDB(
    #     db='ddb_user',
    #     user='ddb_user',
    #     pw='ADMINforJUSTICE1220!',
    #     host='10.0.0.4',
    #     port=5432
    # )
    #
    # log.info(json.dumps(db_object.__str__(), indent=4))

    with PsyDB(
        db='ddb_user',
        user='ddb_user',
        pw='ADMINforJUSTICE1220!',
        host='10.0.0.4',
        port=5432
    ) as pdb:
        pdb.execute_query(Queries.create_simple_table.value)


