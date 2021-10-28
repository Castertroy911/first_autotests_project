import time
from selenium.common.exceptions import NoSuchElementException
from log_in import *
from Credentials.credentials_magento import *
from Credentials.credentials_walmart import *
from selenium.webdriver.support.ui import Select

class TestWizard():
    def test_walmart_wizard(self):
        try:
            # Авторизуемся в мадженте
            login = magento_log_in(user_name, user_password)
            time.sleep(3)

            # Начинаем прохождение визарда Walmart
            wlm = browser.find_element(By.XPATH, "// nav/ul[1]/li[7]/a")
            wlm.click()
            try:
                close = wait(".action")
            except NoSuchElementException as err:
                pass

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

            country = browser.find_element(By.CSS_SELECTOR, "#country")
            country.click()
            us = browser.find_element(By.CSS_SELECTOR, "[value = 'US']")
            us.click()

            browser.find_element(By.CSS_SELECTOR, "#city").clear()
            city = browser.find_element(By.CSS_SELECTOR, "#city")
            city.send_keys("city")

            browser.find_element(By.CSS_SELECTOR, "#postal_code").clear()
            postal_code = browser.find_element(By.CSS_SELECTOR, "#postal_code")
            postal_code.send_keys("city")

            agreement = wait("[value = '1']")

            next_step = wait("#continue")

            # # Второй шаг визарда
            marketplace = wait("#marketplace_id")

            US = wait("[value = '37']")

            login_wlm = walmart_log_in(user_id, user_secret)

            button = wait("#continue")

            # Третий шаг визарда
            upc = wait("#upc_mode [attribute_code = 'upc']")

            ean = wait("#ean_mode [attribute_code = 'ean']")

            next = wait("#continue")

            #Начинаем создавать первый листинг непосредственно после прохождения визарда
            button = wait("#continue")


            title = browser.find_element(By.ID, "title")
            title.clear()
            title.send_keys("auto_created_listing")

            store_view = Select(browser.find_element(By.ID, "store_id"))
            store_view.select_by_visible_text("Default Config")
            time.sleep(3)

            selling_policy = wait("#add_selling_format_template_link")

            second_window = browser.window_handles[1]
            browser.switch_to.window(second_window)

            title = browser.find_element(By.ID, "title")
            title.send_keys("auto_created_selling_policy")

            prod_tax_code = browser.find_element(By.ID, "product_tax_code_custom_value")
            prod_tax_code.send_keys("2037780")

            weight = browser.find_element(By.ID, "item_weight_custom_value")
            weight.send_keys("15")

            button = wait("#save_and_close-button")

            first_window = browser.window_handles[0]
            browser.switch_to.window(first_window)
            time.sleep(3)

            description_policy = wait("#add_description_template_link")

            second_window = browser.window_handles[1]
            browser.switch_to.window(second_window)

            title = browser.find_element(By.ID, "title")
            title.send_keys("auto_created_description_policy")

            brand = browser.find_element(By.ID, "brand_custom_value")
            brand.send_keys("Unbranded")

            button = wait("#save_and_close-button")

            first_window = browser.window_handles[0]
            browser.switch_to.window(first_window)
            time.sleep(3)

            synchronization_policy = wait("#add_synchronization_template_link")

            second_window = browser.window_handles[1]
            browser.switch_to.window(second_window)

            title = browser.find_element(By.ID, "title")
            title.send_keys("auto_created_synchronization_policy")

            button = wait("#save_and_close-button")

            first_window = browser.window_handles[0]
            browser.switch_to.window(first_window)
            time.sleep(3)

            button = wait("#save_and_next")

            button = wait("#next")

            sort = wait("[data-sort = 'product_id']")

            simple_prod = wait(".admin__control-checkbox[value='1']")

            button = wait("#add_products_mode_product_continue")

            edit = wait("#edit_category_template")

            category_policy = wait("#template_category_addNew_link")

            second_window = browser.window_handles[1]
            browser.switch_to.window(second_window)

            title = browser.find_element(By.ID, "title")
            title.send_keys("auto_created_category_policy")

            category = wait("#edit_category_link")
            time.sleep(3)

            search = wait("#walmartTemplateCategoryCategoriesChooserTabs_search")

            category = browser.find_element(By.ID, "query")
            category.send_keys("284435000000")

            find_category = wait("#chooser_search_input_container .primary")

            select = wait(".search_results_results_tr a")

            button = wait(".action-primary.walmart_template_category_chooser_confirm")

            button = wait("#save_and_close-button")

            first_window = browser.window_handles[0]
            browser.switch_to.window(first_window)
            time.sleep(3)

            assign = browser.find_element(By.LINK_TEXT, "Assign")
            assign.click()

            button = wait("#next")

            assert browser.find_element(By.CLASS_NAME, "page-title").text == "Congratulations", "Test Failed"
        finally:
            browser.quit()
