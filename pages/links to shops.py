import requests
import pymysql

# Настройки подключения к БД.
connect = pymysql.connect(
    host = '37.140.192.171',
    db = 'u0785704_mnemag',
    user = 'u0785704_testing',
    password = '5V3q1N8g',
    charset = 'utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
print ("Успешное подключение!", '\n')

try:
    # запрос ссылок из БД
    with connect.cursor() as cursor:
        sql = 'SELECT s_url FROM cms_con_shop WHERE id != 65 AND is_deleted is null AND date_approved is not null '
        cursor.execute(sql)
        print(cursor.description, '\n')

        # проверка статус-кодов ссылок
        dict_error, count_error = dict(), 0
        for row in cursor:
            try :
                url = str(row['s_url']).split('|')[0]
                status_url = requests.get(str(row['s_url']).split('|')[0])
                print(status_url, url)
            except:
                print(f"Ошибка - {url}")
                dict_error[url] = status_url
                count_error += 1
                continue
finally:
    connect.close()
    print(f"\nТест кодов ответов ссылок завершился! Ошибок - {count_error}\n")
    for key, value in dict_error.items():
        print(key, value)