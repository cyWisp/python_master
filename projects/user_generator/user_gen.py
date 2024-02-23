import configargparse
import json
import logging


parser = configargparse.get_argument_parser(
    description='Command line arguments for user generator',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('')