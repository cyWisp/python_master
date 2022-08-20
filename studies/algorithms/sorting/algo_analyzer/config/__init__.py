import configargparse

parser = configargparse.get_argument_parser(
    name='default',
    description='parameters for running bubble sort',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('--log-level', '-lL', type=str, required=False,
                    default='INFO', help='Log level specification.')

parser.add_argument('--array-length', '-aL', type=int, required=False,
                    default=20, help='The length of the array to process')

parser.add_argument('--iterations', '-i', type=int, required=False,
                    default=3, help='The number of times to run the algorithm.')

parser.add_argument('--algorithm', '-a', type=str, required=False,
                    default='bubble', help='The algorithm to run: ["bubble"]')

cfg = parser.parse_known_args()[0]