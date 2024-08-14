import os

import configargparse
import dotenv


dotenv.load_dotenv()

parser = configargparse.get_argument_parser(
    description='Github API configuration',
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
    '-t',
    '--token',
    type=str,
    required=False,
    env_var='GIT_TOKEN',
    default=os.environ['GIT_TOKEN'],
    help='Github API token.',
)

parser.add_argument(
    '-r',
    '--repository-name',
    type=str,
    required=True,
    env_var='REPO_NAME',
    default=os.environ['REPO_NAME'],
    help='The target repository name.',
)

parser.add_argument(
    '-d',
    '--dry-run',
    type=str,
    required=False,
    default='True',
    help='Determine whether this will be a dry run [True | False]',
)

cfg = parser.parse_known_args()[0]
