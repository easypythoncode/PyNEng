from functools import wraps
from importlib import reload
import sys
import pytest

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        __tracebackhide__ = True
        wrapper.total_calls += 1
        result = func(*args, **kwargs)
        return result

    wrapper.total_calls = 0
    return wrapper


@count_calls
def monkey_input_r2(prompt):
    __tracebackhide__ = True
    if monkey_input_r2.total_calls == 1:
        return "r2"
    elif monkey_input_r2.total_calls == 2:
        return "ip"


@count_calls
def monkey_input_sw1(prompt):
    __tracebackhide__ = True
    if monkey_input_sw1.total_calls == 1:
        return "sw1"
    elif monkey_input_sw1.total_calls == 2:
        return "произвольная строка"


def test_task_r2_correct_param(capsys, monkeypatch):
    """
    Проверка работы задания при вводе r2
    """
    monkeypatch.setattr("builtins.input", monkey_input_r2)
    import task_5_1c

    out, err = capsys.readouterr()
    correct_stdout = "10.255.0.2"

    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
            correct_stdout in out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"


def test_task_sw1_wrong_param(capsys, monkeypatch):
    """
    Проверка работы задания при вводе sw1
    """
    monkeypatch.setattr("builtins.input", monkey_input_sw1)
    if sys.modules.get("task_5_1c"):
        del sys.modules["task_5_1c"]
    try:
        import task_5_1c
    except KeyError:
        pytest.fail(
            "В этом задании должна обрабатываться ситуация, "
            "когда параметр указан неправильный. Не должна возникать ошибка KeyError"
        )

    out, err = capsys.readouterr()
    correct_stdout = "параметра нет"
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
            correct_stdout in out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"
