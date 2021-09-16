#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def init_driver():

	#creates a Firefox webdriver object called 'driver'
	driver = webdriver.Firefox()
	#tells driver to wait until the page has fully loaded for at least 5 seconds
	driver.wait = WebDriverWait(driver, 5)
	#returns the driver object
	return driver

def lookup(driver, query):

	driver.get("http://www.google.com")

	try:

		box = driver.wait.until(EC.presence_of_element_located(By.NAME, "q"))
		button = driver.wait.until(EC.element_to_be_clickable(By.NAME, "btnK"))
		box.send_keys(query)
		button.click()
	except TimeoutException:
		print("Box or Button not found in google.com")

if __name__ == '__main__':
	driver = init_driver()
	lookup(driver, "Selenium")
	time.sleep(5)
	driver.quit()
