#!/usr/bin/env python
import configargparse
import json
from logger.logger import Logger

parser = configargparse.get_argument_parser(
    name='default'
)

parser.add_argument('-lf', '--log-file', type=str, required=True,
                    help='Log file to parse')

cfg = parser.parse_known_args()[0]
log = Logger().get_logger()


class LogParser:
    def __init__(self, log_file_name: str) -> None:
        self.log_file_name = log_file_name
        self.records = dict()

    def read_file_gen(self):
        try:
            with open(self.log_file_name, 'r') as f:
                for row in f.readlines():
                    yield row.replace('\n', '')
        except (IOError, FileNotFoundError) as e:
            log.error(e)

    def populate_empty_records(self):
        for row in self.read_file_gen():
            if 'EventID' in row:
                event_id = row.split('>')[1].split('<')[0]
                self.records[event_id] = {
                    'ORDER_TAKEN': 0,
                    'ORDER_DELIVERED': 0,
                    'ORDER_MODIFIED': 0,
                    'PAYMENT': 0,
                    'DATE': ''
                }

    def extract_records(self):
        event_id, event_data, event_time, date_time = None, None, None, None

        for row in self.read_file_gen():
            if '<EventID>' in row:
                event_id = row.split('>')[1].split('<')[0]

            if '<Date>' in row:
                event_date = row.split('>')[1].split('<')[0]

            if '<Time>' in row:
                event_time = row.split('>')[1].split('<')[0]

                date_time = f'{event_date} {event_time}'
                self.records[event_id]['DATE'] = date_time

            if '<Stage>' in row:
                stage = row.split('>')[1].split('<')[0]
                self.records[event_id][stage] += 1

        return self.records

if __name__ == '__main__':
    log.info(f'Configuration: {json.dumps(vars(cfg), indent=4)}')

    parser_object = LogParser(cfg.log_file)
    parser_object.populate_empty_records()
    records = parser_object.extract_records()

    for event_id, stats in records.items():
        log.info(f'{event_id}: {stats}')

