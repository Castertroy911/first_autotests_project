from waitings import *
from conftest import *
from m2.data.form.local.ebay.template.ebay_category_data import *
from common_functions import *


@pytest.mark.ebay_policy
@pytest.mark.policies
class TestPolicy():
    def test_payment_policy(self, browser):
        browser.get(ebay_policy_url)

        wait_element_clickable(".action-toggle", browser)

        add = browser.find_element(By.ID, "add_policy-payment")
        add.click()

        title = browser.find_element(By.ID, "title")
        title.send_keys(payment_title)

        marketplace = Select(browser.find_element(By.ID, "marketplace_id"))
        marketplace.select_by_visible_text(payment_marketplace)

        wait_presence_of_element("#managed_payments_mode", browser)

        wait_presence_of_element("#save_and_continue-button", browser)

        # Проверяем что первый выбранный метод оплаты сохранился
        is_element_selected("#managed_payments_mode", browser)

        # Проверяем, что все остальные методы оплаты теперь неактивны
        is_element_disabled("#pay_pal_mode", browser)
        is_element_disabled("#pay_pal_immediate_payment", browser)
        is_element_disabled("#payment_methods_MOCC", browser)
        is_element_disabled("#payment_methods_PersonalCheck", browser)
        is_element_disabled("#payment_methods_VisaMC", browser)
        is_element_disabled("#payment_methods_AmEx", browser)
        is_element_disabled("#payment_methods_Discover", browser)
        is_element_disabled("#payment_methods_PaymentSeeDescription", browser)
        is_element_disabled("#payment_methods_IntegratedMerchantCreditCard", browser)
        is_element_disabled("#payment_methods_CashOnPickup", browser)
        wait_presence_of_element("#managed_payments_mode", browser)

        # Выбираем второй метод оплаты
        wait_presence_of_element("#pay_pal_mode", browser)
        email = browser.find_element(By.ID, "pay_pal_email_address")
        email.send_keys(payment_mail)
        wait_presence_of_element("#pay_pal_immediate_payment", browser)

        # Проверяем, что Дополнительные способы оплаты скрылись
        is_element_invisible("#payment_methods_MOCC", browser)
        is_element_invisible("#payment_methods_PersonalCheck", browser)
        is_element_invisible("#payment_methods_VisaMC", browser)
        is_element_invisible("#payment_methods_AmEx", browser)
        is_element_invisible("#payment_methods_Discover", browser)
        is_element_invisible("#payment_methods_PaymentSeeDescription", browser)
        is_element_invisible("#payment_methods_IntegratedMerchantCreditCard", browser)
        is_element_invisible("#payment_methods_CashOnPickup", browser)

        wait_presence_of_element("#save_and_continue-button", browser)
        try:
            wait_element_clickable("#do_not_show_again", browser)
            wait_presence_of_element(".action-primary", browser)
        except TimeoutException as err:
            pass

        wait_presence_of_element("#pay_pal_immediate_payment", browser)

        # Проверяем, что Дополнительные способы оплаты снова видны
        assert WebDriverWait(browser, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[name='payment[services][]']"))
        ), "Test Failed"

        # Выбираем все Дополнительные способы оплаты и сохраняем настройки
        wait_presence_of_element("#payment_methods_MOCC", browser)
        wait_presence_of_element("#payment_methods_PersonalCheck", browser)
        wait_presence_of_element("#payment_methods_VisaMC", browser)
        wait_presence_of_element("#payment_methods_AmEx", browser)
        wait_presence_of_element("#payment_methods_Discover", browser)
        wait_presence_of_element("#payment_methods_PaymentSeeDescription", browser)
        wait_presence_of_element("#payment_methods_IntegratedMerchantCreditCard", browser)
        wait_presence_of_element("#payment_methods_CashOnPickup", browser)
        wait_presence_of_element("#save_and_continue-button", browser)

        # Проверяем, что после сохранения, все выбранные способы оплаты сохранились
        is_element_selected("#pay_pal_mode", browser)
        is_element_selected("#payment_methods_MOCC", browser)
        is_element_selected("#payment_methods_PersonalCheck", browser)
        is_element_selected("#payment_methods_VisaMC", browser)
        is_element_selected("#payment_methods_AmEx", browser)
        is_element_selected("#payment_methods_Discover", browser)
        is_element_selected("#payment_methods_PaymentSeeDescription", browser)
        is_element_selected("#payment_methods_IntegratedMerchantCreditCard", browser)
        is_element_selected("#payment_methods_CashOnPickup", browser)



