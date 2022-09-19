from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *


class Helper(BasePage):
    def __init__(self, *args, **kwargs):
        super(Helper, self).__init__(*args, **kwargs)

    def wait_for_element_and_click(self, method, selector, timeout=5):
        element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, selector)))
        element.click()

    def wait_for_element(self, method, selector, timeout=5):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, selector)))

    def wait_for_text_in_element(self, text, method, selector, timeout=300):
        return WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element((method, selector), text))

    def visibility_of_element(self, method, selector, timeout=5):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((method, selector)))

    def select_element_by_text(self, text, method, selector):
        try:
            element = Select(self.browser.find_element(method, selector))
            element.select_by_visible_text(text)
        except NoSuchElementException:
            assert NoSuchElementException is False, f"Element with a text {text} is not enabled for selecting"

    def select_element_by_value(self, value, method, selector):
        try:
            element = Select(self.browser.find_element(method, selector))
            element.select_by_value(value)
        except NoSuchElementException:
            assert NoSuchElementException is False, f"Element with a value {value} is not enabled for selecting"

    def is_element_selected(self, method, selector):
        assert self.browser.find_element(method, selector).get_attribute("selected"), "Element isn't selected, but it" \
                                                                                      " should be"

    def is_element_deselected(self, method, selector):
        assert self.browser.find_element(method, selector).get_attribute("selected") is None, "Element is selected, " \
                                                                                              "but is shouldn't be"

    def is_element_present(self, method, selector):
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return False
        return True

    def text_present_in_attribute(self, attribute_name, method, selector):
        return self.browser.find_element(method, selector).get_attribute(attribute_name)


