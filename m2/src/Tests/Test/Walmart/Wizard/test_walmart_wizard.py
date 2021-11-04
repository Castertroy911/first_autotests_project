from login_wlm import *
from Credentials.credentials_walmart import *
from selenium.webdriver.support.ui import Select
from conftest import *
from waitings import *


@pytest.mark.wizard
class TestWizard():
    def test_walmart_wizard(self, browser):
        # Начинаем прохождение визарда Walmart
        browser.get("http://10.0.30.122/magento_2/prefix_clear/admin/m2epro/wizard_installationWalmart/")
        try:
            close = wait(".action", browser)
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

            agreement = wait("[value = '1']", browser)

            next_step = wait("#continue", browser)
        except NoSuchElementException as err:
            pass


        # Второй шаг визарда
        marketplace = Select(browser.find_element(By.ID, "marketplace_id"))
        marketplace.select_by_visible_text("United States")

        login_wlm = walmart_log_in(user_id_walmart, user_secret_walmart, browser)

        button = wait("#continue", browser)

        # Третий шаг визарда
        upc = wait("#upc_mode [attribute_code = 'upc']", browser)

        ean = wait("#ean_mode [attribute_code = 'ean']", browser)

        next = wait("#continue", browser)

        # Начинаем создавать первый листинг непосредственно после прохождения визарда
        button = wait("#continue", browser)

        title = browser.find_element(By.ID, "title")
        title.clear()
        title.send_keys("auto_created_listing")

        store_view = Select(browser.find_element(By.ID, "store_id"))
        store_view.select_by_visible_text("Default Config")
        time.sleep(3)

        selling_policy = wait("#add_selling_format_template_link", browser)

        second_window = browser.window_handles[1]
        browser.switch_to.window(second_window)

        title = browser.find_element(By.ID, "title")
        title.send_keys("auto_created_selling_policy")

        prod_tax_code = browser.find_element(By.ID, "product_tax_code_custom_value")
        prod_tax_code.send_keys("2037780")

        weight = browser.find_element(By.ID, "item_weight_custom_value")
        weight.send_keys("15")

        button = wait("#save_and_close-button", browser)

        first_window = browser.window_handles[0]
        browser.switch_to.window(first_window)
        time.sleep(3)

        description_policy = wait("#add_description_template_link", browser)

        second_window = browser.window_handles[1]
        browser.switch_to.window(second_window)

        title = browser.find_element(By.ID, "title")
        title.send_keys("auto_created_description_policy")

        brand = browser.find_element(By.ID, "brand_custom_value")
        brand.send_keys("Unbranded")

        button = wait("#save_and_close-button", browser)

        first_window = browser.window_handles[0]
        browser.switch_to.window(first_window)
        time.sleep(3)

        synchronization_policy = wait("#add_synchronization_template_link", browser)

        second_window = browser.window_handles[1]
        browser.switch_to.window(second_window)

        title = browser.find_element(By.ID, "title")
        title.send_keys("auto_created_synchronization_policy")

        button = wait("#save_and_close-button", browser)

        first_window = browser.window_handles[0]
        browser.switch_to.window(first_window)
        time.sleep(3)

        button = wait("#save_and_next", browser)

        button = wait("#next", browser)

        sort = wait("[data-sort = 'product_id']", browser)

        simple_prod = wait(".admin__control-checkbox[value='1']", browser)

        button = wait("#add_products_mode_product_continue", browser)

        edit = wait("#edit_category_template", browser)

        category_policy = wait("#template_category_addNew_link", browser)

        second_window = browser.window_handles[1]
        browser.switch_to.window(second_window)

        title = browser.find_element(By.ID, "title")
        title.send_keys("auto_created_category_policy")

        category = wait("#edit_category_link", browser)
        time.sleep(3)

        search = wait("#walmartTemplateCategoryCategoriesChooserTabs_search", browser)

        category = browser.find_element(By.ID, "query")
        category.send_keys("284435000000")

        find_category = wait("#chooser_search_input_container .primary", browser)

        select = wait(".search_results_results_tr a", browser)

        button = wait(".action-primary.walmart_template_category_chooser_confirm", browser)

        button = wait("#save_and_close-button", browser)

        first_window = browser.window_handles[0]
        browser.switch_to.window(first_window)
        time.sleep(3)

        assign = browser.find_element(By.LINK_TEXT, "Assign")
        assign.click()

        button = wait("#next", browser)

        assert browser.find_element(By.CLASS_NAME, "page-title").text == "Congratulations", "Test Failed"
