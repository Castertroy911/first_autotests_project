from locators import BasePageLocators
import pytest


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(5)

    def open(self):
        self.browser.get(self.url)

    def open_ebay_tab(self):
        ebay = self.browser.find_element(*BasePageLocators.EBAY_LINK)
        ebay.click()

    def go_to_ebay_policies_page(self):
        policies = self.browser.find_element(*BasePageLocators.EBAY_POLICIES_PAGE)
        policies.click()

    def open_amazon_tab(self):
        amazon = self.browser.find_element(*BasePageLocators.AMAZON_LINK)
        amazon.click()

    def open_walmart_tab(self):
        walmart = self.browser.find_element(*BasePageLocators.WALMART_LINK)
        walmart.click()
