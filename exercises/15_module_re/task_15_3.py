# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""

# answer

import re
import os


def convert_ios_nat_to_asa(filein, fileout):
    regex = r'\D+ (?P<ip>\S+) (?P<dport>\S+) \S+ \S+ (?P<sport>\S+)'
    if os.path.isfile("asa_nat_config.txt"):
        os.remove("asa_nat_config.txt")
    with open(filein) as f1:
        for line in f1:
            match = re.search(regex, line)
            if match:
                ip, dport, sport = match.group('ip'), match.group('dport'), match.group('sport')
                string1 = f'object network LOCAL_{ip}\n'
                string2 = f' host {ip}\n'
                string3 = f' nat (inside,outside) static interface service tcp {dport} {sport}\n'
                with open(fileout, 'a') as f2:
                    f2.write(string1)
                    f2.write(string2)
                    f2.write(string3)
    return


if __name__ == "__main__":
    call = convert_ios_nat_to_asa('cisco_nat_config.txt', 'asa_nat_config.txt')
