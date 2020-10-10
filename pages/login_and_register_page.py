# pytest -s -v -m high_importance test_register.py
# pytest -s -v -m "not high_importance" test_register.py
# pytest -s -v -m "high_importance or high_importance2" test_register.py
# pytest -s -v -m high_importance --tb=line --reruns 1 --browser_name=firefox  test_register.py

import time
import pytest
from selenium.webdriver.support.ui import Select
from datetime import datetime

link = "https://mnemag.ru/auth/register"

user_data = {1: ['test_mnemag@ya.ru', 'testpass', 'testpass'],
             2: ['empty@ya.ru', 'pass', 'pass'],
             3: ['123#mail.com', ' f_ "', ' f_ "']}


class TestMainRegister():
    @pytest.mark.guest()
    def test_positive_guest_registration_form(self, browser):
        # заполнение формы регистрации
        browser.get(link)
        browser.find_element_by_id('nickname').send_keys(f'TestName{datetime.now().microsecond}')
        Select(browser.find_element_by_id('group_id')).select_by_value('4')
        browser.find_element_by_id('email').send_keys(user_data[1][0])
        browser.find_element_by_id('password1').send_keys(user_data[1][1])
        browser.find_element_by_id('password2').send_keys(user_data[1][1])
        browser.find_element_by_name('submit').click()

        # текст активной группы пользователей
        group_user = browser.find_element_by_class_name('chosen-single')
        assert "Пользователи" == group_user.text, \
            "Текст выбранной группы не соответствует id"

        # текст проверки ввода капчи
        captcha_text = browser.find_element_by_class_name('error_text')
        assert "Неправильно указан код защиты от спама" == captcha_text.text, \
            "Текст о отсутствии ввода капчи отсутствует"

        # текст о наличии ошибок в форме
        error_text = browser.find_element_by_css_selector('.sess_messages .error')
        assert "Найдены ошибки в форме" in error_text.text, \
            "Текст о наличии ошибок в форме отсутствует"

        time.sleep(3)

    # @pytest.mark.xfail(reason="the error is being corrected")  # -rX -v
    # def test_fail_test(self, browser):
    #     # текст о наличии ошибок в форме
    #     error_text = browser.find_element_by_css_selector('.sess_messages .error')
    #     assert "Найдены ошибки в форме" in error_text.text, \
    #         "Текст о наличии ошибок в форме отсутствует"
