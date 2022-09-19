import pytest
from Pages.ebay_shipping_policy_page import EbayShippingPolicyPage


@pytest.mark.ebay_policies
class TestEbayShippingPolicy:
    def test_ebay_shipping_policy(self, browser):
        page = EbayShippingPolicyPage(browser, browser.current_url)
        page.open_ebay_tab()
        page.go_to_policies_page()
        page.add_shipping_policy()
        page.only_general_tab_is_visible()
        page.fill_in_general_information()
        page.add_shipping_method()
        page.save_and_continue()
        page.check_fields_after_saving()
