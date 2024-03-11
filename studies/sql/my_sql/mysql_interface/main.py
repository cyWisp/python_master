#!/usr/bin/env python
import logging
import json
import sys

from config import parser


cfg = parser.parse_known_args()[0]

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.getLevelName(cfg.log_level.upper()),
    handlers=[
        logging.FileHandler(cfg.log_file, 'a+', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

log = logging.getLogger()

log.debug(json.dumps(vars(cfg), indent=4))

if __name__ == '__main__':
    log.info('This is just a test')


