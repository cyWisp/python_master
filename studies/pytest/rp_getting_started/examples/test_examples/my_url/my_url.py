import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout


def make_request(url):
    try:
        return requests.get(url)
    except (
        ConnectionError,
        HTTPError,
        Timeout
    ) as e:
        print(f'Request failed: {e}')
