from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from waitings import *
from m2.config.local_config import *

def ebay_log_in(a, b, browser):
    try:
        switch_acc = wait_presence_of_element("#switch-account-anchor", browser)
    except TimeoutException as err:
        pass
    user = browser.find_element(By.ID, "userid")
    user.send_keys(a)
    button = wait_presence_of_element("#signin-continue-btn", browser)
    password = browser.find_element(By.ID, "pass")
    password.clear()
    password.send_keys(b)
    signin = browser.find_element(By.ID, "sgnBt")
    signin.click()
    submit = browser.find_element(By.ID, "submit")
    submit.click()
    browser.get("http://" + VM_IP + "/magento_2/prefix_clear/admin/m2epro/wizard_installationEbay/afterToken/mode/sandbox/")