import configargparse

parser = configargparse.get_argument_parser(
    name='default',
    default_config_files=['config/defaults.ini'],
    description='Default configuration files.',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('--secret-key', type=str, env_var='SECRET_KEY', required=True,
                    help='The secret key. OooooOOooooh')

parser.add_argument('--log-level', type=str, env_var='LOG_LEVEL', required=False,
                    default='DEBUG', help='The log level for the application.')