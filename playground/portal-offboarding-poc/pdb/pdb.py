import logging
import psycopg2
import sys

from psycopg2 import OperationalError, Error


log = logging.getLogger()


class PDB:
    RETRIES = 3

    def __init__(self, db_name: str, db_user: str,db_pass: str,
                db_host: str, db_port: int) -> None:

        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_host = db_host
        self.db_port = db_port

        self.connection, self.cursor = None, None
        self._connect()

    def _connect(self):
        for r in range(self.RETRIES):
            if not self.connection:
                try:
                    log.debug(f'Connecting to database. Attempt {r + 1}')

                    self.connection = psycopg2.connect(
                        database=self.db_name,
                        user=self.db_user,
                        password=self.db_pass,
                        host=self.db_host,
                        port=self.db_port
                    )
                    self.connection.autocommit = True

                    log.debug('Connection successful.')

                    if r == self.RETRIES - 1:
                        raise OperationalError

                except OperationalError as e:
                    log.error(f'Unable to connect to database:\n{e}')
                    sys.exit()

    def _check_connection(self):
        if not self.connection:
            self._connect()

        if not self.cursor:
            self.cursor = self.connection.cursor()

    def run_query(self, query: str):
        try:
            log.debug(f'Running {query}')

            self._check_connection()
            self.cursor.execute(query)

            log.debug(f'Execution successful.')

        except (OperationalError, Error):
            raise

    # Returns a list of tuples
    def read(self, query: str, limit=None) -> list:

        try:
            log.debug('Querying the target database.')
            self._check_connection()

            if limit:
                query = query.replace(';', ' ') + f'LIMIT {str(limit)};'

            log.debug(f'Executing {query}')
            self.cursor.execute(query)

            query_result = self.cursor.fetchall()

            if not query_result:
                raise ValueError('Query returned no results.')

            return query_result

        except (OperationalError, Error) as e:
            log.error(f'Query failed: \n{e}', exc_info=True)

        except ValueError as e:
            log.error(e)

    def __str__(self):
        return vars(self)

    def __enter__(self):
        self._connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            try:
                log.debug(f'Closing connection to {self.db_name}.')
                self.connection.close()

            except (OperationalError, Error) as e:
                log.error(e, exc_info=True)




