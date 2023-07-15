#!/usr/bin/env python
import logging
import json

logging.basicConfig(
    format='%(asctime)s - %(levelname)s: %(message)s',
    level=logging.INFO
)

log = logging.getLogger()

def create_user_location_file(names_file_path, locations_file_path):
    names_and_locations = dict()

    try:
        log.info(f'Reading {names_file_path}.')
        with open(names_file_path) as f:
            names = [x.rstrip('\n') for x in f.readlines()]

        log.info(f'Reading {locations_file_path}.')
        with open(locations_file_path) as f:
            locations = [x.rstrip('\n') for x in f.readlines()]

        log.info('Compiling lists in dictionary object.')
        names_and_locations = {
            'names': names,
            'locations': locations
        }

    except Exception as e:
        log.error(f'Unable to compile.\n{e}', exc_info=True)


    try:
        log.info(f'Writing to json file.')

        with open('names_and_locations.json', 'w+', encoding='utf-8') as f:
            json.dump(names_and_locations, f)

        log.info('File written successfully.')
    except Exception as e:
        log.error(e)


if __name__ == '__main__':
    create_user_location_file('users.txt', 'cities.txt')