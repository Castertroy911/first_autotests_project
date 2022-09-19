from Pages.ebay_synchronization_policy_page import EbaySynchronizationPolicyPage
import pytest


@pytest.mark.ebay_synchronization_policy
class TestEbaySynchronizationPolicy:
    def test_ebay_synchronization_policy(self, browser):
        page = EbaySynchronizationPolicyPage(browser, browser.current_url)
        page.open_ebay_tab()
        page.go_to_policies_page()
        page.add_synchronization_policy()
        page.fill_general_information()
        page.list_rules()
        page.revise_rules()
        page.relist_rules()
        page.stop_rules()
        page.save_and_continue()
        page.check_fields_after_saving()