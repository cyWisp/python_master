#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

if __name__ == '__main__':

    try:
        log.info('Attempting division by zero.')
        var = 3 / 0

    except ZeroDivisionError as e:
        log.error(f'Could not divide by zero:\n{e}', exc_info=True)