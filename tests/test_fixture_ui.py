import pytest
from selenium import webdriver

@pytest.fixture
def getdriver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_chrome(getdriver):
    getdriver.get("https://www.google.com")
    getdriver.maximize_window()
    print(getdriver.title)
    print(getdriver.current_url)