from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = "http://10.0.30.122/magento_2/prefix_clear/admin/"
browser = webdriver.Chrome()
browser.implicitly_wait(20)
browser.get(link)

def magento_log_in(a, b):
    name = browser.find_element_by_id("username")
    name.send_keys(a)
    password = browser.find_element_by_id("login")
    password.send_keys(b)
    button = browser.find_element_by_class_name("action-login")
    button.click()

def walmart_log_in(a, b):
    user = browser.find_element_by_css_selector("#client_id")
    user.send_keys(a)
    password = browser.find_element_by_css_selector("#client_secret")
    password.send_keys(b)

def wait(a):
    clickable_element = WebDriverWait(browser, 40).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, a)))
    clickable_element.click()