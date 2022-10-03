import configargparse

parser = configargparse.get_argument_parser(
    default_config_files=['defaults.ini'],
    name='default',
    description='default argument parser',
    formatter_class=configargparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument('-ll', '--log-level', env_var='LOG_LEVEL', type=str, required=False,
                    default='INFO', help='Log level.')
parser.add_argument('-lf', '--log-file', env_var='LOG_FILE', type=str, required=False,
                    default='app.log', help='Log file name.')

