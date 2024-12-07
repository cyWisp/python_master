import os

import configargparse
import dotenv


dotenv.load_dotenv('.env.local')

parser = configargparse.get_argument_parser(
    description='Portal Offboarding Configuration',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter,
)

parser.add_argument(
    '-l',
    '--log-level',
    type=str,
    required=False,
    env_var='LOG_LEVEL',
    default=os.environ['LOG_LEVEL'],
    help='The application logging level.',
)

parser.add_argument(
    '-u',
    '--db-user',
    type=str,
    required=True,
    env_var='DB_USERNAME',
    default=os.environ['DB_USERNAME'],
    help='Database username.',
)

parser.add_argument(
    '-d',
    '--db-name',
    type=str,
    required=True,
    env_var='DB_NAME',
    default=os.environ['DB_NAME'],
    help='Database name.',
)

parser.add_argument(
    '-p',
    '--db-pass',
    type=str,
    required=True,
    env_var='DB_PASSWORD',
    default=os.environ['DB_PASSWORD'],
    help='Database password',
)

parser.add_argument(
    '-h',
    '--db-host',
    type=str,
    required=False,
    env_var='DB_HOSTNAME',
    default=os.environ['DB_HOSTNAME'],
    help='Database hostname.',
)

parser.add_argument(
    '-dP',
    '--db-port',
    type=int,
    required=False,
    env_var='DB_PORT',
    default=os.environ['DB_PORT'],
    help='Database port.',
)

parser.add_argument(
    '-g',
    '--data-access-group',
    type=str,
    required=True,
    help='Data access group.',
)


cfg = parser.parse_known_args()[0]
