import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


def answer():
    return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser..")
    browser.quit()


@pytest.mark.parametrize('question_num',  # ["236898"]
                         ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_hint_test_is_correct(browser, question_num):
    link = f"https://stepik.org/lesson/{question_num}/step/1"
    browser.get(link)

    answer_field = WebDriverWait(browser, 10).until(
        Ec.element_to_be_clickable((By.ID, "ember69"))
    )
    answer_field.send_keys(answer())

    submit_button = browser.find_element_by_css_selector("button.submit-submission")
    submit_button.click()

    expected_element = WebDriverWait(browser, 10).until(
        Ec.visibility_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
    )
    assert expected_element.text == "Correct!"
