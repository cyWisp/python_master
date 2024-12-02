import requests
import logging
from bs4 import BeautifulSoup

from requests.exceptions import HTTPError, ConnectionError, Timeout


logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger(__name__)


URL = 'https://www.lipsum.com/feed/html'

if __name__ == '__main__':

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    pars = ' '.join([x.text.replace('\n', '') for x in soup.findAll('p')])




