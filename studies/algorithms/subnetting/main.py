#!/usr/bin/env python
import logging
import configargparse
import json

parser = configargparse.get_argument_parser(
    name='default',
    description='Arguments for subnet calculator.',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('--log-level', type=str, required=False,
                        default='INFO', help='The default log level.')
parser.add_argument('--cidr', type=str, required=False,
                    default='/24', help='The CIDR suffix to calculate.')

cfg = parser.parse_known_args()[0]

logging.basicConfig(
    format='%(levelname)s: %(message)s',
    level=logging.getLevelName(cfg.log_level.upper()),
    handlers=[logging.StreamHandler()]
)

log = logging.getLogger()

class MagicNumber:
    def __init__(self, suffix):
        self.suffix = int(suffix.replace('/', ''))
        self.net_mask = list()
        self.bin_map = [[0 for x in range(8)] for y in range(4)]
        self.bin_values = {
            0: 128,
            1: 64,
            2: 32,
            3: 16,
            4: 8,
            5: 4,
            6: 2,
            7: 1
        }

    def map_suffix(self):
        for i in range(len(self.bin_map)):
            for j in range(len(self.bin_map[i])):
                if sum([sum(x) for x in self.bin_map]) == self.suffix:
                    break
                self.bin_map[i][j] = 1

        log.info(f'Binary: {".".join(["".join([str(x) for x in y]) for y in self.bin_map])}')

    def calculate_net_mask(self):
        log.info('Calculating Subnet Mask.')
        self.map_suffix()

        for i in range(len(self.bin_map)):
            octet = 0

            for j in range(len(self.bin_map[i])):
                if self.bin_map[i][j] == 1:
                    octet += self.bin_values[j]

            self.net_mask.append(octet)


    def display_result(self):
        log.info(f'Network suffix: /{self.suffix} | Subnet Mask: {str(".".join([str(x) for x in self.net_mask]))}')

if __name__ == '__main__':
    log.debug(json.dumps(vars(cfg), indent=4))

    mn_object = MagicNumber(cfg.cidr)
    mn_object.calculate_net_mask()
    mn_object.display_result()
