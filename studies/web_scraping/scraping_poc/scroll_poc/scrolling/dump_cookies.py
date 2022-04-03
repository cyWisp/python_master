#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle
from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
from time import sleep

if __name__ == '__main__':

    user_name = "stoicberserker@gmail.com"
    pass_word = "ONElove1985$"

    # url = "https://www.instagram.com/python_scripts/"
    url = "https://www.instagram.com/"
    # login = ""

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    # chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    sleep(3)


    driver.get_screenshot_as_file("initial_load.png")
    login_button = driver.find_element_by_link_text('Log in')
    login_button.click()
    
    sleep(3)

    
    driver.get_screenshot_as_file("login.png")

    user_name_input = driver.find_element_by_name('username')
    user_name_input.send_keys(user_name)

    password_input = driver.find_element_by_name('password')
    password_input.send_keys(pass_word)

    sleep(3)

    driver.get_screenshot_as_file("type_fields.png")
    
    print("[*] Logging in...")
    login_button = driver.find_element_by_css_selector("button[type='submit']")
    login_button.click()

    sleep(5)

    driver.get_screenshot_as_file("logged_in.png")

    sleep(3)

    print("[*] Dumping session cookies...")
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

    new_url = "https://www.instagram.com/python_scripts/"
    driver.get(new_url)

    sleep(5)

    driver.get_screenshot_as_file("auth.png")

    driver.close()
