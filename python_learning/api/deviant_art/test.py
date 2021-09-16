#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from pprint import pprint

if __name__=='__main__':

	da = "https://www.deviantart.com/daily-deviations"
	url = "https://randomuser.me/api/"

	response = requests.get(url)

	pprint(response.json())
