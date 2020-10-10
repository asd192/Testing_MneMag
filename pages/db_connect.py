import pymysql


def connect_db_user_read_and_write():
    pass


def connect_db_user_read_only():
    """коннект к базе, только чтение"""
    try:
        with open("database_access.txt") as da_ini:
            param_db = da_ini.readlines()

        connect = pymysql.connect(
            host=param_db[0].strip(),
            db=param_db[1].strip(),
            user=param_db[2].strip(),
            password=param_db[3].strip(),
            charset=param_db[4].strip(),
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Успешное подключение!", '\n')
    except:
        print("Не удалось подключиться к БД(на чтение)")
    finally:
        connect.close()
    return connect
