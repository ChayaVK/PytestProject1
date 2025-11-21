import pytest
from selenium import webdriver

@pytest.fixture
def base_value():
    return 10

@pytest.mark.param
@pytest.mark.parametrize("incremental_value,expected_value", [
    (5,15),
    (20,30),
    (50,60)
])
def test_operation_fixture(base_value, incremental_value, expected_value):
    assert base_value+incremental_value == expected_value

@pytest.mark.param
@pytest.mark.parametrize("x,y,z",[
    (1,5,6),
    (10,20,30),
    (15,20,35)
])
def test_addition(x,y,z):
    assert x+y==z



