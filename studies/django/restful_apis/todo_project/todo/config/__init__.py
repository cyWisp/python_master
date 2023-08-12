import configargparse

parser = configargparse.get_argument_parser(
    default_config_files=['todo/config/defaults.ini'],
    description='Just working on Django APIs',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('--db-name', type=str, required=True, env_var='DB_NAME',
                    help='The database name.')

parser.add_argument('--db-user', type=str, required=True, env_var='DB_USER',
                    help='The database user.')

parser.add_argument('--db-pass', type=str, required=True, env_var='DB_PASS',
                    help='The database password.')

parser.add_argument('--db-host', type=str, required=True, env_var='DB_HOST',
                    help='The database host name.')

parser.add_argument('--db-port', type=int, required=True, env_var='DB_PORT',
                    help='The database port number.')
