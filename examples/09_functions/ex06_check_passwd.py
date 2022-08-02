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


def select_correct_passwd(user_list):
    ok = []
    not_ok = []
    for user, password in user_list:
        correct_password = check_passwd(user, password)

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
