import pytest
import requests
import pymysql

@pytest.mark.skip
@pytest.mark.links_shop
def serviceability_link_shops(path_file):
    """коннект к базе, только чтение"""
    try:
        with open(path_file) as dt_acc:
            param_db = dt_acc.readlines()

        connect = pymysql.connect(
            host=param_db[0].strip(),
            db=param_db[1].strip(),
            user=param_db[2].strip(),
            password=param_db[3].strip(),
            charset=param_db[4].strip(),
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Успешное подключение!", '\n')

        # запрос ссылок из БД
        with connect.cursor() as cursor:
            sql = 'SELECT s_url FROM cms_con_shop WHERE id != 65 AND is_deleted is null AND date_approved is not null'
            cursor.execute(sql)
            print(cursor.description, '\n')

            # проверка статус-кодов ссылок
            dict_error, count_error = dict(), 0
            for row in cursor:
                try:
                    url = str(row['s_url']).split('|')[0]
                    status_url = requests.get(str(row['s_url']).split('|')[0])
                    print(status_url, url)
                except:
                    print(f"Ошибка - {status_url} {url}")
                    dict_error[url] = status_url
                    count_error += 1
                    continue

        print(f"\nТест кодов ответов ссылок завершился! Ошибок - {count_error}\n")
        for key, value in dict_error.items():
            print(key, value)
    except:
        print("Не удалось проверить ссылки магазинов")
        raise