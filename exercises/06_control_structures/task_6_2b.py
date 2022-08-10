# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

# answwer
chek = True
ip = input('Введите IP адрес: ')
octet = ip.split('.')
while chek == True:
    for a in octet:
        if len(octet) != 4 or not a.isdigit() or int(a) < 0 or int(a) > 255:
            print('Неправильный IP-адрес')
            ip = input('Введите IP адрес: ')
            octet = ip.split('.')
            break
        else:
            chek = False
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
