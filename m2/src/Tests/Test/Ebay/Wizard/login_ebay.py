from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from waitings import *


def ebay_log_in(a, b, browser):
    try:
        switch_acc = wait("#switch-account-anchor", browser)
    except TimeoutException as err:
        pass
    user = browser.find_element(By.ID, "userid")
    user.send_keys(a)
    button = wait("#signin-continue-btn", browser)
    password = browser.find_element(By.ID, "pass")
    password.clear()
    password.send_keys(b)
    signin = browser.find_element(By.ID, "sgnBt")
    signin.click()
    submit = browser.find_element(By.ID, "submit")
    submit.click()
    browser.get("http://10.0.30.122/magento_2/prefix_clear/admin/m2epro/wizard_installationEbay/afterToken/mode/sandbox/")