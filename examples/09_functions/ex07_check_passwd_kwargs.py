from pprint import pprint


def check_passwd(
        user, passwd, min_len=8, unique_numbers=3, spec_sym=True, whitespace=False
):
    numbers = "0123456789"

    if len(passwd) < min_len:
        return False
    elif user.lower() in passwd.lower():
        return False
    elif len(set(passwd).intersection(set(numbers))) < unique_numbers:
        return False
    else:
        return True


# def select_correct_passwd(user_list, min_len=8, unique_numbers=3):
def select_correct_passwd(user_list, **kwargs):
    """
    Отбирает из списка списков user_list правильные пароли
    kwargs - смотри аргументы check_passwd
    """
    print("kwargs переменной длины", kwargs)
    ok = []
    not_ok = []
    for user, password in user_list:
        correct_password = check_passwd(
            # user, password, min_len=min_len, unique_numbers=unique_numbers
            user, password, **kwargs  # min_len=5, spec_sym=False
        )

        if correct_password:
            ok.append([user, password])
        else:
            not_ok.append([user, password])
    return (ok, not_ok)


data = [
    ["user10", "sdld1235fj"],
    ["user20", "sdf####2245klfdj"],
    ["user30", "ssdkfjsus#%er3df"],
    ["user40", "sfjsus#%er3df"],
]
ok, not_ok = select_correct_passwd(
    # data, min_len=5, spec_sym=False, whitespace=True
    data, 5, False, True
)
pprint(ok)
pprint(not_ok)
