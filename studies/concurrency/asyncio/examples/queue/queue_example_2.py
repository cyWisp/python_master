#!/usr/bin/env python
import asyncio
import requests
import logging
from bs4 import BeautifulSoup

URLS = [
    'http://cybersherpa.net',
    'https://example.com',
    'https://someonewhocares.org',
    'https://www.scrapethissite.com/pages/simple/',
    'https://www.scrapethissite.com/pages/ajax-javascript/'
]

logging.basicConfig(
    format='%(process)d - %(funcName)s: %(message)s',
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger()


async def get_response(url):
    try:
        log.info(f'Requesting {url}')
        response = requests.get(url)

        return response
    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.HTTPError,
        requests.exceptions.Timeout
    ) as e:
        log.error(e)


async def process_html(q):
    r = await q.get()

    logging.info(f'Retrieving links for {r.url}.')

    links = BeautifulSoup(r.content, 'html.parser').findAll('a', href=True)

    log.info(f'Links: {[l["href"] for l in links]}')

    q.task_done()


async def add_to_queue(url, q):
    http_response = await get_response(url)

    log.info(f'Adding {http_response.url} to processing queue.')
    await q.put(http_response)


async def main():
    q = asyncio.Queue()

    prod = [asyncio.create_task(add_to_queue(u, q)) for u in URLS]
    con = [asyncio.create_task(process_html(q)) for i in range(10)]

    await asyncio.gather(*prod)
    await q.join()

    for c in con:
        c.cancel()


if __name__ == '__main__':
    log.info('Initializing link scraper.')
    asyncio.run(main())