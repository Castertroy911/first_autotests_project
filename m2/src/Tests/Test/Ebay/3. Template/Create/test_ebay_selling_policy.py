import time

from waitings import *
from conftest import *
from m2.data.form.local.ebay.template.ebay_category_data import *
from common_functions import *


@pytest.mark.ebay_policy
@pytest.mark.policies
class TestPolicy():
    def test_selling_policy(self, browser):
        browser.get(ebay_policy_url)

        wait_element_clickable(".action-toggle", browser)
        wait_presence_of_element("#add_policy-selling", browser)

        title = browser.find_element(By.ID, "title")
        title.send_keys(selling_title)

        # Проверяем, что все поля по умолчанию заполнены
        is_element_selected("#listing_type>[value='2']",
                            "Fixed Price isn't selected by default", browser)
        is_element_selected("#listing_is_private>[value='0']",
                            "No isn't selected bu default in Private Listing", browser)
        is_element_selected("#restricted_to_business>[value='0']",
                            "Disabled isn't selected by default in For business users only", browser)
        is_element_selected("#qty_mode>[value='1']",
                            "Product Quantity isn't selected by default in Quantity", browser)
        is_element_selected("#qty_percentage>[value='100']",
                            "100% isn't selected by default in Quantity Percentage", browser)
        is_element_selected("#qty_modification_mode>[value='0']",
                            "Disabled isn't selected by default for Conditional Quantity", browser)
        is_element_selected("#lot_size_mode>[value='0']",
                            "No isn't selected by default for Specify Lot Size", browser)
        is_element_selected("#ignore_variations_value>[value='0']",
                            "No isn't selected by default for Ignore Variations", browser)
        assert browser.find_element(
            By.CSS_SELECTOR, "#vat_percent").get_attribute("value") == "0", "0 isn't selected by default for VAT Rate, %"
        is_element_selected("#tax_table_mode>[value='0']",
                            "No isn't selected by default for Use eBay Tax Table", browser)
        is_element_selected("#price_increase_vat_percent>[value='0']",
                            "No isn't selected by default for Add VAT Percentage", browser)
        is_element_selected("#fixed_price_mode>[value='1']",
                            "Product Price isn't selected by default for Price", browser)
        is_element_selected("#fixed_price_coefficient_mode>[value='0']",
                            "None isn't selected by default for Price Change", browser)
        is_element_selected("#price_variation_mode>[value='1']",
                            "Main Product isn't selected by default for Variation Price", browser)
        is_element_selected("#price_discount_stp_mode>[value='0']",
                            "None isn't selected by default for Strike-Through Price", browser)
        is_element_selected("#price_discount_map_mode>[value='0']",
                            "None isn't selected by default for Minimum Advertised Price", browser)
        is_element_selected("#best_offer_mode>[value='0']",
                            "No isn't selected by defaul for Allow Best Offer", browser)

        # Выбираем другие параметры и проверяем, что все работает как положено
        select_by_value("#listing_type", "1", browser)
        is_element_invisible("#qty_mode", browser)
        is_element_invisible("#qty_custom_value", browser)
        is_element_invisible("#ignore_variations_value", browser)
        is_element_invisible("#best_offer_mode", browser)
        select_by_value("#listing_type", "2", browser)
        select_by_value("#listing_is_private", "1", browser)
        select_by_value("#restricted_to_business", "1", browser)
        select_by_value("#qty_mode", "1", browser)
        is_element_invisible("#qty_custom_value", browser)
        select_by_value("#qty_mode", "1", browser)
        select_by_value("#qty_percentage", "80", browser)
        select_by_value("#qty_modification_mode", "1", browser)

        min_qty = browser.find_element(By.ID, "qty_min_posted_value")
        min_qty.clear()
        min_qty.send_keys("5")

        max_qty = browser.find_element(By.ID, "qty_max_posted_value")
        max_qty.clear()
        max_qty.send_keys("50")

        select_by_value("#lot_size_mode", "1", browser)
        items_in_lot = browser.find_element(By.ID, "lot_size_custom_value")
        items_in_lot.send_keys("5")

        select_by_value("#ignore_variations_value", "1", browser)

        vat = browser.find_element(By.ID, "vat_percent")
        vat.clear()
        vat.send_keys("10")

        select_by_value("#tax_table_mode", "1", browser)
        select_by_value("#price_increase_vat_percent", "1", browser)
        select_by_value("#fixed_price_mode", "1", browser)
        select_by_value("#price_variation_mode", "2", browser)
        select_by_value("#fixed_price_coefficient_mode", "1", browser)
        abs_value = browser.find_element(By.CSS_SELECTOR, "[name='selling_format[fixed_price_coefficient]']")
        abs_value.send_keys("10")

        select_by_value("#price_discount_stp_mode", "1", browser)
        is_element_selected("[name='selling_format[price_discount_stp_type]']>[value='0']",
                            "Recommended Retail Price isn't selected by the default for Reason (UK, DE only)", browser)
        select_by_value("#price_discount_map_mode", "1", browser)
        is_element_selected("[name='selling_format[price_discount_map_exposure_type]']>[value='0']",
                            "None isn't selected by default for Exposure", browser)
        select_by_value("#best_offer_mode", "1", browser)
        select_by_value("#best_offer_accept_mode", "1", browser)
        select_by_value("#best_offer_reject_mode", "1", browser)

        best_offer_accept = browser.find_element(By.ID, "best_offer_accept_value")
        best_offer_accept.send_keys("95")

        best_offer_reject = browser.find_element(By.ID, "best_offer_reject_value")
        best_offer_reject.send_keys("90")

        # Сохраняем изменения и проверяем, что изменения сохранились
        wait_element_clickable("#save_and_continue-button", browser)
        is_element_selected("#listing_type>[value='2']", "Changes aren't saved", browser)
        is_element_selected("#listing_is_private>[value='1']", "Changes aren't saved", browser)
        is_element_selected("#restricted_to_business>[value='1']", "Changes aren't saved", browser)
        is_element_selected("#qty_mode>[value='1']", "Changes aren't saved", browser)
        is_element_selected("#qty_percentage>[value='80']", "Changes aren't saved", browser)
        is_element_selected("#qty_modification_mode>[value='1']", "Changes aren't saved", browser)
        assert browser.find_element(By.ID, "qty_min_posted_value").get_attribute("value") == "5", "Changes aren't seved"
        assert browser.find_element(By.ID, "qty_max_posted_value").get_attribute("value") == "50", "Changes aren't saved"
        is_element_selected("#lot_size_mode>[value='1']", "Changes aren't saved", browser)
        assert browser.find_element(By.ID, "lot_size_custom_value").get_attribute("value") == "5", "Changes aren't saved"
        is_element_selected("#ignore_variations_value>[value='1']", "Changes aren't saved", browser)
        assert browser.find_element(By.ID, "vat_percent").get_attribute("value") == "10", "Changes aren't saved"
        is_element_selected("#tax_table_mode>[value='1']", "Changes aren't saved", browser)
        is_element_selected("#price_increase_vat_percent>[value='1']", "Changes aren't saved", browser)
        is_element_selected("#fixed_price_mode>[value='1']", "Changes aren't saved", browser)
        is_element_selected("#price_discount_stp_mode>[value='1']", "Changes aren't saved", browser)
        is_element_selected("#fixed_price_coefficient_mode>[value='1']", "Changes aren't saved", browser)
        assert browser.find_element(By.CSS_SELECTOR, "[name='selling_format[fixed_price_coefficient]']"
                                    ).get_attribute("value") == "10", "Changes aren't saved"
        is_element_selected("[name='selling_format[price_discount_stp_type]']>[value='0']", "Changes aren't saved", browser)
        is_element_selected("#price_discount_map_mode>[value='1']", "Changes aren't saved", browser)
        is_element_selected("[name='selling_format[price_discount_map_exposure_type]']>[value='0']", "Changes aren't saved", browser)
        is_element_selected("#best_offer_mode>[value='1']", "Changes aren't saved", browser)
        is_element_selected("#best_offer_accept_mode>[value='1']", "Changes aren't saved", browser)
        is_element_selected("#best_offer_reject_mode>[value='1']", "Changes aren't saved", browser)
        assert browser.find_element(By.ID, "best_offer_accept_value").get_attribute("value") == "95", "Changes aren't saved"
        assert browser.find_element(By.ID, "best_offer_reject_value").get_attribute("value") == "90", "Changes aren't saved"

        # Выбираем еще одни настройки, сохраняем и проверяем, сохранились ли изменения
        select_by_value("#qty_mode", "3", browser)
        quantity_value = browser.find_element(By.ID, "qty_custom_value")
        quantity_value.clear()
        quantity_value.send_keys("10")
        wait_element_clickable("#save_and_continue-button", browser)
        try:
            wait_presence_of_element(".admin__control-checkbox", browser)
            time.sleep(0.1)
            wait_element_clickable(".action-primary", browser)
        except TimeoutException as err:
            pass
        is_element_selected("#qty_mode>[value='3']", "Changes aren't saved", browser)
        assert browser.find_element(By.ID, "qty_custom_value").get_attribute("value") == "10", "Changes aren't saved"
        select_by_value("#listing_type", "1", browser)
        wait_element_clickable("#save_and_continue-button", browser)
        is_element_selected("#duration_mode>[value='3']", "Changes aren't saved", browser)
        is_element_selected("#start_price_mode>[value='1']", "Changes aren't saved", browser)
        is_element_selected("#start_price_coefficient_mode>[value='0']", "Changes aren't saved", browser)
        is_element_selected("#reserve_price_mode>[value='0']", "Changes aren't saved", browser)
        is_element_selected("#buyitnow_price_mode>[value='0']", "Changes aren't saved", browser)
        is_element_invisible("#best_offer_mode", browser)

