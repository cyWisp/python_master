#!/usr/bin/env python
import logging
import json
import sys
import random

from config import parser

cfg = parser.parse_known_args()[0]

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.getLevelName(cfg.log_level.upper()),
    handlers=[
        logging.FileHandler(cfg.log_file, 'a+', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

log = logging.getLogger()

log.debug(json.dumps(vars(cfg), indent=4))


def load_sample_data(file_list: list) -> dict:
    s_data = {}

    for f in file_list:
        log.info(f'Loading {f}')
        s_data[f.split('.')[0].split('/')[-1]] = json.load(open(f))

    return s_data


def create_customer_records(s_data: dict, num_records: int) -> list:
    new_customers = []

    for i in range(num_records):
        first_name = random.choice(s_data['first-names'])
        last_name = random.choice(s_data['last-names'])

        new_record = {
            'customer_first_name': first_name,
            'customer_last_name': last_name,
            'customer_address': f'{random.randint(1111, 9999)} {random.choice(s_data["street-names"])}',
            'customer_city': random.choice(s_data['us-cities']),
            'customer_state': random.choice(s_data['states']),
            'customer_zip': f'{random.randint(11111, 99999)}-{random.randint(1111, 9999)}',
            'customer_phone': f'{random.randint(111, 999)}{random.randint(111, 999)}'
                              f'{random.randint(1111, 9999)}',
            'customer_email': f'{first_name}.{last_name}@{random.choice(s_data["domain-names"])}'
        }

        new_customers.append(new_record)

    return new_customers


if __name__ == '__main__':
    from db.ms_api import MSInterface

    ms_db = MSInterface(
        'comic_book_shop_1',
        'localhost',
        'root',
        'password'
    )

    # ten_customers = ms_db.execute_query('SELECT * FROM customer LIMIT 1, 10')
    # log.info(json.dumps(ten_customers, indent=4))

    data_files = [
        'data/domain-names.json',
        'data/first-names.json',
        'data/last-names.json',
        'data/marvel.json',
        'data/street-names.json',
        'data/us-cities.json',
        'data/words.json',
        'data/states.json',
        'data/words.json'
    ]

    sample_data = load_sample_data(data_files)
    new_customer_records = create_customer_records(sample_data, 100)

    for r in new_customer_records:
        log.info(json.dumps(r, indent=4))

        query = f'''
        INSERT INTO `customer` (
            `customer_first_name`,
            `customer_last_name`,
            `customer_address`,
            `customer_city`,
            `customer_state`,
            `customer_zip`,
            `customer_phone`,
            `customer_email`
        ) VALUES (
            \'{r["customer_first_name"]}\',
            \'{r["customer_last_name"]}\',
            \'{r["customer_address"]}\',
            \'{r["customer_city"]}\',
            \'{r["customer_state"]}\',
            \'{r["customer_zip"]}\',
            \'{r["customer_phone"]}\',
            \'{r["customer_email"]}\'
        );'''

        result = ms_db.execute_query(query)
        log.info(result)
