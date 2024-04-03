import configargparse


parser = configargparse.get_argument_parser(
    description='Default argument parser',
    default_config_files=['config/defaults.ini'],
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('-l', '--log-level', type=str, required=False, default='INFO',
                    help='The logging level for the application <info, debug, warning, critical, error>')

parser.add_argument('-lf', '--log-file', type=str, required=False, default='logs/app.log',
                    help='The log file path.')

