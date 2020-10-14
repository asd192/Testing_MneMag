<h1>Тестирование сайта MneMag.ru</h1>


<h2>Запуск тестов</h2>
<pre>
    — <b>главная страница, гостевые тесты</b> - <i>pytest -m guest -s -v --tb=line --browser_name=chrome --lang=ru test_main_page.py</i>
    — <b>главная страница, тесты для залогиненных</b> - <i>pytest -m user -s -v --tb=line --browser_name=chrome --lang=ru test_main_page.py</i>
    — <b>ссылки, целостность (по коду 200) - <i>pytest</b> -m links_shops -s -v --tb=line test_shop_page.py</i>
</pre>

<h2>Файлы</h2>
<ul>
<li><p><b>pages/mail_chek_register_code.py</b> - модуль извлечения регистрационного проверочного кода с почты</li>
<li><b>pages/checking_urls_shops.py</b> - модуль извлечения ссылок из БД, для проверки на код ответа 200</li>
</ul>  