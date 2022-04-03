#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

if __name__ == '__main__':

    #chrome options instance, to set the size and headless preference
    chrome_options = Options() #instance of the Options class
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    #creating and instance of the chrome web driver
    driver = webdriver.Chrome(chrome_options=chrome_options) #executable_path=chrome_driver <-- not needed
    driver.get("https://www.google.com")

    lucky_button = driver.find_element_by_css_selector("[name = btnI]")
    lucky_button.click()

    #capture the screen
    driver.get_screenshot_as_file("screeny.png")

