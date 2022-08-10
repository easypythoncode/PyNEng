# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

# answwer
chek = True
ip = input('Введите IP адрес: ')
octet = ip.split('.')
for a in octet:
    if len(octet) != 4 or not a.isdigit() or int(a) < 0 or int(a) > 255:
        print('Неправильный IP-адрес')
        chek = False
        break
if chek == True and int(octet[0]) >= 1 and int(octet[0]) <= 223:
    print('unicast')
elif chek == True and int(octet[0]) >= 224 and int(octet[0]) <= 239:
    print('multicast')
elif chek == True and '255.255.255.255' in ip:
    print('local broadcast')
elif chek == True and '0.0.0.0' in ip:
    print('unassigned')
elif chek == True:
    print('unused')
