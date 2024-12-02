import requests
import logging
import configargparse
import json

from requests.exceptions import (
    ConnectionError,
    HTTPError,
    Timeout
)

parser = configargparse.get_argument_parser()

parser.add_argument('--log-level', '-l', type=str, required=False, default='info',
                    help='The logging level for the application - <info, debug, warning, critical>')

parser.add_argument('--url', '-u', type=str, required=False, help='The target URL for the video.')
parser.add_argument('--output-file', '-o', type=str, required=False, default='video', help='Output file name.')

parser.add_argument('--url-list-file', '-uL', type=str, required=False, default=None,
                    help='A list of urls in text file format.')

cfg = parser.parse_known_args()[0]


logging.basicConfig(
    level=logging.getLevelName(cfg.log_level.upper()),
    format='%(process)d - %(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)

log = logging.getLogger()
log.name = 'default'
APP_VERSION = 'v1.0.0'
AUTHOR = 'W15P'


def show_splash():
    splash = '''               __ ____   ____.__    .___       
  ____   _____/  |\\   \ /   /|__| __| _/_______
 /    \\_/ __ \\   __\\   Y   / |  |/ __ |\\___   /
|   |  \\  ___/|  |  \\     /  |  / /_/ | /    / 
|___|  /\\___  >__|   \\___/   |__\\____ |/_____ \\
     \\/     \\/                       \\/      \\/
'''
    log.info('\n' + splash + '\n\t\t\t\t' + APP_VERSION + ' by ' + AUTHOR + '\n')


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
        download_video(u, file_name=f'{cfg.output_file}-{index + 1}.{get_video_file_extension(u)}')


def get_video_file_extension(url: str) -> str:
    return url.split('.')[-1]


show_splash()
log.debug(f'Configuration: {json.dumps(vars(cfg), indent=4)}')


if __name__ == '__main__':
    try:
        if not cfg.url_list_file and not cfg.url_list_file:
            raise ValueError('No URL(s) provided.\nPlease provide either a valid URL, or a list of URLs.')

        if cfg.url_list_file:
            download_multiple_videos(get_urls(cfg.url_list_file))

        if cfg.url:
            download_video(cfg.url, f'{cfg.output_file}.{get_video_file_extension(cfg.url)}')

    except ValueError as e:
        log.error(e)
