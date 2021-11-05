from login_ebay import *
from Credentials.credentials_ebay import  *
from selenium.webdriver.support.ui import Select
from conftest import *
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.wizard
class TestWizard():
    def test_ebay_wizard(self, browser):
        ebay = browser.get("http://" + VM_IP + "/magento_2/prefix_clear/admin/m2epro/wizard_installationEbay/")
        try:
            close = wait(".action", browser)
        except TimeoutException as err:
            pass

        # Первый шаг визарда
        try:
            email = browser.find_element(By.ID, "form_email")
            email.clear()
            email.send_keys("admin@admin.com")

            first_name = browser.find_element(By.ID, "first_name")
            first_name.clear()
            first_name.send_keys("admin")

            last_name = browser.find_element(By.ID, "last_name")
            last_name.clear()
            last_name.send_keys("admin")

            phone = browser.find_element(By.ID, "phone")
            phone.clear()
            phone.send_keys("1231234567")

            country = Select(browser.find_element(By.ID, "country"))
            country.select_by_visible_text("United States")

            city = browser.find_element(By.ID, "city")
            city.send_keys("city")

            postal_code = browser.find_element(By.ID, "postal_code")
            postal_code.clear()
            postal_code.send_keys("90034")

            agreement = wait("[value = '1']", browser)

            next_step = wait("#continue", browser)
        except NoSuchElementException as err:
            pass

        # Второй шаг визарда
        account = wait("#modesandbox", browser)

        button = wait("#continue", browser)

        login = ebay_log_in(user_id_ebay, user_secret_ebay, browser)

        # Третий шаг визарда
        upc = Select(browser.find_element(By.ID, "product_identifier_upc"))
        upc.select_by_visible_text("UPC")

        ean = Select(browser.find_element(By.ID, "product_identifier_ean"))
        ean.select_by_visible_text("EAN")

        button = wait("#continue", browser)

        skip = wait("#skip", browser)

