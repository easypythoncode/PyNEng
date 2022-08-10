# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

# answwer
ip = input('Введите IP адрес: ')
octet = ip.split('.')
if int(octet[0]) >= 1 and int(octet[0]) <= 223:
    print('unicast')
elif int(octet[0]) >= 224 and int(octet[0]) <= 239:
    print('multicast')
elif '255.255.255.255' in ip:
    print('local broadcast')
elif '0.0.0.0' in ip:
    print('unassigned')
else:
    print('unused')
