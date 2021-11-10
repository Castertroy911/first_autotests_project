from conftest import *
from m2.config.local_config import *
from common_functions import *


@pytest.mark.ebay_marketplaces
class TestMarketplaces():
    def test_marketplaces_update(self, browser):
        browser.get("http://" + VM_IP + "/magento_2/prefix_clear/admin/m2epro/ebay_marketplace/index/")

        select_by_value("#status_1", "1", browser)
        select_by_value("#status_2", "1", browser)
        select_by_value("#status_19", "1", browser)
        select_by_value("#status_3", "1", browser)
        select_by_value("#status_8", "1", browser)
        select_by_value("#status_5", "1", browser)
        select_by_value("#status_11", "1", browser)
        select_by_value("#status_6", "1", browser)
        select_by_value("#status_7", "1", browser)
        select_by_value("#status_17", "1", browser)
        select_by_value("#status_10", "1", browser)
        select_by_value("#status_12", "1", browser)
        select_by_value("#status_21", "1", browser)
        select_by_value("#status_13", "1", browser)
        select_by_value("#status_14", "1", browser)
        select_by_value("#status_4", "1", browser)
        select_by_value("#status_15", "1", browser)
        select_by_value("#status_16", "1", browser)
        select_by_value("#status_18", "1", browser)
        select_by_value("#status_20", "1", browser)
        select_by_value("#status_22", "1", browser)
        select_by_value("#status_9", "1", browser)

        save = browser.find_element(By.ID, "run_save_and_synch")
        save.click()
        a = WebDriverWait(browser, 99999).until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, "[data-ui-id='messages-message-success']"), "Marketplace synchronization was completed."))
