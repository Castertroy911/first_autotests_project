import time

from helper import Helper
from locators import *


class EbayMarketplaceUpdatePage(Helper):
    def go_to_ebay_marketplaces_page(self):
        marketplaces_page = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.MARKETPLACES_PAGE)
        marketplaces_page.click()

    def update_us_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.UNITED_STATES)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.UNITED_STATES_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        time.sleep(1)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"United States marketplace isn't updated"

    def update_canada_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.CANADA)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.CANADA_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Canada marketplace isn't updated"

    def update_canada_french_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.CANADA_FRENCH)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.CANADA_FRENCH_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Canada(French) marketplace isn't updated"

    def update_uk_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.UNITED_KINGDOM)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.UNITED_KINGDOM_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"United Kingdom marketplace isn't updated"

    def update_germany_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.GERMANY)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.GERMANY_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Germany marketplace isn't updated"

    def update_austria_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.AUSTRIA)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.AUSTRIA_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Austria marketplace isn't updated"

    def update_belgium_dutch_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.BELGIUM_DUTCH)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.BELGIUM_DUTCH_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Belgium(Dutch) marketplace isn't updated"

    def update_belgium_french_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.BELGIUM_FRENCH)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.BELGIUM_FRENCH_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Belgium(French) marketplace isn't updated"

    def update_france_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.FRANCE)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.FRANCE_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"France marketplace isn't updated"

    def update_ireland_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.IRELAND)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.IRELAND_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Ireland marketplace isn't updated"

    def update_italy_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.ITALY)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.ITALY_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Italy marketplace isn't updated"

    def update_netherlands_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.NETHERLANDS)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.NETHERLANDS_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Netherlands marketplace isn't updated"

    def update_poland_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.POLAND)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.POLAND_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Poland marketplace isn't updated"

    def update_spain_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.SPAIN)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.SPAIN_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Spain marketplace isn't updated"

    def update_switzerland_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.SWITZERLAND)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.SWITZERLAND_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Switzerland marketplace isn't updated"

    def update_australia_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.AUSTRALIA)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.AUSTRALIA_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Australia marketplace isn't updated"

    def update_hong_kong_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.HONG_KONG)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.HONG_KONG_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Hong Kong marketplace isn't updated"

    def update_india_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.INDIA)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.INDIA_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"India marketplace isn't updated"

    def update_malaysia_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.MALAYSIA)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.MALAYSIA_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Malaysia marketplace isn't updated"

    def update_philippines_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.PHILIPPINES)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.PHILIPPINES_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Philippines marketplace isn't updated"

    def update_singapore_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.SINGAPORE)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.SINGAPORE_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Singapore marketplace isn't updated"

    def update_ebay_motors_marketplace(self):
        self.select_element_by_value("1", *EbayMarketplaceUpdatePageLocators.EBAY_MOTORS)
        self.is_element_selected(*EbayMarketplaceUpdatePageLocators.EBAY_MOTORS_ENABLED)
        save = self.browser.find_element(*EbayMarketplaceUpdatePageLocators.SAVE)
        save.click()
        self.visibility_of_element(*BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        self.wait_for_text_in_element("100", *BasePageLocators.PROGRESS_BAR_PERCENTAGE)
        result = self.wait_for_element(*EbayMarketplaceUpdatePageLocators.SYNCHRONIZATION_COMPLETED)
        result = result.text
        assert result == "Marketplace synchronization was completed.", f"Ebay Motors marketplace isn't updated"
