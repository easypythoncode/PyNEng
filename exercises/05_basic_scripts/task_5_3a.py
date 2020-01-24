# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

# access_template = [
#     'switchport mode access', 'switchport access vlan {}',
#     'switchport nonegotiate', 'spanning-tree portfast',
#     'spanning-tree bpduguard enable'
# ]
#
# trunk_template = [
#     'switchport trunk encapsulation dot1q', 'switchport mode trunk',
#     'switchport trunk allowed vlan {}'
# ]

# answer
mode = (input('Введите режим работы интерфейса (access/trunk): '))  # <class 'str'>
interface = (input('Введите тип и номер интерфейса: '))
input_template = [
    ['Введите номер VLAN:'],
    ['Введите разрешенные VLANы:']
]
mode1 = mode.count('trunk')
vlan = (input(input_template[mode1]))

# vlan = (input('Введите номер влан(ов): '))

summ_template = [
    ['switchport mode access',
     'switchport access vlan {}',
     'switchport nonegotiate',
     'spanning-tree portfast',
     'spanning-tree bpduguard enable'],
    ['switchport trunk encapsulation dot1q',
     'switchport mode trunk',
     'switchport trunk allowed vlan {}']
]
mode = mode.count('trunk')

print('-' * 30)
print('interface {}'.format(interface))
print('\n'.join(summ_template[mode]).format(vlan))
