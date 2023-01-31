#!/usr/bin/env python
import random
import logging
import json
import math


logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.DEBUG
)

log = logging.getLogger()

NUM_CLASSES = 6
MIN_DATA_VALUE = 0
# MAX_DATA_VALUE = 104


def generate_commute_times():
    log.debug('Generating commute times.')
    commute_times = [random.randint(0, 104) for _ in range(200)]

    try:
        with open('times.json', 'w') as f:
            json.dump(commute_times, f)
    except Exception as e:
        log.error(e)


def read_commute_times():
    log.debug('Reading commute times file.')
    try:
        with open('times.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        log.error(e)


def calculate_class_width(t_list):
    max_value = max(t_list)
    return (max_value - MIN_DATA_VALUE) / NUM_CLASSES, max_value


def get_class_limits(class_width: int, max_value: int) -> dict:
    limits = dict()
    l_limit = 0

    while True:
        log.debug(l_limit)
        if l_limit >= max_value:
            break

        if l_limit == 0:
            limits[l_limit] = class_width - 1
            l_limit += class_width
            continue

        limits[l_limit] = l_limit + class_width - 1
        l_limit += class_width

    return limits

def get_tally(limits_dict, data_set):
    results_dict = dict()

    for lower_limit, upper_limit in limits_dict.items():
        count = 0
        for num in data_set:
            if num >= lower_limit and num <= upper_limit:
                count += 1
        results_dict[f'{lower_limit}-{upper_limit}'] = count

    return results_dict


if __name__ == '__main__':
    t = read_commute_times()
    # log.debug(json.dumps(t, indent=4))

    c_width, m_value = calculate_class_width(t)
    c_width = round(c_width)

    log.debug(f'Class width: {c_width}')

    lims = get_class_limits(c_width, m_value)
    log.debug(json.dumps(lims, indent=4))

    r = get_tally(lims, t)

    log.debug(json.dumps(r, indent=4))