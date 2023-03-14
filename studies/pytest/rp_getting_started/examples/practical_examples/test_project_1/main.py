import json
from config import parser
from logger.logger import Logger


cfg = parser.parse_known_args()[0]
log = Logger(
    log_file_name=cfg.log_file.split('/')[-1],
    log_file_path=cfg.log_file.split('/')[0],
    log_level=cfg.log_level,
    log_to_file=True
).get_logger()


def get_version():
    try:
        with open('version.properties') as f:
            return f.read().split('=')[-1]
    except IOError as e:
        log.error(f'Unable to read version properties file:\n{e}')


if __name__ == '__main__':
    log.info(f'Version: {get_version()}')
    log.info(f'Configuration: {json.dumps(vars(cfg), indent=4)}')

    log.info('Test.')
