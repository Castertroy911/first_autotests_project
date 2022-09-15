from locators import BasePageLocators
import pytest


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(5)

    def open(self):
        self.browser.get(self.url)

    def user_go_to_ebay(self):
        ebay = self.browser.find_element(*BasePageLocators.EBAY_LINK)
        ebay.click()

    def user_go_to_policies_page(self):
        policies = self.browser.find_element(*BasePageLocators.EBAY_POLICIES_PAGE)
        policies.click()

    def user_can_go_to_amazon(self):
        amazon = self.browser.find_element(*BasePageLocators.AMAZON_LINK)
        amazon.click()

    def user_can_go_to_walmart(self):
        walmart = self.browser.find_element(*BasePageLocators.WALMART_LINK)
        walmart.click()
