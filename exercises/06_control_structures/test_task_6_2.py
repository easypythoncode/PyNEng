from importlib import reload
import sys
import pytest

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


@pytest.mark.parametrize(
    "ip_add,ip_type",
    [
        ("10.1.1.1", "unicast"),
        ("230.1.1.1", "multicast"),
        ("255.255.255.255", "local broadcast"),
        ("0.0.0.0", "unassigned"),
        ("250.1.1.1", "unused"),
    ],
)
def test_task_ip(capsys, monkeypatch, ip_add, ip_type):
    """
    Проверка работы задания при вводе multicast адреса
    """
    monkeypatch.setattr("builtins.input", lambda x=None: ip_add)
    if sys.modules.get("task_6_2"):
        reload(sys.modules["task_6_2"])
    import task_6_2

    out, err = capsys.readouterr()
    correct_stdout = ip_type
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
            correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"
