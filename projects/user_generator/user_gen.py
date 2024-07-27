import configargparse
import json
import logging


parser = configargparse.get_argument_parser(
    default_config_files=['defaults.ini'],
    description='Command line arguments for user generator',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('--log-level', type=str, required=False, default='INFO',
                    help='The logging level of the application')

cfg = parser.parse_known_args()[0]


logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.getLevelName(cfg.log_level.upper()))
log = logging.getLogger(__name__)

log.debug(f'Configuration: {json.dumps(vars(cfg), indent=4)}')


if __name__ == '__main__':
    log.info('This is just a test')
    log.debug('This is another test')
