# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

# answer
import subprocess


def ping_ip_addresses(ip_adress):
    reachable = []
    unreachable = []
    result = {}
    for ip in ip_adress:
        ping = subprocess.run(['ping', ip],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
        if ping.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)
    result = reachable, unreachable
    return result


if __name__ == "__main__":
    list = ping_ip_addresses(['8.8.8.8', '9.9.9.a'])
    print(list)
