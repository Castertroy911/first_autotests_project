from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from selenium.webdriver.support.select import Select


class Helper(BasePage):
    def __init__(self, *args, **kwargs):
        super(Helper, self).__init__(*args, **kwargs)

    def wait_for_element_and_click(self, method, selector, timeout=5):
        element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, selector)))
        element.click()

    def wait_for_element(self, method, selector, timeout=5):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, selector)))

    def select_element_by_text(self, text, method, selector):
        element = Select(self.browser.find_element(method, selector))
        element.select_by_visible_text(text)
