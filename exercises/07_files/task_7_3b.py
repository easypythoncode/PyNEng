# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

# answer
uservlan = input('Введите номер Vlan: ')
result = []
with open('CAM_table.txt') as f:
    for line in f:
        if '/' in line:
            line = line.split()
            element = int(line.pop(0))
            line.insert(0, element)
            result.append(line)
result.sort()
for line in result:
    vlan, mac, type, port = line[0], line[1], line[2], line[3]
    if int(uservlan) == vlan:
        print('{:<8}{:18}{:9}'.format(vlan, mac, port))
