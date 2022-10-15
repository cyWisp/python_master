#!/usr/bin/env python
import logging, configargparse, json
from random import randint

parser = configargparse.get_argument_parser(
    name='default',
    description='algorithm parameters',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('-l', '--length', type=int, required=False,
                    default=20, help='The length of the array to test.')
parser.add_argument('--log-level', type=str, required=False,
                    default='DEBUG', help='Debugging log level.')


cfg = parser.parse_known_args()[0]

logging.basicConfig(
    format='%(asctime)s - %(levelname)s: %(message)s',
    level=logging.getLevelName(cfg.log_level.upper()),
    handlers=[logging.StreamHandler()]
)

log = logging.getLogger()

log.debug(f'Configuration: {json.dumps(vars(cfg), indent=4)}')

def generate_array(length: int) -> list | None:
    array = list()

    try:
        assert length > 0, 'Length cannot be zero or negative.'

        while len(array) != length:
            random_number = randint(1, length)
            if random_number not in array:
                array.append(random_number)

        return array

    except AssertionError as e:
        log.error(e)
        return


def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):  # Looping from the second element
        key_item = array[i]         # current_item
        j = i - 1                   # variable for correct position of element

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array


if __name__ == '__main__':

    arr = generate_array(cfg.length)
    log.debug(f'New array: {arr}')
    log.debug(f'Sorted array: {insertion_sort(arr)}')

