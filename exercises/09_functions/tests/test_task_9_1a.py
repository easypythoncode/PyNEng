import pytest
import task_9_1a
import sys
sys.path.append('..')

from common_functions import check_function_exists, check_function_params


def test_function_created():
    check_function_exists(task_9_1a, 'generate_access_config')


def test_function_params():
    check_function_params(function=task_9_1a.generate_access_config,
                          param_count=3,
                          param_names=['intf_vlan_mapping', 'access_template', 'psecurity'])


def test_function_return_value():
    template_psecurity = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]
    access_vlans_mapping = {
        'FastEthernet0/12': 10,
        'FastEthernet0/14': 11,
        'FastEthernet0/16': 17
    }
    template_access_mode = [
        'switchport mode access', 'switchport access vlan',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]
    correct_return_value_without_psecurity = ['interface FastEthernet0/12',
                                              'switchport mode access',
                                              'switchport access vlan 10',
                                              'switchport nonegotiate',
                                              'spanning-tree portfast',
                                              'spanning-tree bpduguard enable',
                                              'interface FastEthernet0/14',
                                              'switchport mode access',
                                              'switchport access vlan 11',
                                              'switchport nonegotiate',
                                              'spanning-tree portfast',
                                              'spanning-tree bpduguard enable',
                                              'interface FastEthernet0/16',
                                              'switchport mode access',
                                              'switchport access vlan 17',
                                              'switchport nonegotiate',
                                              'spanning-tree portfast',
                                              'spanning-tree bpduguard enable']
    correct_return_value_with_psecurity = ['interface FastEthernet0/12',
                                           'switchport mode access',
                                           'switchport access vlan 10',
                                           'switchport nonegotiate',
                                           'spanning-tree portfast',
                                           'spanning-tree bpduguard enable',
                                           'switchport port-security maximum 2',
                                           'switchport port-security violation restrict',
                                           'switchport port-security',
                                           'interface FastEthernet0/14',
                                           'switchport mode access',
                                           'switchport access vlan 11',
                                           'switchport nonegotiate',
                                           'spanning-tree portfast',
                                           'spanning-tree bpduguard enable',
                                           'switchport port-security maximum 2',
                                           'switchport port-security violation restrict',
                                           'switchport port-security',
                                           'interface FastEthernet0/16',
                                           'switchport mode access',
                                           'switchport access vlan 17',
                                           'switchport nonegotiate',
                                           'spanning-tree portfast',
                                           'spanning-tree bpduguard enable',
                                           'switchport port-security maximum 2',
                                           'switchport port-security violation restrict',
                                           'switchport port-security']

    return_value = task_9_1a.generate_access_config(access_vlans_mapping, template_access_mode)
    assert return_value != None, "?????????????? ???????????? ???? ????????????????????"
    assert type(return_value) == list, "?????????????? ???????????? ???????????????????? ????????????"
    assert return_value == correct_return_value_without_psecurity, "?????????????? ???????????????????? ???????????????????????? ???????????????? ?????? ???????????? ?? psecurity == None"
    return_value_with_psecurity = task_9_1a.generate_access_config(
        access_vlans_mapping, template_access_mode, template_psecurity)
    assert return_value_with_psecurity == correct_return_value_with_psecurity, "?????????????? ???????????????????? ???????????????????????? ???????????????? ?????? ???????????? ?? psecurity"

