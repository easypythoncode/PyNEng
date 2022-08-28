# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""

# answer


import re
import csv
from pprint import pprint


def write_dhcp_snooping_to_csv(filenames, output):
    regex1 = r'^(\S+\d+)'
    regex2 = r'(?P<mac>\S+:\S\S) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<intr>\S+)'
    data = [['switch', 'mac', 'ip', 'vlan', 'interface']]
    for file in filenames:
        device = re.search(regex1, file).group(1)
        with open(file) as f:
            for line in f:
                match = re.search(regex2, line)
                if match:
                    list = []
                    list.append(device)
                    for i in match.groups():
                        list.append(i)
                    data.append(list)
    # pprint(data)
    with open(output, 'w', newline='') as f:
        wr = csv.writer(f)
        for row in data:
            wr.writerow(row)
    # with open(output) as f:
    #     print(f.read())
    return


if __name__ == "__main__":
    # call = write_dhcp_snooping_to_csv(['sw1_dhcp_snooping.txt'], 'summ_dhcp_snooping.csv')
    call = write_dhcp_snooping_to_csv(['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt'],
                                      'summ_dhcp_snooping.csv')
