import imaplib
import email


def mail_check():
    # получить логин/пароль доступа к почтовому ящику
    with open("pages/mail_access.txt", "r", encoding="UTF-8") as mail_access:
        param_mail = [val.strip() for val in mail_access]

    # Создаем сессию для подключения к почтовому ящику по IMAP и заносим ее в переменную mail
    mail = imaplib.IMAP4_SSL(param_mail[0])
    # Подключаемся к почтовому ящику по IMAP с использованием учетной записи
    mail.login(param_mail[1], param_mail[2])
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
    # Получаем заголовки и тело письма, заносим результат в переменную email_message.
    email_message = email.message_from_string(raw_email_string)

    # добываем код подтверждения из "mail delivery failed"
    with open("message_mail.txt", "w", encoding="UTF-8") as message:
        message.write(str(email_message))

    with open("message_mail.txt", "r", encoding="utf8") as message:
        message = message.read()

    find_text = 'подтверждения:'
    first_symbol_code = message.find(find_text) + len(find_text)
    last_symbol_code = first_symbol_code + 33

    code_confirmation = message[first_symbol_code + 1: last_symbol_code]
    print(code_confirmation)
    return code_confirmation

mail_check()