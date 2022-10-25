from Pages.ebay_return_policy_page import EbayReturnPolicyPage


class TestEbayReturnPolicy:
    def test_ebay_return_policy(self, browser):
        page = EbayReturnPolicyPage(browser, browser.current_url)
        page.open_ebay_tab()
        page.go_to_ebay_policies_page()
        page.add_ebay_return_policy()
        page.fill_in_general_info()
        page.domestic_returns_block_is_visible()
        page.save_policy()
        page.changes_is_saved()