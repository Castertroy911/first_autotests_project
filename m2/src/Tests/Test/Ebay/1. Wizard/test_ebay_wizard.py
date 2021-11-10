from login_ebay import *
from Credentials.credentials_ebay import  *
from selenium.webdriver.support.ui import Select
from conftest import *
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.wizard
class TestWizard():
    def test_ebay_wizard(self, browser):
        browser.get("http://" + VM_IP + "/magento_2/prefix_clear/admin/m2epro/wizard_installationEbay/")
        try:
            wait_presence_of_element(".action", browser)
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

            wait_presence_of_element("[value = '1']", browser)

            wait_presence_of_element("#continue", browser)
        except NoSuchElementException as err:
            pass

        # Второй шаг визарда
        wait_presence_of_element("#modesandbox", browser)

        wait_presence_of_element("#continue", browser)

        ebay_log_in(user_id_ebay, user_secret_ebay, browser)

        wait_presence_of_element("#skip", browser)

