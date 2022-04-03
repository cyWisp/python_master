#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from time import sleep
from sys import exit
import re, json

def get_single_post(url):
    return urlopen(url).read()

def login(creds):

    url = "https://www.instagram.com/"

    print("[*] Settings chrome options...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    print("[*] Navigating to web page...")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    print("[*] Logging in...")
    sleep(3)

    login_button = driver.find_element_by_link_text('Log in')
    login_button.click()

    sleep(3)

    user_name_input = driver.find_element_by_name('username')
    user_name_input.send_keys(creds[0])

    password_input = driver.find_element_by_name('password')
    password_input.send_keys(creds[1])

    sleep(3)

    login_button = driver.find_element_by_css_selector("button[type='submit']")
    login_button.click()

    print("[*] Taking screen shot...")
    sleep(3)

    driver.get_screenshot_as_file("logged_in.png")

    return driver

def read_creds():

    print("[*] Reading user credentials...")
    try:
        with open("./creds.txt", "r+") as cfile:
            creds = [x.strip("\n") for x in cfile.readlines()]
    except:
        print("[x] Unable to read file...")
    else:
        return creds
    finally:
        cfile.close()

def post_count(html):

    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.findAll('span')
    total = int(posts[6].text)

    return total

def scroll(driver, url):
    
    print("[*] Navigating to requested url...")
    driver.get(url)
    sleep(3)
    
    print("[*] Initial screen capture taken...")
    driver.get_screenshot_as_file('initial_load.png')
    page_body = driver.find_element_by_tag_name('body')
    
    print("[*] Calculating scroll distance...")
    html = driver.page_source
    posts = post_count(html)
    scroll_count = (posts // 12) * 51

    print(f"[*] Scrolling with arrow DOWN {scroll_count} times...")

    print("[*] Scrolling...")
    for x in range(scroll_count):
        page_body.send_keys(Keys.DOWN)
    
    print("[*] Bottom reached- taking final screen capture...")
    driver.get_screenshot_as_file('bottom.png')
    driver.quit()

def check_url(url):
    try:
        html = urlopen(url).read()
    except ValueError as value_error:
        print(f"[x] Value Error encountered:\n{value_error}")
        exit(0)
    except HTTPError as http_error:
        print(f"[x] HTTP Error encountered:\n{http_error}")
        exit(0)
    except URLError as url_error:
        print(f"[x] URL Error encountered:\n{url_error}")
        exit(0)
    else:
        pass

def parse_data(html):
    try:
        #print("[*] Parsing post data...")
        soup = BeautifulSoup(html, 'html.parser')
        shared_data = soup.find('script', text=re.compile('window._sharedData'))
        json_raw = shared_data.text.split(' = ', 1)[1].rstrip(';')
        raw_data = json.loads(json_raw)
        base_data = raw_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
        type_name = base_data['__typename']
    except KeyError:
        print(f"[x] Cannot read post URL!\n[?] URL may belong to a profile page.")
        exit(0)
    else:
        return base_data, type_name
