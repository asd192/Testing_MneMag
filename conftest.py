import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_add_option(parser):
    """новые параметры для командной строки"""
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--lang', action='store', default='ru',
                     help="Choose language")


@pytest.fixture(scope="function")  # function, class, module, session
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption("lang")

    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("ожидается параметр --browser chrome или firefox")


    browser.implicitly_wait(3)  # ожидание 3 секунды, для случаев задержек в работе сайта
    yield browser
    browser.quit()
