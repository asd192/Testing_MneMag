# pytest -v --tb=line --browser_name chrome test_main_page.py
# pytest -s -v --tb=line --browser_name=firefox test_main_page.py
import pytest
import time

from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_regiser_pages import LoginRegisterPage

link = "https://mnemag.ru/"


@pytest.mark.guest
class TestGuest():
    def test_guest_checking_whether_the_authorization_form_is_available(self, browser):
        """проверка исправности формы авторизации для гостей"""
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.checking_guest_whether_the_authorization_form_is_available()

    def test_guest_checking_for_widgets(self, browser):
        """проверка наличия требуемых виджетов"""
        page = MainPage(browser, link)
        page.open()
        page.checking_guest_for_widgets()
        page = BasePage(browser, link)
        page.copyright_checks()


@pytest.mark.user
class TestUser():
    @pytest.mark.register
    def test_registration_of_user(self, browser):
        """регистрация нового пользователя с главной страницы"""
        page = LoginRegisterPage(browser, link)
        page.open()
        page.go_to_register_page()
        page.register_user()

        time.sleep(5)
