import pytest

# параметризованный тест - запускается один и тот же тест несколько раз для разных входных параметров
@pytest.mark.parametrize("num, output", [(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
    assert 11 * num == output