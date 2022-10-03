#!/usr/bin/env python
from logger.logger import Logger
import json
from config import parser

cfg = parser.parse_known_args()[0]

log = Logger(
    log_to_file=True,
    log_level=cfg.log_level,
    log_file_name=cfg.log_file
).get_logger()

if __name__ == '__main__':
    log.debug(f'Configuration: {json.dumps(vars(cfg), indent=4)}')

    log.info('this is an info message')

    from pack_1 import mod_1

    mod_1.func_1()