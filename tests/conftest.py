import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def get_sampledata():
    user_credentials = {'username':'tomsmith','password':'SuperSecretPassword!'}
    return user_credentials



