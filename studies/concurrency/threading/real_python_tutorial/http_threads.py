#!/usr/bin/env python
import logging
import requests
import threading
import configargparse
from time import sleep

parser = configargparse.get_argument_parser(name='default')

parser.add_argument('-t', '--thread-count', type=int, required=False, default=10)

logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.INFO
)

log = logging.getLogger()

TARGET_URL = 'https://example.com'

def get_response(task_id):
    log.info(f'Initiating request for {task_id}')
    response = requests.get(TARGET_URL)
    sleep(2)

    log.info(f'Task ID: {task_id} | Response Status: {response.status_code}')

if __name__ == '__main__':
    cfg = parser.parse_known_args()[0]

    log.info(f'Initiating requests running in {cfg.thread_count} threads.')

    threads = [threading.Thread(target=get_response, args=(x,)) for x in range(cfg.thread_count)]

    log.info('Starting threads.')

    for t in threads:
        log.info(f'Initializing thread {t}.')
        t.start()

    for t in threads:
        t.join()



