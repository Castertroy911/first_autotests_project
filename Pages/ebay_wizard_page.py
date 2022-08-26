from selenium.common.exceptions import *
from Pages.wizard_page import WizardPage
from locators import EbayWizardLocators
from Credentials.credentials_ebay import *


class EbayWizardPage(WizardPage):
    def second_wizard_step(self):
        mode = self.wait_for_element_and_click(*EbayWizardLocators.SANDBOX_MODE)

        continue_button = self.browser.find_element(*EbayWizardLocators.CONTINUE)
        continue_button.click()

    def login_to_ebay(self):
        self.wait_for_element(*EbayWizardLocators.EBAY_USERNAME)
        user_name = self.browser.find_element(*EbayWizardLocators.EBAY_USERNAME)
        user_name.send_keys(user_id_ebay)

        next_step = self.browser.find_element(*EbayWizardLocators.NEXT_STEP)
        next_step.click()

        user_password = self.browser.find_element(*EbayWizardLocators.EBAY_PASSWORD)
        user_password.send_keys(user_secret_ebay)

        sign_in_button = self.browser.find_element(*EbayWizardLocators.SIGN_IN_BUTTON)
        sign_in_button.click()

        submit_button = self.browser.find_element(*EbayWizardLocators.SUBMIT_BUTTON)
        submit_button.click()

    def select_identifier(self, identifier, selector, element):
        try:
            self.select_element_by_text(identifier, selector, element)
        except NoSuchElementException:
            self.select_element_by_text("Create a New One...", selector, element)

            label = self.wait_for_element(*EbayWizardLocators.LABEL)
            label.send_keys(identifier)

            code = self.browser.find_element(*EbayWizardLocators.CODE)
            code.send_keys(identifier)

            confirm = self.browser.find_element(*EbayWizardLocators.CONFIRM)
            confirm.click()
