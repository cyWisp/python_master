#!/usr/bin/env python
import concurrent.futures
import requests
import logging
import configargparse
import time

parser = configargparse.get_argument_parser(name='default')
parser.add_argument('-t', '--thread-count', type=int, required=False, default=5)
parser.add_argument('-l', '--log-level', type=str, required=False, default='INFO')
cfg = parser.parse_known_args()[0]

logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.getLevelName(cfg.log_level)
)
log = logging.getLogger()

URL = 'https://example.com'


def get_http_response(name, url):
    log.info(f'Initiating request to {url} for {name}')
    request_status_code = requests.get(url).status_code

    time.sleep(2)

    log.info(f'Thread {name} | Status code: {request_status_code}')
    return request_status_code

if __name__ == '__main__':
    results = list()

    with concurrent.futures.ThreadPoolExecutor(max_workers=cfg.thread_count) as ex:
        # ex.map(get_http_response, range(cfg.thread_count))

        for i in range(cfg.thread_count):
            status = ex.submit(get_http_response, i, URL)
            results.append(status)

    log.info(f'Results: {[x.result() for x in results]}')