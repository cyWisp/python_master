import configargparse

parser = configargparse.get_argument_parser(
    name='default',
    description='Just a test',
    default_config_files=['config/defaults.ini'],
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('--log-level', type=str, required=False,
                    default='INFO', help='Logging level for application run time.')

parser.add_argument('--log-file', type=str, required=False,
                    default='logs/app.log', help='The log file path.')

