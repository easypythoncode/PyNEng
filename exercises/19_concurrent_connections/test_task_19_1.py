import pytest
import task_19_1
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, get_reach_unreach

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_19_1, "ping_ip_addresses")


def test_function_return_value():
    """
    Проверка работы функции
    """
    list_of_ips = ["1.1.1.1", "8.8.8.8", "8.8.4.4", "2.2.2.2"]
    correct_return_value = get_reach_unreach(list_of_ips)
    correct_reachable, correct_unreachable = correct_return_value
    correct_reachable, correct_unreachable = sorted(correct_reachable), sorted(
        correct_unreachable
    )

    return_value = task_19_1.ping_ip_addresses(list_of_ips)
    assert return_value != None, "Функция ничего не возвращает"
    assert (
            type(return_value) == tuple
    ), f"По заданию функция должна возвращать кортеж, а возвращает {type(return_value).__name__}"
    assert 2 == len(return_value), "Функция должна возвращать кортеж с двумя списками"
    assert all(
        type(item) == list for item in return_value
    ), "Функция должна возвращать кортеж со списками внутри"

    return_reachable, return_unreachable = return_value
    return_reachable, return_unreachable = sorted(return_reachable), sorted(
        return_unreachable
    )
    assert correct_return_value == (
        return_value
    ), "Функция возвращает неправильное значение"
