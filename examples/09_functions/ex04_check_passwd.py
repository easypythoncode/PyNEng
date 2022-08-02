def check_passwd(user, passwd, min_len=8, unique_numbers=3):
    numbers = "0123456789"

    if len(passwd) < min_len:
        print("Пароль слишком короткий")
        return False
    elif user.lower() in passwd.lower():
        print("В пароле содержится имя пользователя")
        return False
    elif len(set(passwd).intersection(set(numbers))) < unique_numbers:
        print("В пароле должно быть 3 уникальные цифры")
        return False
    else:
        print(f"Пароль для пользователя {user} установлен")
        return True


def check_passwd_input(min_len=8, unique_numbers=3):
    user = input("Введите имя пользователя: ")
    passwd = input("Введите пароль: ")
    return check_passwd(user, passwd, min_len, unique_numbers)


def check_passwd_envvar(min_len=8, unique_numbers=3):
    # user = read from envvar
    # passwd = read from envvar
    return check_passwd(user, passwd, min_len, unique_numbers)
