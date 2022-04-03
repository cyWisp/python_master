import asyncio
import requests
import logging
from bs4 import BeautifulSoup

SITES = [
    'http://cybersherpa.net',
    'http://example.com',
    'https://ipchicken.com/'
]

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(levelname)s: %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)

async def get_content(url):
    try:
        response = requests.get(url)
        logging.debug(f'Response: {response.status_code}')
        await asyncio.sleep(1)
        return response
    except Exception as e:
        logging.exception(f'Something went wrong: {e}')


async def parse_response(response, url):
    try:
        logging.info(f'Parsing response for {url}')
        links = BeautifulSoup(response.content, 'html.parser').findAll('a', href=True)
        await asyncio.sleep(1)
        return [l['href'] for l in links]
    except Exception as e:
        logging.exception(f'Something went wrong: {e}')
        return None


async def get_links(url):
    logging.info(f'Initiating request for {url}')
    http_response = await get_content(url)

    try:
        assert http_response.content is not None, 'Response cannot be empty.'
        assert http_response.status_code == 200, 'Request returned non-200 response'
    except AssertionError as e:
        logging.exception(e)
        return None

    parse_result = await parse_response(http_response, url)
    return parse_result


async def main(*args):
    results = await asyncio.gather(*(get_links(x) for x in args))
    return results


def display_results(r):
    for res in r: logging.info(res)


if __name__ == '__main__':
    logging.info('Starting main.')
    results = asyncio.run(main(*SITES))
    display_results(results)
