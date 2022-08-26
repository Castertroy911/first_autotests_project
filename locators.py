from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_NAME = (By.CSS_SELECTOR, "#username")
    USER_PASSWORD = (By.CSS_SELECTOR, "#login")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, ".action-login")


class BasePageLocators:
    EBAY_LINK = (By.CSS_SELECTOR, "#menu-ess-m2epro-ebay>a")
    AMAZON_LINK = (By.CSS_SELECTOR, "#menu-ess-m2epro-amazon>a")
    WALMART_LINK = (By.CSS_SELECTOR, "#menu-ess-m2epro-walmart>a")


class WizardFirstStepLocators:
    OK_BUTTON = (By.CSS_SELECTOR, ".action.primary")
    EMAIL = (By.CSS_SELECTOR, "#form_email")
    FIRST_NAME = (By.CSS_SELECTOR, "#first_name")
    LAST_NAME = (By.CSS_SELECTOR, "#last_name")
    PHONE = (By.CSS_SELECTOR, "#phone")
    COUNTRY = (By.CSS_SELECTOR, "#country")
    CITY = (By.CSS_SELECTOR, "#city")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal_code")
    CHECK = (By.CSS_SELECTOR, "#licence_agreement")
    CONTINUE = (By.CSS_SELECTOR, "#continue")


class EbayWizardLocators:
    SANDBOX_MODE = (By.CSS_SELECTOR, "#modesandbox")
    CONTINUE = (By.CSS_SELECTOR, "#continue")
    EBAY_USERNAME = (By.CSS_SELECTOR, "#userid")
    EBAY_PASSWORD = (By.CSS_SELECTOR, "#pass")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#sgnBt")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
    UPC = (By.CSS_SELECTOR, "#product_identifier_upc")
    EAN = (By.CSS_SELECTOR, "#product_identifier_ean")
    LABEL = (By.CSS_SELECTOR, "#store_label")
    CODE = (By.CSS_SELECTOR, "#code")
    CONFIRM = (By.CSS_SELECTOR, ".action.primary")
    SKIP = (By.CSS_SELECTOR, "#skip")
    NEXT_STEP = (By.CSS_SELECTOR, "#signin-continue-btn")

