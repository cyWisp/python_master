#!/usr/bin/env python
import logging
import configargparse
import json

from utils.files import read_data_file
from stats.stats import Stats

parser = configargparse.getArgumentParser(
    description='Arguments for basic statistics program.',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter,
)

parser.add_argument('-l', '--log-level', type=str, required=False, default='info',
                    help='The logging level for the application. Default: info.')

parser.add_argument('-p', '--log-path', type=str, required=False, default='app.log',
                    help='The log path for the application. Default: app.log.')


parser.add_argument('-d', '--data', type=str, required=False, default='data.json',
                    help='The data file to be read.')

cfg = parser.parse_known_args()[0]

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.getLevelName(cfg.log_level.upper()),
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(cfg.log_path, 'a+', encoding='utf-8')
    ]
)

log = logging.getLogger()
log.debug(f'Current configuration: {json.dumps(vars(cfg), indent=4)}')


if __name__ == '__main__':
    log.info('Init')

    new_data = read_data_file(cfg.data)

    with Stats(target_data=new_data) as s:
        s.get_all_statistics()

