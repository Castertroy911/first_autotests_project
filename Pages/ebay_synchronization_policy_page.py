from policies_page import PoliciesPage
from locators import *
from m2.data.form.local.Policies.policies_data import *


class EbaySynchronizationPolicyPage(PoliciesPage):
    def add_synchronization_policy(self):
        self.go_to_policies_page()
        self.add_policy(*PoliciesPageLocators.ADD_SYNCHRONIZATION_POLICY)

    def fill_general_information(self):
        title = self.wait_for_element(*EbaySynchronizationPolicyLocators.TITLE)
        title.send_keys(synchronization_policy_title)

    def list_rules(self):
        self.select_element_by_value("0", *EbaySynchronizationPolicyLocators.LIST_MODE)

    def revise_rules(self):
        self.wait_for_element_and_click(*EbaySynchronizationPolicyLocators.REVISE_TAB)
        self.is_element_selected(*EbaySynchronizationPolicyLocators.REVISE_PRICE)
        self.is_element_deselected(*EbaySynchronizationPolicyLocators.REVISE_TITLE)
        self.is_element_deselected(*EbaySynchronizationPolicyLocators.REVISE_SUBTITLE)
        self.is_element_deselected(*EbaySynchronizationPolicyLocators.REVISE_DESCRIPTION)
        self.is_element_deselected(*EbaySynchronizationPolicyLocators.REVISE_IMAGES)
        self.is_element_deselected(*EbaySynchronizationPolicyLocators.REVISE_CATEGORIES)
        self.is_element_deselected(*EbaySynchronizationPolicyLocators.REVISE_EBAY_PARTS_COMPATIBILITY)
        self.is_element_deselected(*EbaySynchronizationPolicyLocators.REVISE_SHIPPING)
        self.is_element_deselected(*EbaySynchronizationPolicyLocators.REVISE_RETURN)
        self.is_element_deselected(*EbaySynchronizationPolicyLocators.REVISE_OTHER)

    def relist_rules(self):
        self.wait_for_element_and_click(*EbaySynchronizationPolicyLocators.RELIST_TAB)
        self.is_element_selected(*EbaySynchronizationPolicyLocators.RELIST_MODE)

    def stop_rules(self):
        self.wait_for_element_and_click(*EbaySynchronizationPolicyLocators.STOP_TAB)
        self.is_element_selected(*EbaySynchronizationPolicyLocators.STOP_MODE)

    def save_and_continue(self):
        self.wait_for_element_and_click(*EbaySynchronizationPolicyLocators.SAVE_AND_CONTINUE)
        message = self.wait_for_element(*BasePageLocators.SUCCESS_MESSAGE)
        message = message.text()
        assert message == "Policy was saved.", f"Synchronization Policy wasn't saved, but it should be"

    def check_fields_after_saving(self):
        self.is_element_deselected(*EbaySynchronizationPolicyLocators.LIST_MODE_STATUS)
        self.revise_rules()
        self.relist_rules()
        self.stop_rules()

