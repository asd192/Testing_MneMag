from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators
from datetime import datetime


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """открыть урл"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """перехват исключний, проверка наличия элемента"""
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def go_to_login_page(self):
        """переход в форму авторизации"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_register_page(self):
        """переход на страницу регистрации"""
        link = self.browser.find_element(*BasePageLocators.REGISTER_LINK)
        link.click()

    def should_be_authorized_user(self):
        """проверка, что user залогинен"""
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "Отсутствует значок пользователя. Вероятно, пользователь не залогинен."

    def is_not_element_present(self, how, what, timeout=2):
        """проверяет, что элемент не появляется на странице в течение заданного времени"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=2):
        """проверяет, что какой-то элемент исчезает"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def copyright_checks(self):
        """проверка актуальности года копирайта"""
        assert self.browser.find_element(*BasePageLocators.COPYRIGHT).text[-4:] == str(datetime.now().year), \
            "год копирайта не соответствует текущему"
