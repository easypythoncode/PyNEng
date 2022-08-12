# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

# answer
list = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
with open('ospf.txt') as f:
    for line in f:
        line = line.replace(",", " ").replace("[", "").replace("]", "")
        line = line.split()
        a6, prefix, metric, a3, hope, update, int = line
        print('{:20}{}'.format(list[0], prefix))
        print('{:20}{}'.format(list[1], metric))
        print('{:20}{}'.format(list[2], hope))
        print('{:20}{}'.format(list[3], update))
        print('{:20}{}'.format(list[4], int))
