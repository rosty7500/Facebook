__author__ = 'admin'

from selenium.webdriver.common.by import By

class login_locators(object):
    _email = (By.ID, "email")
    _password = (By.ID, "pass")
    _submit = (By.ID, "u_0_q")
    _incorrect_email = (By.XPATH, "//div[@id='js_0']/div/div/div/a")
    _incorrect_password = (By.XPATH, "//div[@id='js_0']/div/div/div/a")











