from Pages.ebay_marketplace_update_page import EbayMarketplaceUpdatePage
import pytest


@pytest.mark.ebay_marketplaces
class TestEbayMarketplacesUpdate:
    def test_us_marketplaces_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.user_can_go_to_ebay()
        page.go_to_ebay_marketplaces_page()
        page.update_us_marketplace()

    def test_canada_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_canada_marketplace()

    def test_canada_french_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_canada_french_marketplace()

    def test_uk_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_uk_marketplace()

    def test_germany_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_germany_marketplace()

    def test_austria_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_austria_marketplace()

    def test_belgium_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_belgium_dutch_marketplace()

    def test_belgium_french_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_belgium_french_marketplace()

    def test_france_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_france_marketplace()

    def test_ireland_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_ireland_marketplace()

    def test_italy_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_italy_marketplace()

    def test_netherlands_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_netherlands_marketplace()

    def test_poland_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_poland_marketplace()

    def test_spain_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_spain_marketplace()

    def test_switzerland_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_switzerland_marketplace()

    def test_australia_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_australia_marketplace()

    def test_hong_kong_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_hong_kong_marketplace()

    def test_india_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_india_marketplace()

    def test_malaysia_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_malaysia_marketplace()

    def test_philippines_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_philippines_marketplace()

    def test_singapore_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_singapore_marketplace()

    def test_ebay_motors_marketplace_update(self, browser):
        page = EbayMarketplaceUpdatePage(browser, browser.current_url)
        page.update_ebay_motors_marketplace()
