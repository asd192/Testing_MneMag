from .base_page import BasePage
from .locators import BasePageLocators
from .locators import MainPageLocators


class MainPage(BasePage):
    def checking_guest_whether_the_authorization_form_is_available(self):
        """проверка полей в форме авторизации"""
        assert self.is_element_present(*BasePageLocators.LOGIN_EMAIL),\
            "В форме авторизации отсутствует поле email"
        assert self.is_element_present(*BasePageLocators.LOGIN_PASSWORD), \
            "В форме авторизации отсутствует поле ввода пароля"

    def checking_guest_for_widgets(self):
        assert self.is_element_present(*MainPageLocators.WIDGET_LEFT_1), \
            "отсутствует виджет №1(новости)"
        assert self.is_element_present(*MainPageLocators.WIDGET_LEFT_2), \
            "отсутствует виджет №2(магазины)"
        assert self.is_element_present(*MainPageLocators.WIDGET_LEFT_3), \
            "отсутствует виджет №3(читальня)"
        assert self.is_element_present(*MainPageLocators.WIDGET_LEFT_4), \
            "отсутствует виджет №4(записки)"
        assert self.is_not_element_present(*MainPageLocators.WIDGET_LEFT_NOT_5), \
            "на главной обнаружен неожидаемый виджет, слева"
        assert self.is_element_present(*MainPageLocators.WIDGET_RIGHT_1), \
            "отсутствует виджет №1(новые компании)"
        assert self.is_element_present(*MainPageLocators.WIDGET_RIGHT_2), \
            "отсутствует виджет №2(новые отзывы)"
        assert self.is_not_element_present(*MainPageLocators.WIDGET_RIGHT_NOT_3), \
            "на главной обнаружен неожидаемый виджет, справа"



