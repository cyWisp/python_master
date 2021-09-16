#!/usr/bin/env python
import time
from selenium import webdriver

def main():

	driver = webdriver.Firefox()
	time.sleep(3)
	driver.quit()

if __name__ == '__main__':
	main()
