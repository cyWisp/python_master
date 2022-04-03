#!/usr/bin/env python
#from urllib.request import urlopen, urlretrieve
from sys import argv, exit
from bs4 import BeautifulSoup
#import re, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def check_args():
    if len(argv) != 2:
        print(f"[x] Usage: {argv[0]} <URL>")
        exit(0)
    else:
        return argv[1]

# def get_html(url):
#     return urlopen(url).read()

# def find_elements(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     divs = soup.findAll('a')
#     links = [x['href'] for x in divs]

#     return links

# def return_loaded(url):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--window-size=1920x1080")

#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(url)

#     loaded_page_source = driver.page_source
#     driver.quit()

#     return loaded_page_source

if __name__ == '__main__':
    page = check_args()
    source = return_loaded(page)
    links = find_elements(source)
    
    for l in links:
        if "/p/" in l:
            print(f"https://www.instagram.com/youversion{l}")

    # raw_data = find_links(page)
    
    # base_data = raw_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    # print(base_data)

