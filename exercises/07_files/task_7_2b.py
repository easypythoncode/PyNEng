# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

# answer
from sys import argv

src, dst = argv[1], argv[2]
with open(src) as f, open(dst, 'w') as f1:
    for list in f:
        if list.startswith('!'):
            continue
        for element in ignore:
            if element in list:
                break
        else:
            f1.write(list)
