from selenium.webdriver.common.by import By


class BasePageLocators():
    # иконка авторизированного пользователя
    USER_ICON = (By.CLASS_NAME, "img-thumbnail")

    # ссылки на форму авторизация / регистрация(шапка)
    LOGIN_LINK = (By.LINK_TEXT, "Войти")
    REGISTER_LINK = (By.LINK_TEXT, "Регистрация")

    # поля фофрмы авторизации
    LOGIN_EMAIL = (By.ID, "login_email")
    LOGIN_PASSWORD = (By.ID, "login_password")

    # год копирайта, версия для ПК
    COPYRIGHT = (By.CLASS_NAME, "tc_copytxt")


class MainPageLocators():
    # виджеты главной
    WIDGET_LEFT_1 = (By.CSS_SELECTOR, "#widget_pos_left-bottom .widget:nth-child(1)")
    WIDGET_LEFT_2 = (By.CSS_SELECTOR, "#widget_pos_left-bottom .widget:nth-child(2)")
    WIDGET_LEFT_3 = (By.CSS_SELECTOR, "#widget_pos_left-bottom .widget:nth-child(3)")
    WIDGET_LEFT_4 = (By.CSS_SELECTOR, "#widget_pos_left-bottom .widget:nth-child(4)")
    WIDGET_LEFT_NOT_5 = (By.CSS_SELECTOR, "#widget_pos_left-bottom .widget:nth-child(5)")

    WIDGET_RIGHT_1 = (By.CSS_SELECTOR, "#widget_pos_right-bottom .widget:nth-child(1)")
    WIDGET_RIGHT_2 = (By.CSS_SELECTOR, "#widget_pos_right-bottom .widget:nth-child(2)")
    WIDGET_RIGHT_NOT_3 = (By.CSS_SELECTOR, "#widget_pos_right-bottom .widget:nth-child(3)")
