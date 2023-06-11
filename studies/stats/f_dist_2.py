#!/usr/bin/env python
import logging, json
import configargparse

parser = configargparse.get_argument_parser(name='default')
parser.add_argument('-f', '--file', type=str, required=False,
                    default='stats.json', help='The file to analyze.')
parser.add_argument('-w', '--class-width', type=int, required=False,
                    default=15, help='Class width.')
parser.add_argument('-c', '--num-classes', type=int, required=False,
                    default=6, help='Number of classes.')
parser.add_argument('-u', '--upper-limit', type=int, required=False,
                    default=70, help='Upper limit.')
parser.add_argument('-l', '--lower-limit', type=int, required=False,
                    default=0, help='Lower limit.')

cfg = parser.parse_known_args()[0]

logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.DEBUG
)
log = logging.getLogger()


def get_file_content(stats_file: str) -> list | tuple:
    try:
        with open(stats_file, 'r') as f:
            content = json.load(f)
        return content, len(content)
    except Exception as e:
        log.exception(e)

def create_classes():
    count = 0
    limits = dict()
    while True:
        if count >= cfg.upper_limit:
            break
        if



if __name__ == '__main__':
    values, num_values = get_file_content(cfg.file)

    log.debug(f'{values} | {num_values}')


