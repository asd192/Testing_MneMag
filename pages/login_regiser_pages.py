# pytest -s -m user test_main_page.py

import time

from .base_page import BasePage
from .mail_chek_register_code import mail_check

from .locators import RegAuthLocators


class LoginRegisterPage(BasePage):
    def register_user(self):
        """регистрация нового пользователя"""
        # генерация уникального логина, пароля и почты
        unique_number = str(int(time.time()))

        nick_name = unique_number
        email = unique_number + "@mail.test"
        password = unique_number

        # заполнение данных регистрации
        input_nick = self.browser.find_element(*RegAuthLocators.REGISTER_NICK_NAME)
        input_nick.send_keys(nick_name)

        input_email = self.browser.find_element(*RegAuthLocators.REGISTER_EMAIL)
        input_email.send_keys(email)

        input_pass_1 = self.browser.find_element(*RegAuthLocators.REGISTER_PASSWORD_1)
        input_pass_1.send_keys(password)

        input_pass_2 = self.browser.find_element(*RegAuthLocators.REGISTER_PASSWORD_2)
        input_pass_2.send_keys(password)

        input_button_resume = self.browser.find_element(*RegAuthLocators.REGISTER_BUTTON_RESUME)
        input_button_resume.click()

        # предпроверка правильности инфо-сообщений при регистрации
        assert self.is_not_element_present(*RegAuthLocators.REGISTER_CAPTCHA), \
            "сработала CAPTCHA"
        assert self.browser.find_element(*RegAuthLocators.REGISTER_MESSAGE_1).text == "Регистрация прошла успешно", \
            "отсутствует сообщение о успешной регистрации"
        assert self.browser.find_element(*RegAuthLocators.REGISTER_MESSAGE_2).text == email, \
            "в инфо-сообщении отсутствует email или указан другой"

        # страница кода подтверждения
        input_reg_token = self.browser.find_element(*RegAuthLocators.REGISTER_REG_TOKEN)
        input_reg_token.send_keys(mail_check())

        input_button_resume = self.browser.find_element(*RegAuthLocators.REGISTER_BUTTON_RESUME)
        input_button_resume.click()

        # проверка инфо-сообщения
        assert "e-mail успешно подтвержден" in self.browser.find_element(*RegAuthLocators.REGISTER_MESSAGE_1).text, \
            "отсутствует сообщение о успешности подтверждения e-mail"