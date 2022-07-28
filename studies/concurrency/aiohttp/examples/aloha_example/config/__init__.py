import configargparse

parser = configargparse.get_argument_parser(
    default_config_files=['config/defaults.ini'],
    description='Aloha NCR/POS Date Corrections - '
                'Source: http://sckgit.fastinc.com/QPM/aloha-ncr-pos/tree/master',
    formatter_class=configargparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument('--log-file', env_var='LOG_FILE', required=False,
                    default='/var/log/kb/aloha/aloha-NCR-POS.log', help='Log file name.')

parser.add_argument('--log-level', env_var='LOG_LEVEL', required=False,
                    default='INFO', help='Log level parameter.')

parser.add_argument('--listening-port', env_var='LISTENING_PORT', required=False,
                    default=8083, help='Port to listen on for incoming requests.')

parser.add_argument('--forwarding-port', env_var='FORWARDING_PORT', required=False,
                    default=8080, help='Port to forward to.')

parser.add_argument('--date-format', env_var='DATE_FORMAT', required=False,
                    default='%Y-%m-%d', help='The expected date format.')

cfg = parser.parse_known_args()[0]