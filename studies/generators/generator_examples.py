#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger()


def read_file(file_name: str):
    with open(file_name) as f:
        for i in f.readlines():
            yield i.replace('\n', '')


if __name__ == '__main__':
    file_content = read_file('techcrunch.csv')
    row_count = 0

    log.info(f'Type: {type(file_content)}')
    for i in file_content:
        row_count += 1

    log.info(f'Row count: {row_count}')
