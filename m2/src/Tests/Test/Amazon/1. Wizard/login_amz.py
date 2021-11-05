from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from waitings import *
from m2.config.local_config import *


def amazon_log_in(a, b, c, browser):
    email = browser.find_element(By.ID, "ap_email")
    email.clear()
    email.send_keys(a)
    password = browser.find_element(By.ID, "ap_password")
    password.clear()
    password.send_keys(b)
    keep_signed_in = browser.find_element(By.CSS_SELECTOR, "[name='rememberMe']")
    keep_signed_in.click()
    button = wait("#signInSubmit", browser)
    try:
        enter_otp = browser.find_element(By.ID, "auth-mfa-otpcode")
        browser.execute_script("window.open('https://gauth.apps.gbraad.nl/')")
        browser.switch_to.window(browser.window_handles[1])
        edit = browser.find_element(By.ID, "edit")
        edit.click()
        button = wait("#addButton", browser)
        acc_name = browser.find_element(By.ID, "keyAccount")
        acc_name.send_keys("Amazon")
        acc_secret = browser.find_element(By.ID, "keySecret")
        acc_secret.send_keys(c)
        button = wait("#addKeyButton", browser)
        password = browser.find_element(By.CSS_SELECTOR, ".ui-last-child.ui-li-static h3").text
        browser.switch_to.window(browser.window_handles[0])
        enter_otp.send_keys(password)
        checkbox = browser.find_element(By.ID, "auth-mfa-remember-device")
        checkbox.click()
        button = wait("#auth-signin-button", browser)
        account = browser.find_element(By.XPATH, "//div [text() = 'M2EPRO_NA_TEST_1']")
        account.click()
        US = browser.find_element(By.XPATH, "//div [text() = 'United States']")
        US.click()
        button = wait(".picker-switch-accounts-button", browser)
    except NoSuchElementException as err:
        pass
    check = browser.find_element(By.CLASS_NAME, "checkbox")
    check.click()
    button = wait(".primary", browser)
    button = wait(".primary", browser)
    browser.get("http://" + VM_IP + "/magento_2/prefix_clear/admin/m2epro/wizard_installationAmazon/afterGetTokenAutomatic/?Merchant=A1VHQHEVZ1GTIX&Marketplace=A1AM78C64UM0Y8&MWSAuthToken=amzn.mws.bca3f75c-a693-49c7-6da0-649e33313dfb&Signature=VAkK4rRdGpgI%2F1nlIB8U9oNKv7lDV0JSoXM6ekBHsUE%3D&SignedString=POST%0D%0Ahttps%3A%2F%2Fm2epro.com%2Faccept-a-na.php%0D%0A%3Fback_url%3DaHR0cDovLzEwLjAuMzAuMTIyL21hZ2VudG9fMi9wcmVmaXhfY2xlYXIvYWRtaW4vbTJlcHJvL3dpemFyZF9pbnN0YWxsYXRpb25BbWF6b24vYWZ0ZXJHZXRUb2tlbkF1dG9tYXRpYy8%3D%0D%0AAWSAccessKeyId%3DAKIAJUNZPBN3EXTI3FCQ%26MWSAuthToken%3Damzn.mws.bca3f75c-a693-49c7-6da0-649e33313dfb%26Marketplace%3DA1AM78C64UM0Y8%26Merchant%3DA1VHQHEVZ1GTIX%26SignatureMethod%3DHmacSHA256%26SignatureVersion%3D2")
