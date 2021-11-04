import pytest
from selenium import webdriver
from m2.config.local_config import *
from Credentials.credentials_magento import *
import time


@pytest.fixture(scope='module')
def browser():
    with webdriver.Chrome() as driver:
        driver.implicitly_wait(5)
        driver.get(magento_base_url)
        name = driver.find_element_by_id("username")
        name.send_keys(user_name)
        password = driver.find_element_by_id("login")
        password.send_keys(user_password)
        button = driver.find_element_by_class_name("action-login")
        button.click()
        yield driver



