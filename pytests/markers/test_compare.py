import pytest

# декоратор @pytest.mark.<имя метки> назначает методу метку/группу
# pytest -m <markername> - запускает все тесты с указанной меткой
@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100


@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.others
def test_less():
    num = 100
    assert num < 100
