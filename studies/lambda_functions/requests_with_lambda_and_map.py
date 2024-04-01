#!/usr/bin/env python
import logging
import requests

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger()

URL = 'https://example.com'
five_urls = [URL for x in range(5)]


if __name__ == '__main__':
    response_content = list(map(lambda x: requests.get(x), five_urls))

    for r in response_content:
        log.info(f'{r.content.decode("utf-8")[:50]}\n')
