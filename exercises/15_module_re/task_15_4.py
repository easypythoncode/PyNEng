# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""

# answer

import re


def get_ints_without_description(file):
    list = []
    regex1 = r'^(interface) (\S+)'
    regex2 = r' description'
    with open(file) as f:
        for line in f:
            match1 = re.search(regex1, line)
            match2 = re.search(regex2, line)
            if match1:
                int = match1.group(2)
                list.append(int)
                continue
            if match2:
                list.pop(-1)
    return list


if __name__ == "__main__":
    call = get_ints_without_description('config_r1.txt')
    print(call)
