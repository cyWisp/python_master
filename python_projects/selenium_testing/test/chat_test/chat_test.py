#!/usr/bin/env python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def init_driver():

	driver = webdriver.Chrome()
	driver.wait = WebDriverWait(driver, 5)
	return driver

def lookup(driver, message):

	driver.get("https://demos.lightstreamer.com/ChatDemo/")
	try:
		box = driver.wait.until(EC.presence_of_element_located((By.ID, "user_message")))
		button = driver.wait.until(EC.element_to_be_clickable((By.ID, "mex_button")))
		box.send_keys(message)
		button.click()
	except TimeoutException:
		print("Box or Button not found in google.com")

if __name__ == '__main__':
	driver = init_driver()
	lookup(driver, "hentai")
	time.sleep(5)
	driver.quit()
