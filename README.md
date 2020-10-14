<h1>Тестирование сайта MneMag.ru</h1>

<b>pytest -m guest -s -v --tb=line --browser_name=chrome --lang=ru test_main_page.py</b> - главная страница, гостевые тесты<br>
<b>pytest -m user -s -v --tb=line --browser_name=chrome --lang=ru test_main_page.py</b> - главная страница, тесты для залогиненных<br>
<b>pytest -m links_shops -s -v --tb=line test_shop_page.py</b> - целостность ссылок(по коду 200)

<ul>
<li><p><b>pages/mail_chek_register_code.py</b> - модуль извлечения регистрационного проверочного кода с почты</li>
<li><b>pages/checking_urls_shops.py</b> - модуль извлечения ссылок из БД, для проверки на код ответа 200</li>
</ul>  