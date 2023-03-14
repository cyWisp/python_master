import logging
import os
import sys


class SystemLogFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, 'id'):
            record.id = 'N/A'

        return True


class Logger:
    log_levels = {
        '50': 'CRITICAL',
        '40': 'ERROR',
        '30': 'WARNING',
        '20': 'INFO',
        '10': 'DEBUG'
    }

    def __init__(
            self,
            name: str = 'default',
            log_level: str = 'INFO',
            log_to_stdout: bool = True,
            log_to_file: bool = False,
            file_mode: str = 'a+',
            log_file_name: str = 'app.log',
            log_file_path: str = 'logs',
            log_format: str = '%(process)d - %(asctime)s - %(funcName)s - '
                              '%(levelname)s - %(id)s: %(message)s',
            date_format: str = '%m-%d-%Y-%H:%M:%S',
    ):
        self.name = name
        self.log_level = log_level
        self.log_to_stdout = log_to_stdout
        self.log_to_file = log_to_file
        self.file_mode = file_mode
        self.log_file_name = log_file_name
        self.log_file_path = log_file_path
        self.log_format = log_format
        self.date_format = date_format

        self.logger = None
        self.valid_log_level = True

        self.create_log_dir_if_not_exists()
        self.validate_log_level()
        self.initialize_logger()
        self.configure_handlers()

    def get_logger(self):
        return self.logger

    def create_log_dir_if_not_exists(self):
        if not os.path.exists(self.log_file_path):
            if self.log_to_file:
                os.makedirs(self.log_file_path)

    def validate_log_level(self):
        if self.log_level not in self.log_levels.keys() and \
                self.log_level.upper() not in self.log_levels.values():
            logging.error('Invalid log level provided. Exiting...')
            sys.exit(1)
        else:
            if self.log_level.isnumeric():
                self.log_level = self.log_levels[self.log_level]
            else:
                self.log_level = self.log_level.upper()

    def initialize_logger(self):
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(self.log_level)

    def configure_handlers(self):
        if not self.logger.handlers:
            if self.log_to_file:
                file_handler = logging.FileHandler(os.path.join(self.log_file_path, self.log_file_name),
                                                   self.file_mode, 'utf-8')

                file_handler.setFormatter(logging.Formatter(self.log_format))
                self.logger.addHandler(file_handler)

            if self.log_to_stdout:
                stream_handler = logging.StreamHandler(sys.stdout)
                stream_handler.setFormatter(logging.Formatter(self.log_format, self.date_format))
                self.logger.addHandler(stream_handler)

        for handler in self.logger.handlers:
            handler.addFilter(SystemLogFilter())
