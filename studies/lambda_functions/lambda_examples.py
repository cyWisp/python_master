#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger()
log.name = 'default'


if __name__ == '__main__':

    # Basic example - add one to variable input
    # -> 3
    log.info((lambda x: x + 1)(2))

    # Could also be written as:
    # -> 3
    func_1 = lambda x: x + 1
    log.info(func_1(2))

    # Lambda function to capitalize a name
    full_name = lambda first_name, last_name: f'Full name: {first_name.title()} {last_name.title()}'
    log.info(full_name('Rob', 'Daglio'))


