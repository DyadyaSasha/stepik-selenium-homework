import pytest

# xfail позволяет выполнять тесты и не учитывать их в отчёте в PASSED и FAILED тестах
# при elfxyjv прохождении теста информация учитывается в xpassed, принеудачном - в xfailed
@pytest.mark.xfail
def test_greater():
    num = 100
    assert num > 100


# пропуск теста
@pytest.mark.skip
def test_less():
    num = 100
    assert num < 100