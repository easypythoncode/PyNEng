import pytest
import task_24_2d
import task_24_2a
from netmiko.cisco.cisco_ios import CiscoIosSSH
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(task_24_2d, "MyNetmiko")


def test_class_inheritance(first_router_from_devices_yaml):
    ssh = task_24_2d.MyNetmiko(**first_router_from_devices_yaml)
    assert isinstance(ssh, CiscoIosSSH), "Класс MyNetmiko должен наследовать CiscoIosSSH"
    check_attr_or_method(ssh, method="send_config_set")
    ssh.disconnect()


@pytest.mark.parametrize(
    "error,command",
    [
        ("Invalid input detected", "logging 0255.255.1"),
        ("Incomplete command", "lo"),
        ("Ambiguous command", "a"),
    ],
)
def test_errors_ignore_false(first_router_from_devices_yaml, command, error):
    ssh = task_24_2d.MyNetmiko(**first_router_from_devices_yaml)
    with pytest.raises(Exception) as excinfo:
        return_value = ssh.send_config_set(command, ignore_errors=False)
    ssh.disconnect()
    assert error in str(
        excinfo
    ), "Метод send_config_commands должен генерировать исключение, когда ignore_errors=False"


@pytest.mark.parametrize(
    "error,command",
    [
        ("Invalid input detected", "logging 0255.255.1"),
        ("Incomplete command", "lo"),
        ("Ambiguous command", "a"),
    ],
)
def test_errors_ignore_true(first_router_from_devices_yaml, command, error):
    ssh = task_24_2d.MyNetmiko(**first_router_from_devices_yaml)
    return_value = ssh.send_config_set(command, ignore_errors=True)
    ssh.disconnect()
    assert (
            error in return_value
    ), "Метод send_config_commands должен возвращать вывод с ошибкой, когда ignore_errors=True"
