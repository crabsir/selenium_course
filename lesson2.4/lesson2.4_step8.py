from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
