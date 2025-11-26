import pytest
from selenium import webdriver



def test_chrome(getdriver):
    getdriver.get("https://www.google.com")
    getdriver.maximize_window()
    print(getdriver.title)
    print(getdriver.current_url)