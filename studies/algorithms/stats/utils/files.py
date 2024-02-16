import logging
import json

log = logging.getLogger()


def read_data_file(file_name: str) -> list:
    try:
        with open(file_name) as f:
            log.debug(f'Reading {file_name}.')
            return json.load(f)
    except (FileNotFoundError, IOError) as e:
        log.debug(f'File operation failed:\n{e}', exc_info=True)