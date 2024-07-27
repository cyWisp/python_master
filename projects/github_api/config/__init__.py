import configargparse


parser = configargparse.get_argument_parser(
    description='Github API configuration',
    default_config_files=['config/defaults.ini'],
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('--default-config', is_config_file=True, default='config/defaults.ini',
                    help='The default config file')

parser.add_argument('-l', '--log-level', type=str, required=False, default='info',
                    help='The application logging level.')

parser.add_argument('-f', '--log-file', type=str, required=False, default='logs/app.log',
                    help='The log file path.')

parser.add_argument('-t', '--token', type=str, required=False, env_var='GIT_TOKEN',
                    help='Github API token.')

cfg = parser.parse_known_args()[0]
