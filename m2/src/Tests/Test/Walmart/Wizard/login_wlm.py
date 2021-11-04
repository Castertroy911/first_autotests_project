from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time


def walmart_log_in(a, b, browser):
    user = browser.find_element_by_css_selector("#client_id")
    user.send_keys(a)
    password = browser.find_element_by_css_selector("#client_secret")
    password.send_keys(b)