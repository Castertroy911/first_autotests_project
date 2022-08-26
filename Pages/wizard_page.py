from selenium.common.exceptions import *
from helper import Helper
from locators import WizardFirstStepLocators, EbayWizardLocators
from m2.data.form.local.Wizard.wizard_data import *


class WizardPage(Helper):
    def wizard_first_step(self):
        try:
            self.wait_for_element_and_click(*WizardFirstStepLocators.OK_BUTTON)
        except TimeoutException:
            pass

        try:
            email = self.browser.find_element(*WizardFirstStepLocators.EMAIL)
            email.clear()
            email.send_keys(email_data)

            first_name = self.browser.find_element(*WizardFirstStepLocators.FIRST_NAME)
            first_name.clear()
            first_name.send_keys(first_name_data)

            last_name = self.browser.find_element(*WizardFirstStepLocators.LAST_NAME)
            last_name.clear()
            last_name.send_keys(last_name_data)

            phone = self.browser.find_element(*WizardFirstStepLocators.PHONE)
            phone.clear()
            phone.send_keys(phone_data)

            country = self.select_element_by_text("United States", *WizardFirstStepLocators.COUNTRY)

            city = self.browser.find_element(*WizardFirstStepLocators.CITY)
            city.clear()
            city.send_keys(city_data)

            postal_code = self.browser.find_element(*WizardFirstStepLocators.POSTAL_CODE)
            postal_code.clear()
            postal_code.send_keys(postal_code_data)

            check = self.browser.find_element(*WizardFirstStepLocators.CHECK)
            check.click()

            continue_button = self.browser.find_element(*WizardFirstStepLocators.CONTINUE)
            continue_button.click()
        except NoSuchElementException:
            pass

    def continue_to_the_next_step(self):
        self.wait_for_element_and_click(*EbayWizardLocators.CONTINUE)

    def skip(self):
        self.wait_for_element_and_click(*EbayWizardLocators.SKIP)
