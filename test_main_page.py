import pytest
from test_register import *

if __name__ == "__main__":
    # позитивный тест - данные введены верно, капча не прожата
    test_completing_the_registration_form()
    test_group_user_text()
    test_captcha_text()
    test_error_text()
    print("register.py - завершено!")
