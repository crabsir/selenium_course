import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser..")
    browser.quit()
