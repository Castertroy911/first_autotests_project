import pytest
from Pages.ebay_wizard_page import EbayWizardPage
from locators import EbayWizardLocators


@pytest.mark.test_ebay_wizard1
class TestWizardEbay:
    def test_first_wizard_step_ebay(self, browser):
        page = EbayWizardPage(browser, browser.current_url)
        page.user_go_to_ebay()
        page.wizard_first_step()

    def test_second_wizard_step_ebay(self, browser):
        page = EbayWizardPage(browser, browser.current_url)
        page.second_wizard_step()
        page.login_to_ebay()

    def test_third_wizard_step_ebay(self, browser):
        page = EbayWizardPage(browser, browser.current_url)
        page.select_identifier("UPC", *EbayWizardLocators.UPC)
        page.select_identifier("EAN", *EbayWizardLocators.EAN)
        page.continue_to_the_next_step()

    def test_fourth_wizard_step_ebay(self, browser):
        page = EbayWizardPage(browser, browser.current_url)
        page.skip()
