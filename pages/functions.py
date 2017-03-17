__author__ = 'admin'

from selenium import webdriver
import time
import os
from pages.Locators import login_locators

path = os.getcwd()
print(path)

class feature_pages(object):
    def __init__(self, base_url):
        self.driver = webdriver.Chrome(path + '\\chrome\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(base_url)

    def accessing_signin_pages_valid(self):
        driver1 = self.driver
        time.sleep(10)
        driver1.find_element(*login_locators._email).send_keys("rosty_06@yahoo.com")
        driver1.find_element(*login_locators._password).send_keys("rash02079190!@#$%")
        time.sleep(2)
        driver1.find_element(*login_locators._submit).click()
        time.sleep(8)
        driver1.find_element(*login_locators._name_present).is_displayed()
        driver1.quit()

    def accessing_invalid_login(self):
        driver1 = self.driver
        time.sleep(10)
        driver1.find_element(*login_locators._email).send_keys("rosty_06@gmail.com")
        driver1.find_element(*login_locators._password).send_keys("rash02079190!@#$%")
        time.sleep(2)
        driver1.find_element(*login_locators._submit).click()
        time.sleep(10)
        self.invalid_email = driver1.find_element(*login_locators._incorrect_email).text
        driver1.quit()
        return self.invalid_email

    def accessing_invalid_password_login(self):
        driver1 = self.driver
        time.sleep(10)
        driver1.find_element(*login_locators._email).send_keys("rosty_06@yahoo.com")
        driver1.find_element(*login_locators._password).send_keys("test")
        time.sleep(2)
        driver1.find_element(*login_locators._submit).click()
        time.sleep(15)
        self.invalid_password = driver1.find_element(*login_locators._incorrect_password).text
        driver1.quit()
        return self.invalid_password












