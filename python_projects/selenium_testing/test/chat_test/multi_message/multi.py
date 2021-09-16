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

def get_elements(driver):

	global box, button

	driver.get("https://demos.lightstreamer.com/ChatDemo/")

	try:

		box = driver.wait.until(EC.presence_of_element_located((By.ID, "user_message")))
		button = driver.wait.until(EC.element_to_be_clickable((By.ID, "mex_button")))

		#box.send_keys(message)
		#button.click()

	except TimeoutException as to_ex:
		print("Error: {}".to_ex)

def send_message(message):

	box.send_keys(message)
	button.click()

def get_messages():

	file_messages = []

	try:
		with open('tester.txt', 'r') as message_file:
			for line in message_file.readlines():
				file_messages.append(line.strip())
	except:
		print("File Read Error")
	finally:
		message_file.close()

	return file_messages

def run():


	chats = get_messages()

	driver = init_driver()
	get_elements(driver)

	for m in chats:
		box.send_keys(m)
		time.sleep(1)
		button.click()

	time.sleep(3)
	driver.quit()
		
def main():

	run()
	

if __name__ == '__main__':
	main()
