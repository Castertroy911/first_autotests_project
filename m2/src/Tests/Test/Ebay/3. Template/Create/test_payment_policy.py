from waitings import *
from conftest import *
from m2.data.form.local.ebay.template.ebay_category_data import *
from common_functions import *


@pytest.mark.ebay_policy
@pytest.mark.policies
class TestPolicy():
    def test_payment_policy(self, browser):
        browser.get(ebay_policy_url)

        button = wait_element_clickable(".action-toggle", browser)

        add = browser.find_element(By.ID, "add_policy-payment")
        add.click()

        title = browser.find_element(By.ID, "title")
        title.send_keys(payment_title)

        marketplace = Select(browser.find_element(By.ID, "marketplace_id"))
        marketplace.select_by_visible_text(payment_marketplace)

        managed_payments = wait_presence_of_element("#managed_payments_mode", browser)

        save = wait_presence_of_element("#save_and_continue-button", browser)

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
        managed_payments = wait_presence_of_element("#managed_payments_mode", browser)

        # Выбираем второй метод оплаты
        pay_pal = wait_presence_of_element("#pay_pal_mode", browser)
        email = browser.find_element(By.ID, "pay_pal_email_address")
        email.send_keys(payment_mail)
        immediate_payments = wait_presence_of_element("#pay_pal_immediate_payment", browser)

        # Проверяем, что Дополнительные способы оплаты скрылись
        is_element_invisible("#payment_methods_MOCC", browser)
        is_element_invisible("#payment_methods_PersonalCheck", browser)
        is_element_invisible("#payment_methods_VisaMC", browser)
        is_element_invisible("#payment_methods_AmEx", browser)
        is_element_invisible("#payment_methods_Discover", browser)
        is_element_invisible("#payment_methods_PaymentSeeDescription", browser)
        is_element_invisible("#payment_methods_IntegratedMerchantCreditCard", browser)
        is_element_invisible("#payment_methods_CashOnPickup", browser)

        save = wait_presence_of_element("#save_and_continue-button", browser)
        try:
            check = wait_element_clickable("#do_not_show_again", browser)
            button = wait_presence_of_element(".action-primary", browser)
        except TimeoutException as err:
            pass

        immediate_payments = wait_presence_of_element("#pay_pal_immediate_payment", browser)

        # Проверяем, что Дополнительные способы оплаты снова видны
        assert WebDriverWait(browser, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[name='payment[services][]']"))
        ), "Test Failed"

        # Выбираем все Дополнительные способы оплаты и сохраняем настройки
        money_order = wait_presence_of_element("#payment_methods_MOCC", browser)
        personal_check = wait_presence_of_element("#payment_methods_PersonalCheck", browser)
        visa_mc = wait_presence_of_element("#payment_methods_VisaMC", browser)
        american_exp = wait_presence_of_element("#payment_methods_AmEx", browser)
        discovery_card = wait_presence_of_element("#payment_methods_Discover", browser)
        other = wait_presence_of_element("#payment_methods_PaymentSeeDescription", browser)
        int_merch = wait_presence_of_element("#payment_methods_IntegratedMerchantCreditCard", browser)
        cash_on_pickup = wait_presence_of_element("#payment_methods_CashOnPickup", browser)
        save = wait_presence_of_element("#save_and_continue-button", browser)

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



