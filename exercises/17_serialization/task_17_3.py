# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

# answer

import re
from pprint import pprint


def parse_sh_cdp_neighbors(value):
    list = value.split('\n')
    dict = {}
    regex1 = r'(?P<ldev>\S+)>'
    regex2 = r'(?P<rdev>\S+\d+) +(?P<lintf>\S+ \d+/\d+).+  (?P<rintf>\S+ \d+/\d+)'
    for line in list:
        match1 = re.search(regex1, line)
        match2 = re.search(regex2, line)
        if match1:
            ldev = match1.group(1)
            dict[ldev] = {}
            continue
        elif match2:
            rdev, lintf, rintf = match2.group("rdev", "lintf", "rintf")
            dict[ldev][lintf] = {rdev: rintf}
    return dict


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        call = parse_sh_cdp_neighbors(f.read())
    pprint(call)
