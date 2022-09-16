from Pages.policies_page import PoliciesPage
from locators import *
from m2.data.form.local.Policies.policies_data import *
from selenium.common.exceptions import *


class EbayShippingPolicyPage(PoliciesPage):
    policy_title = shipping_policy_title

    def only_general_tab_is_visible(self):
        item_location_tab = self.is_element_present(*EbayShippingPolicyLocators.ITEM_LOCATION_TAB)
        assert item_location_tab is False, f"All tabs are visible before selecting a Marketplace, but it shouldn't"

    def add_shipping_policy(self):
        try:
            self.add_policy(*PoliciesPageLocators.ADD_BUTTON, *PoliciesPageLocators.ADD_SHIPPING_POLICY)
        except TimeoutException:
            self.add_policy(*PoliciesPageLocators.ADD_BUTTON, *PoliciesPageLocators.ADD_SHIPPING_POLICY)

    def fill_in_general_information(self):
        title = self.wait_for_element(*EbayShippingPolicyLocators.TITLE)
        title.send_keys(self.policy_title)

        self.select_element_by_text(us_marketplace, *EbayShippingPolicyLocators.US_MARKETPLACE)

        item_location_tab = self.is_element_present(*EbayShippingPolicyLocators.ITEM_LOCATION_TAB)
        assert item_location_tab is True, f"All tabs aren't visible after selecting Marketplace, but is should be"

    def add_shipping_method(self):
        self.wait_for_element_and_click(*EbayShippingPolicyLocators.ADD_SHIPPING_METHOD_BUTTON)
        self.select_element_by_text(shipping_service, *EbayShippingPolicyLocators.SHIPPING_SERVICE)
        self.select_element_by_value("1", *EbayShippingPolicyLocators.COST_MODE)
        cost = self.browser.find_element(*EbayShippingPolicyLocators.COST)
        cost.clear()
        cost.send_keys(cost_value)
        additional_cost = self.browser.find_element(*EbayShippingPolicyLocators.ADDITIONAL_COST)
        additional_cost.clear()
        additional_cost.send_keys(additional_cost_value)
        priority = self.browser.find_element(*EbayShippingPolicyLocators.PRIORITY)
        priority.clear()
        priority.send_keys(priority_value)
        text = self.text_present_in_attribute("style", *EbayShippingPolicyLocators.COST_MODE)
        assert "none" not in text, "Mode isn't active for user"

    def save_and_continue(self):
        self.wait_for_element_and_click(*EbayShippingPolicyLocators.SAVE_AND_CONTINUE_BUTTON)
        success_message = self.wait_for_element(*BasePageLocators.SUCCESS_MESSAGE)
        success_message = success_message.text
        assert success_message == "Policy was saved.", f"Policy wasn't saved successfully"

    def check_fields_after_saving(self):
        title = self.text_present_in_attribute("value", *EbayShippingPolicyLocators.TITLE)
        assert title == self.policy_title, f"Title saved incorrect"

        selected_marketplace = self.browser.find_element(*EbayShippingPolicyLocators.SELECTED_MARKETPLACE)
        assert selected_marketplace.get_attribute("selected") is not None, f"{us_marketplace} marketplace isn't selected"
