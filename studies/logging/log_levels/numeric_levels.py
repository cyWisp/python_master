#!/usr/bin/env python
import logging
import configargparse

parser = configargparse.get_argument_parser(
    name='default'
)

parser.add_argument('--log-level', type=str, default='INFO')
cfg = parser.parse_known_args()[0]



logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.getLevelName(int(cfg.log_level)),
    handlers=[logging.StreamHandler()]
)

log = logging.getLogger()

if __name__ == '__main__':
    log.info('This is in info')
    log.debug('This is debug')