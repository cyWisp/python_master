#!/usr/bin/env python
import requests
import logging
import threading
import time
import uuid

logging.basicConfig(
    datefmt='%Y-%m-%d %H:%M:%S',
    format='%(process)d - %(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s',
    handlers=[logging.StreamHandler()],
    level=logging.INFO
)

log = logging.getLogger()


def get_response(url: str = None, thread_id: str = None):
    try:
        log.info(f'Thread {thread_id} requesting {url}')
        response = requests.get(url)

        log.info(f'Request status: {response.status_code}')

    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.HTTPError,
        requests.exceptions.Timeout
    ) as e:
        log.error(f'Thread {thread_id} failed:\n{e}')


if __name__ == '__main__':
    log.info(f'Starting MAIN.')

    urls = [
        'https://examples.com',
        'https://someonewhocares.org/hosts/',
        'https://www.scrapethissite.com/pages/simple/',
        'https://www.scrapethissite.com/pages/forms/',
        'https://www.scrapethissite.com/pages/frames/'
    ]

    http_threads = list()

    for url in urls:
        new_thread = threading.Thread(target=get_response, args=(url, uuid.uuid4()))

        http_threads.append(new_thread)
        new_thread.start()

    for thread in http_threads:
        thread.join()

    log.info(f'All threads terminated.')