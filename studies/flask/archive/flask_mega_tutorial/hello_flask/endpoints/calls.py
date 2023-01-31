import requests
import logging
from requests.exceptions import HTTPError, ConnectionError, Timeout


def get_external_ip():
    try:
        response = requests.get('https://checkip.amazonaws.com')
        return response.content.decode('utf-8').replace('\n', '')
    except (HTTPError, ConnectionError, Timeout) as e:
        logging.error(e)
