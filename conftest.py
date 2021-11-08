import pytest
from selenium import webdriver
from m2.config.local_config import *
from Credentials.credentials_magento import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


@pytest.fixture(scope='module')
def browser(self):
    with webdriver.Chrome() as driver:
        driver.implicitly_wait(5)
        driver.get(magento_base_url)
        name = driver.find_element(By.ID, "username")
        name.send_keys(user_name)
        password = driver.find_element(By. ID, "login")
        password.send_keys(user_password)
        button = driver.find_element(By.CLASS_NAME, "action-login")
        button.click()
        yield driver