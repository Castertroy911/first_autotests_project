from Pages.policies_page import PoliciesPage
from locators import EbayReturnPolicyLocators, PoliciesPageLocators
from selenium.common.exceptions import TimeoutException
from m2.data.form.local.Policies.policies_data import *


class EbayReturnPolicyPage(PoliciesPage):
    def add_ebay_return_policy(self):
        try:
            self.add_policy(*PoliciesPageLocators.ADD_RETURN_POLICY)
        except TimeoutException:
            self.add_policy(*PoliciesPageLocators.ADD_RETURN_POLICY)

    def fill_in_general_info(self):
        title = self.wait_for_element(*EbayReturnPolicyLocators.TITLE)
        title.clear()
        title.send_keys(return_policy_title)

        self.select_element_by_text(us_marketplace_return, *EbayReturnPolicyLocators.MARKETPLACE)

    def domestic_returns_block_is_visible(self):
        assert self.is_element_present(*EbayReturnPolicyLocators.DOMESTIC_RETURNS_BLOCK), f"Domestic returns block " \
                                                                                          f"is not present on the page"

    def save_policy(self):
        self.wait_for_element_and_click(*EbayReturnPolicyLocators.SAVE_AND_CONTINUE)
        self.wait_for_text_in_element(f"Policy was saved", *EbayReturnPolicyLocators.SUCCESS_MESSAGE)

    def changes_is_saved(self):
        assert self.is_element_present(*EbayReturnPolicyLocators.DOMESTIC_RETURNS_BLOCK), f"Changes are not saved"
        self.is_element_selected(*EbayReturnPolicyLocators.MARKETPLACE_SELECTED)
