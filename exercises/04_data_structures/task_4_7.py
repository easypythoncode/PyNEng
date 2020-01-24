# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = 'AAAA:BBBB:CCCC'
# answer
mac = mac.split(':')
print(mac)

a = bin(int(mac[0], 16))
b = bin(int(mac[1], 16))
c = bin(int(mac[2], 16))
out = a + b + c
print(out.lstrip('0b'))
