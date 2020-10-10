with open("database_access.txt") as dt_acc:
    param_db = [val.strip() for val in dt_acc]

print(param_db)