#!/usr/bin/env python
import configargparse
import logging
import json

parser = configargparse.get_argument_parser(
    default_config_files=['defaults.ini'],
    name='default',
    description='default argument parser',
    formatter_class=configargparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument('-un', '--user-name', env_var='USER_NAME', type=str, required=False,
                    default='Rob', help='The user\'s name.')
parser.add_argument('-ll', '--log-level', env_var='LOG_LEVEL', type=str, required=False,
                    default='INFO', help='Log level.')
parser.add_argument('-lf', '--log-file', env_var='LOG_FILE', type=str, required=False,
                    default='app.log', help='Log file name.')


cfg = parser.parse_known_args()[0]

class SystemLogFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, 'id'):
            record.id = 'N/A'

        return True

def configure_logging(log_file: str, log_level: str) -> logging.Logger:
    logging.basicConfig(
        format='%(process)d - %(asctime)s - %(levelname)s - %(id)s: %(message)s',
        level=logging.getLevelName(log_level.upper()),
        datefmt='%m-%d-%Y %H:%M:%S',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_file, 'a+', 'utf-8')
        ]
    )

    system_log = logging.getLogger()

    for handler in system_log.handlers:
        handler.addFilter(SystemLogFilter())

    return system_log

log = configure_logging(cfg.log_file, cfg.log_level)
log.debug(json.dumps(vars(cfg), indent=4))

if __name__ == '__main__':
    log.info('This is a test.', extra={'id': 'some id'})