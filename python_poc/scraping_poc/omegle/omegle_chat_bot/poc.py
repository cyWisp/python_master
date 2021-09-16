#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

#def check_elements(source):

class Pause():
    def __init__(self):
        pass
    def small(self):
        sleep(1)
    def medium(self):
        sleep(3)
    def large(self):
        sleep(5)

def get_driver(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    return driver

def start_chat(driver, p):

    # Click text chat button
    print("[*] Starting chat...")
    text_chat_button = driver.find_element_by_id('textbtn')
    text_chat_button.click()

    driver.get_screenshot_as_file("text_chat.png")

    p.medium()

    # find text area and type greeting
    text_area_entry = driver.find_element_by_class_name("chatmsg")
    text_area_entry.send_keys("Hi there...")

    p.small()
    
    driver.get_screenshot_as_file("typed_message.png")

    # find  and click send button
    send_button = driver.find_element_by_class_name("sendbtn")
    p.small()
    send_button.click()
    p.medium

    # Wait for response
    p.large()

    driver.get_screenshot_as_file("sent_message.png")

    current_state = driver.page_source

    return current_state, driver

def get_log(source):

    soup = BeautifulSoup(source, 'html.parser')
    log_items = soup.findAll('span')

    chat = [l.text for l in log_items]
    return chat



if __name__ == '__main__':

    sleep_duration = Pause()

    # Navigate to website
    print("[*] Navigating...")
    omegle = "https://www.omegle.com/"
    driver = get_driver(omegle)
    
    sleep_duration.samll()
    driver.get_screenshot_as_file("omegle.png")

    state, driver = start_chat(driver, sleep_duration)
    chat = get_log(state)

    



    print("[*] Exiting...")
    driver.quit()



