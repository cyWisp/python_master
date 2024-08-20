import configargparse
import logging

parser = configargparse.get_argument_parser(
    description='Just a test'
)

parser.add_argument('-l', '--log-level', type=str, required=False, default='info',)
cfg = parser.parse_known_args()[0]

logging.basicConfig(format='%(message)s', level=logging.getLevelName(cfg.log_level.upper()))
log = logging.getLogger(__name__)

if __name__ == '__main__':
    log.info(f'TEST | Current log level: {cfg.log_level}')
