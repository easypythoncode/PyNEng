# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

# answer
from sys import argv

ip = argv[1].split('/')
mask = ip.pop(-1)  # <class 'str'>
ip = ip[0]  # <class 'str'>

# mask
mask1 = '1' * int(mask) + '0' * (32 - int(mask))  # получаем маску в двоичной форме
mask2 = '/' + mask
a1 = mask1[0:8]  # <class 'str'>
b1 = mask1[8:16]
c1 = mask1[16:24]
d1 = mask1[24:]
a2 = int(a1, 2)  # <class 'int'>
b2 = int(b1, 2)
c2 = int(c1, 2)
d2 = int(d1, 2)
#  IP
ip = ip.split('.')  # <class 'list'>

a = int(ip[0])  # <class 'int'>
a = bin(a & a2)  # <class 'str'> побитно умножаем IP (int) на mask (int) для получения адреса сети в bin
a = str(int(a, 2))
b = int(ip[1])  # <class 'int'>
b = bin(b & b2)  # побитно умножаем IP (int) на mask (int) для получения адреса сети
b = str(int(b, 2))
c = int(ip[2])  # <class 'int'>
c = bin(c & c2)  # побитно умножаем IP (int) на mask (int) для получения адреса сети
c = str(int(c, 2))
d = int(ip[3])  # <class 'int'>
d = bin(d & d2)  # побитно умножаем IP (int) на mask (int) для получения адреса сети
d = str(int(d, 2))

# выводим Network
out = '''
Network:
{:<10}{:<10}{:<10}{:<10}
{:08b}  {:08b}  {:08b}  {:08b}
'''
print(out.format(a, b, c, d, int(a), int(b), int(c), int(d)))

# выводим mask
out1 = '''
Mask:
{}
{:<10}{:<10}{:<10}{:<10}
{:<8}  {:<8}  {:<8}  {:<8}
'''
print(out1.format(mask2, int(a1, 2), int(b1, 2), int(c1, 2), int(d1, 2), a1, b1, c1, d1))
