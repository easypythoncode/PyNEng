# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


# answer
def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    result = ()
    with open(config_filename) as f:
        for line in f:
            allowed = []
            line = line.rstrip()
            if '/' in line:
                intf = (line.split())[-1]
            elif 'switchport access vlan' in line and line[-1].isdigit():
                access_dict[intf] = int(line.split()[-1])
            elif 'switchport mode access' in line and line[-1].isalpha():
                access_dict[intf] = 1
            elif 'switchport trunk allowed vlan' in line:
                vlan = line.split()[-1].split(',')
                for element in vlan:
                    allowed.append(int(element))
                trunk_dict[intf] = allowed
    result = list(result)
    result.append(access_dict)
    result.append(trunk_dict)
    result = tuple(result)
    return result


a = get_int_vlan_map('config_sw2.txt')
print(a)
