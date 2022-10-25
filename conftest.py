import pytest
from selenium import webdriver
from locators import LoginPageLocators
from m2.config.local_config import *
from Credentials.credentials_magento import *



@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    browser.get(magento_base_url)
    name = browser.find_element(*LoginPageLocators.USER_NAME)
    name.send_keys(user_name)
    password = browser.find_element(*LoginPageLocators.USER_PASSWORD)
    password.send_keys(user_password)
    button = browser.find_element(*LoginPageLocators.CONFIRM_BUTTON)
    button.click()
    yield browser
    browser.quit()
