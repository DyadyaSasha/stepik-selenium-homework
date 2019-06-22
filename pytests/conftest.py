import pytest

# данный метод будет виден любому тесту
@pytest.fixture
def input_val():
    input = 39
    print("run conftest fixture")
    return input

