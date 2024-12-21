from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

USER_NAME = 'roberto.daglio@esimplicity.com'
PASSWORD = 'LOVEtoCODE69$'

if __name__ == '__main__':

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('http://localhost:3000')




    # cookies
    # cookies = driver.get_cookies()
    #
    # print(cookies)
    #
    # driver.quit()

    # login functionality

    # driver.save_screenshot('pre_login.png')

    login_button = driver.find_element(By.XPATH, '//button[text()="Portal Login"]')

    login_button.click()

    sleep(1)

    driver.save_screenshot('post_login.png')

    driver.find_element(By.ID, 'input28').send_keys(USER_NAME)
    driver.find_element(By.ID, 'input36').send_keys(PASSWORD)

    driver.find_element(By.CLASS_NAME, 'button.button-primary').click()

    sleep(3)

    driver.save_screenshot('post_login.png')

    driver.quit()