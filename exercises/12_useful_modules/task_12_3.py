# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

# answer

from task_12_1 import ping_ip_addresses
from task_12_2 import convert_ranges_to_ip_list
from tabulate import tabulate


def print_ip_table(value1, value2):
    dict = {}
    dict['Reachable'] = value1
    dict['Unreachable'] = value2
    result = (tabulate(dict, headers='keys'))
    return result


if __name__ == "__main__":
    result1 = convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132'])
    # result1 = convert_ranges_to_ip_list(['8.8.4.4', '192.168.1.1'])
    resalt2 = ping_ip_addresses(result1)
    result3 = print_ip_table(list(resalt2[0]), list(resalt2[1]))
    print(result3)
