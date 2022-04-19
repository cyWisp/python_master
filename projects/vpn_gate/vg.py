#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

URL = "https://www.vpngate.net/en/"

class PageElements:
    def __init__(self, url):
        self.url = url
        self.response = None
        self.soup = None

    def get_site_data(self):
        self.response = requests.get(self.url)

    def get_table_rows(self):
        try:
            self.soup = BeautifulSoup(self.response.content, 'html.parser')
            # table_rows = self.soup.findAll('tr')
            return self.soup.findAll('td', {'class': 'vg_table_row_1'})
        except Exception as e:
            print(e)


if __name__ == '__main__':
    pe = PageElements(URL)
    pe.get_site_data()
    table_data = pe.get_table_rows()

    for t in table_data:
        print(t.text)

