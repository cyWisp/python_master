import requests
import logging

from requests.exceptions import (
    ConnectionError,
    HTTPError,
    Timeout
)

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger()
log.name = 'default'

TARGET_URL = 'https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/YSvEcxy/videoblocks-lots-of-100-dollars-american-bills-money-banknotes-cash-finance-and-investment-concept-rich-business-economy-of-usa-shooting-at-an-angle-currency-exchange-of-one-hundred-usd-copy-space_hvas6ybdo__117b9e39447cd30553aa6ab2ef7e85a9__P360.mp4'


def download_video(url: str, file_name: str = None):
    try:
        log.info(f'Requesting: {url}')
        r = requests.get(url)

        log.info(f'Downloading associated video.')
        with open(file_name, 'wb') as vid:
            vid.write(r.content)

    except (IOError, FileNotFoundError) as e:
        log.error(f'File write failed:\n{e}', exc_info=True)

    except (ConnectionError, HTTPError, Timeout) as e:
        log.error(f'HTTP request failed:\n{e}', exc_info=True)


def get_urls(file_name: str) -> list:
    try:
        log.info(f'Reading urls from {file_name}')

        with open(file_name) as f:
            return [x.replace('\n', '') for x in f.readlines()]

    except (IOError, FileNotFoundError) as e:
        log.error(f'Unable to read url file:\n{e}', exc_info=True)




def download_multiple_videos(url_list: list) -> None:
    for index, u in enumerate(url_list):
        download_video(u, file_name=f'video-{index + 10}.mp4')


if __name__ == '__main__':
    # download_video(TARGET_URL)

    # for i in get_urls('scratch.txt'):
    #     log.info(i)

    download_multiple_videos(get_urls('scratch.txt'))
