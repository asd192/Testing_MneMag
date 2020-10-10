import imaplib
import base64
import email

# Создаем сессию для подключения к почтовому ящику по IMAP и заносим ее в переменную mail
mail = imaplib.IMAP4_SSL('imap.yandex.ru')

# Подключаемся к почтовому ящику по IMAP с использованием учетной записи
mail.login('panshinda@yandex.ru', 'dwhfedwoljmeuyrj')

# Выводим список папок в почтовом ящике
mail.list()

# Выбираем для работы папку входящие (inbox)
mail.select("inbox")

# Получаем массив со списком найденных почтовых сообщений
result, data = mail.search(None, "ALL")

# Сохраняем в переменную ids строку с номерами писем
ids = data[0]

# Получаем массив номеров писем
id_list = ids.split()

# Задаем переменную latest_email_id, значением которой будет номер последнего письма
latest_email_id = id_list[-1]

# Получаем письмо с идентификатором latest_email_id (последнее письмо).
result, data = mail.fetch(latest_email_id, "(RFC822)")

# В переменную raw_email заносим необработанное письмо
raw_email = data[0][1]

# Переводим текст письма в кодировку UTF-8 и сохраняем в переменную raw_email_string
raw_email_string = raw_email.decode('UTF-8')

# Получаем заголовки и тело письма и заносим результат в переменную email_message.
email_message = email.message_from_string(raw_email_string)

# кому отправлено письмо
print(email_message['To'])

# от кого отправлено письмо
print(email.utils.parseaddr(email_message['From'])[1])

# дата отправки письма
print(email_message['Date'])

# тема письма из base64
print(base64.b64decode(email_message['Subject'][10:-21].decode("UTF-8")))

# идентификатор письма
print(email_message['Message-Id'])


assert 'https://mnemag.ru/shop/123.html' in raw_email_string, "нет"
