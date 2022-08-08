import configargparse

parser = configargparse.get_argument_parser(
    description='Some description- we are trying to create '
                'a forwarder',
    default_config_files=['default.ini'],
    formatter_class=configargparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument('--log-level', type=str, required=False,
                    default='INFO', help='Log level.')

parser.add_argument('--listening-port', type=int, required=False,
                    default=9999, help='The port to listen on.')

parser.add_argument('--forwarding-port', type=int, required=False,
                    default=8080, help='The port to forward to.')

cfg = parser.parse_known_args()[0]