from pprint import pprint


def check_passwd(user, passwd, min_len=8, unique_numbers=3):
    numbers = "0123456789"

    if len(passwd) < min_len:
        return False
    elif user.lower() in passwd.lower():
        return False
    elif len(set(passwd).intersection(set(numbers))) < unique_numbers:
        return False
    else:
        return True


data = [
    ["user10", "sdld1235fj"],
    ["user20", "sdf####2245klfdj"],
    ["user30", "ssdkfjsus#%er3df"],
]
for user_data in data:
    user = user_data[0]
    password = user_data[1]
    if len(passwd) < min_len:
        correct_password = False
    elif user.lower() in passwd.lower():
        correct_password = False
    elif len(set(passwd).intersection(set(numbers))) < unique_numbers:
        correct_password = False
    else:
        correct_password = True

    if correct_password:
        print("Пароль ОК")
    else:
        print("Пароль не ОК")

for user_data in data:
    user = user_data[0]
    password = user_data[1]
    correct_password = check_passwd(user, password)

    if correct_password:
        print("Пароль ОК")
    else:
        print("Пароль не ОК")
