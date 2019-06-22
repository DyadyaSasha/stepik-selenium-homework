import pytest


# @pytest.fixture - помечаем метод, который будет выполняться перед каждым тестом
# данный метод имеет область видимости в рамках текущего скрипта, чтобы распространить метод-fixture на все методы, нужно определить его в файле conftest
@pytest.fixture
def input_value():
    input = 39
    return input

# в параметрах метода-теста указывается имя метода-fixture
# (метод-fixture выполнится только тогда, когда укажут его имя в параметрах метода-теста)
def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


def test_divisible_by_6(input_val):
    assert input_val % 6 == 0