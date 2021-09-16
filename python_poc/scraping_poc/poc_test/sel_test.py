#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os, time
from sys import argv

def get_args():
    if len(argv) != 2:
        exit(0)
    else:
        return argv[1]

if __name__ == '__main__':

    #chrome options instance, to set the size and headless preference
    chrome_options = Options() #instance of the Options class
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    #creating and instance of the chrome web driver
    driver = webdriver.Chrome(options=chrome_options) #executable_path=chrome_driver <-- not needed
    driver.get(get_args())

    #lucky_button = driver.find_element_by_css_selector("[name = btnI]")
    #lucky_button.click()

    #capture the screen

    driver.get_screenshot_as_file("top.png")
    # counter = 0

    # while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(3)
    #     driver.get_screenshot_as_file(f"screen_{counter}.png")
    #     counter += 1
    #     if counter == 2:
    #         break
        #target_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "K50FK")))
        #driver.implicitly_wait(15)
    time.sleep(30)
    driver.get_screenshot_as_file("bottom.png")
    driver.quit()