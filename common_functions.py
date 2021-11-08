from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Часто используемые функции в проекте


# Помагает быстро выбрать нужный элемент из выпадающего списка
def select_by_value(selector, value, browser):
    sel = Select(browser.find_element(By.CSS_SELECTOR, selector))
    sel.select_by_value(value)


# Помагает быстро проверить, выбран ли элемент (стоит ли возле него галочка)
def is_element_checked(selector, browser):
    assert browser.find_element(
        By.CSS_SELECTOR, selector).get_attribute("checked"), "Test Failed"


# Позволяет быстро проверить, что элемент имеет статус disabled и не может быть выбран пользователем
def is_element_disabled(selector, browser):
    assert browser.find_element(
        By.CSS_SELECTOR, selector).get_attribute("disabled"), "Test Failed"


# Позволяет быстро проверить, выбрано ли в дроп-дауне значение по умолчанию
def is_element_selected(selector, message, browser):
    assert browser.find_element(By.CSS_SELECTOR, selector).get_attribute("selected"), message


# Позволяет быстро проверить, скрыт ли сейчас элемент на странице
def is_element_invisible(selector, browser):
    assert WebDriverWait(browser, 10).until(
        EC.invisibility_of_element((By.CSS_SELECTOR, selector))), "Test Failed"


