from login_wlm import *
from Credentials.credentials_walmart import *
from conftest import *
from waitings import *


@pytest.mark.wizard
@pytest.mark.walmart_wizard
class TestWizard():
    def test_walmart_wizard(self, browser):
        # Начинаем прохождение визарда Walmart
        browser.get("http://" + VM_IP + "/magento_2/prefix_clear/admin/m2epro/wizard_installationWalmart/")
        try:
            wait_presence_of_element(".action", browser)
        except TimeoutException as err:
            pass

        try:
            # Первый шаг визарда
            email = browser.find_element(By.CSS_SELECTOR, "#form_email")
            email.clear()
            email.send_keys("admin@admin.com")

            first_name = browser.find_element(By.CSS_SELECTOR, "#first_name")
            first_name.clear()
            first_name.send_keys("admin")

            last_name = browser.find_element(By.CSS_SELECTOR, "#last_name")
            last_name.clear()
            last_name.send_keys("admin")

            phone = browser.find_element(By.CSS_SELECTOR, "#phone")
            phone.clear()
            phone.send_keys("+1231234567")

            country = Select(browser.find_element(By.ID, "country"))
            country.select_by_visible_text("United States")

            city = browser.find_element(By.CSS_SELECTOR, "#city")
            city.clear()
            city.send_keys("city")

            postal_code = browser.find_element(By.CSS_SELECTOR, "#postal_code")
            postal_code.clear()
            postal_code.send_keys("90034")

            wait_presence_of_element("[value = '1']", browser)

            wait_presence_of_element("#continue", browser)
        except NoSuchElementException as err:
            pass


        # Второй шаг визарда
        marketplace = Select(browser.find_element(By.ID, "marketplace_id"))
        marketplace.select_by_visible_text("United States")

        walmart_log_in(user_id_walmart, user_secret_walmart, browser)

        wait_presence_of_element("#continue", browser)

        # Третий шаг визарда
        wait_presence_of_element("#upc_mode [attribute_code = 'upc']", browser)

        wait_presence_of_element("#ean_mode [attribute_code = 'ean']", browser)
        time.sleep(1)

        wait_presence_of_element("#continue", browser)

        wait_presence_of_element("#skip", browser)
