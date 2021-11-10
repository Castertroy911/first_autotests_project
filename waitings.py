from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_presence_of_element(selector, browser):
    located_element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    located_element.click()


def wait_element_clickable(selector, browser):
    clickable_element = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    clickable_element.click()


def waitElement(selector, browser, time=5):
    return WebDriverWait(browser, time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector)))


def waitForElementClickable(selector, browser, time=5):
    return WebDriverWait(browser, time).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
