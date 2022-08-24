# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""

# answer

import re


def get_ip_from_cfg(file):
    dict = {}
    regex1 = r'^(interface) (\S+)'
    regex2 = r' ip address (\S+) (\S+)'
    with open(file) as f:
        for line in f:
            match1 = re.search(regex1, line)
            match2 = re.search(regex2, line)
            if match1:
                key = match1.group(2)
                continue
            elif match2:
                dict[key] = match2.groups()
    return dict


if __name__ == "__main__":
    call = get_ip_from_cfg('config_r1.txt')
    print(call)
