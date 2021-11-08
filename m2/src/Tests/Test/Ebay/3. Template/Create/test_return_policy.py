from waitings import *
from conftest import *
from m2.data.form.local.ebay.template.ebay_category_data import *
from common_functions import *


@pytest.mark.ebay_policy
@pytest.mark.policies
@pytest.mark.returnpolicy
class TestPolicy():
    def test_return_policy(self, browser):
        browser.get(ebay_policy_url)

        return_policy = wait_element_clickable(".action-toggle", browser)

        add = wait_presence_of_element("#add_policy-return", browser)

        title = browser.find_element(By.ID, "title")
        title.send_keys(return_title)

        marketplace = Select(browser.find_element(By.ID, "marketplace_id"))
        marketplace.select_by_visible_text(return_marketplace)

        button = wait_presence_of_element("#save_and_continue-button", browser)

        # assert browser.find_element(By.CSS_SELECTOR, "[data-ui-id='messages-message-success']"), "Policy wasn't saved"
        # Проверяем, что все значения установлены по умолчанию
        is_element_selected("#return_accepted>[value='ReturnsAccepted']",\
                            "Something wrong with Return Policy", browser)
        is_element_selected("#return_option>[value='MoneyBack']",\
                            "Something wrong with Refund Will Be Given As", browser)
        is_element_selected("#return_within>[value='Days_14']",\
                            "Something wrong with Item Must Be Returned Within", browser)
        is_element_selected("#return_shipping_cost>[value='Buyer']",\
                            "Something wrong with Return Shipping Will Be Paid By", browser)
        is_element_selected("#return_international_accepted>[value='ReturnsNotAccepted']",\
                            "Something wrong with International Returns>Return Policy", browser)

        # Проверяем, что все остальные элементы (в разделе International returns) скрыты
        is_element_invisible("#return_international_option", browser)
        is_element_invisible("#return_international_within", browser)
        is_element_invisible("#return_international_shipping_cost", browser)

        # Выбираем функцию No Returns Accepted
        select_by_value("#return_accepted", "ReturnsNotAccepted", browser)
        button = wait_presence_of_element("#save_and_continue-button", browser)
        try:
            wait_element_clickable("#do_not_show_again", browser)
            time.sleep(0.1)
            wait_presence_of_element(".action-primary", browser)
        except TimeoutException as err:
            pass

        # Проверяем, что все оставшиеся элементы на странице скрыты
        is_element_invisible("#return_option", browser)
        is_element_invisible("#return_within", browser)
        is_element_invisible("#return_shipping_cost", browser)
        is_element_invisible("#return_international_accepted", browser)
        is_element_invisible("#return_international_option", browser)
        is_element_invisible("#return_international_within", browser)
        is_element_invisible("#return_international_shipping_cost", browser)

        # Выбираем Returns accepted для Domestic and International returns
        select_by_value("#return_accepted", "ReturnsAccepted", browser)
        select_by_value("#return_international_accepted", "ReturnsAccepted", browser)
        button = wait_element_clickable("#save_and_continue-button", browser)

        # Проверяем, что изменения сохранились
        is_element_selected("#return_accepted>[value='ReturnsAccepted']", "Changes not saved", browser)
        is_element_selected("#return_international_accepted>[value='ReturnsAccepted']", "Changes not saved",browser)

        # Выбираем другие параметры и проверяем, что изменения сохранились
        select_by_value("#return_option", "MoneyBackOrReplacement", browser)
        select_by_value("#return_within", "Days_30", browser)
        select_by_value("#return_shipping_cost", "Seller", browser)
        select_by_value("#return_international_option", "MoneyBackOrReplacement", browser)
        select_by_value("#return_international_within", "Days_30", browser)
        select_by_value("#return_international_shipping_cost", "Seller", browser)
        button = wait_element_clickable("#save_and_continue-button", browser)

        is_element_selected("#return_option>[value='MoneyBackOrReplacement']", "Changes not saved", browser)
        is_element_selected("#return_within>[value='Days_30']", "Changes not saved", browser)
        is_element_selected("#return_shipping_cost>[value='Seller']", "Changes not saved", browser)
        is_element_selected("#return_international_option>[value='MoneyBackOrReplacement']", "Changes not saved", browser)
        is_element_selected("#return_international_within>[value='Days_30']", "Changes not saved", browser)
        is_element_selected("#return_international_shipping_cost>[value='Seller']", "Changes not saved", browser)








