import configargparse

parser = configargparse.get_argument_parser(
    name='default',
    default_config_files=['config/defaults.ini'],
    description='Default configuration for dynamic table.',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('--log-level', type=str, required=False, env_var='LOG_LEVEL',
                    default='INFO', help='The logging level of the application.')

parser.add_argument('--log-file', type=str, required=False, env_var='LOG_FILE',
                    default='logs/app.log', help='The log file path.')

parser.add_argument('--headers-file', type=str, required=True, default='data/headers.json',
                    help='Table headers file path.')

parser.add_argument('--values-file', type=str, required=True, default='data/values.json',
                    help='Data values file path.')
