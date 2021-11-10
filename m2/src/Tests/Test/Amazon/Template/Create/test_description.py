from selenium.webdriver.chrome.webdriver import WebDriver
from m2.src.Tests.Test.Abstract import Abstract
from waitings import *
from conftest import *
from common_functions import *


@pytest.mark.amazon_policy_description
@pytest.mark.amazon_policies
class TestDescription(Abstract):

    def test_execute(self, browser: WebDriver):
        browser.get('http://m2developm2e.test/admin/m2epro/amazon_template/index/')

        waitForElementClickable('#add_policy', browser).click()
        waitForElementClickable('#add_policy-description', browser).click()

        self.generalFieldset(browser)
        self.categoryFieldset(browser)

        browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        waitForElementClickable("#save_and_continue-button", browser).click()

        message = browser.find_element_by_css_selector(".message-success div").text
        assert "saved" in message

    def generalFieldset(self, browser):
        waitElement('#magento_block_amazon_template_description_general', browser)

        title = browser.find_element(By.ID, 'title')
        title.send_keys('United States' + self.getCurrentTime())

        select = Select(browser.find_element(By.ID, 'marketplace_id'))
        select.select_by_visible_text('United States')

    def categoryFieldset(self, browser):
        waitElement('#magento_block_template_description_edit_category', browser)

        waitForElementClickable('#edit_category_link', browser).click()
        waitForElementClickable('#amazonTemplateDescriptionCategoryChooserTabs_search', browser).click()

        query = browser.find_element(By.ID, 'query')
        query.send_keys('dress')
        browser.find_element(By.ID, 'search').click()

        waitForElementClickable('.search_results_results_tr td:last-child a', browser).click()

        waitElement('#selected_category_path', browser)
        waitForElementClickable('.action-primary', browser).click()
