#!/usr/bin/env python
from requests import get
from requests import ConnectionError, HTTPError

if __name__ == '__main__':

    try:
        req = get('https://nothinwelkfhsdlkfh')
    except (ConnectionError, HTTPError) as e:
        print("no work")


