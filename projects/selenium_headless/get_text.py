#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time, os

if __name__ == '__main__':

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.wait = WebDriverWait(driver, 5)

    server = 'http://cybersherpa.net'
    driver.get(server)
    time.sleep(5)
    driver.quit()

    h1_text = driver.find_element_by_id("title").text
    print(h1_text)
