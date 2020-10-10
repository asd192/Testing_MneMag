# pytest -v --tb=line --browser_name chrome test_main_page.py
import pytest

from .pages.base_page import BasePage
from .pages.main_page import MainPage


link = "https://mnemag.ru/"


class TestsGuest():
    def test_checking_whether_the_authorization_form_is_available(self, browser):
        """проверка исправности формы авторизации для гостей"""
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.checking_guest_whether_the_authorization_form_is_available()

    def test_checking_for_widgets(self, browser):
        """проверка наличия требуемых виджетов"""
        page = MainPage(browser, link)
        page.open()
        page.checking_guest_for_widgets()
        page = BasePage(browser, link)
        page.copyright_checks()
