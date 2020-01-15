# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
# answer
ospf_route = ospf_route.split()  # преобразуем строку в список строк
print(ospf_route)
protocol = ospf_route[0]
protocol = protocol.replace('O', 'OSPF')
prefix = ospf_route[1]
metric = ospf_route[2]
metric = metric.strip('[]')
hop = ospf_route[4]
hop = hop.rstrip(',')
update = ospf_route[5]
update = update.rstrip(',')
interface = ospf_route[6]
#
out = '''
Protocol:            {}
Prefix:              {}
AD/Metric:           {}
Next-Hop:            {}
Last update:         {}
Outbound Interface:  {}
'''
print(out.format(protocol, prefix, metric, hop, update, interface))
