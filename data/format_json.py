#!/usr/bin/env python
import json
import os
import logging
import configargparse

logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.DEBUG
)
log = logging.getLogger()

parser = configargparse.get_argument_parser(name='default')
parser.add_argument('-f', '--file', type=str, required=True,
                    help='File to convert.')
cfg = parser.parse_known_args()[0]


def read_text_file(file_name: str) -> list:
    try:
        with open(file_name, 'r') as f:
            raw = f.readlines()
            content = [float(x) for x in raw]
            log.debug(f'Raw: {len(raw)} | Content: {len(content)}')
        return content
    except Exception as e:
        log.exception(e)


def write_json_file(file_name: str, content: list | dict):
    new_file_name = '.'.join([file_name.split('.')[0], 'json'])

    try:
        with open(new_file_name, 'w') as f:
            json.dump(content, f)
    except Exception as e:
        log.exception(e)


if __name__ == '__main__':
    file_content = read_text_file(cfg.file)
    write_json_file(cfg.file, file_content)