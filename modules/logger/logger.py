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
        'CRITICAL': '50',
        'ERROR': '40',
        'WARNING': '30',
        'INFO': '20',
        'DEBUG': '10'
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

        self.create_log_dir_if_not_exists()
        self.verify_log_level()

    def create_log_dir_if_not_exists(self):
        if not os.path.exists(self.log_file_path):
            if self.log_to_file:
                os.makedirs(self.log_file_path)

    def verify_log_level(self):
        try:
            if self.log_level.isalpha():
                if self.log_level not in self.log_levels.keys():
                    self.log_level = 'INFO'

            if self.log_level.isnumeric():
                if self.log_level not in self.log_levels.values():
                    self.log_level = 'INFO'
                else:
                    self.log_level = logging.getLevelName(int(self.log_level))

        except Exception as e:
            logging.error(f'Error setting log level: {e}')

    def get_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(self.log_level)

        if not logger.handlers:
            if self.log_to_file:
                file_handler = logging.FileHandler(os.path.join(self.log_file_path, self.log_file_name),
                                                   self.file_mode, 'utf-8')

                file_handler.setFormatter(logging.Formatter(self.log_format))
                logger.addHandler(file_handler)

            if self.log_to_stdout:
                stream_handler = logging.StreamHandler(sys.stdout)
                stream_handler.setFormatter(logging.Formatter(self.log_format, self.date_format))
                logger.addHandler(stream_handler)

        for handler in logger.handlers:
            handler.addFilter(SystemLogFilter())

        return logger
