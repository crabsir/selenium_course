from selenium import webdriver
import time
import math


def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("return window.scrollBy(0, 150);")

    x = int(browser.find_element_by_id("input_value").text)
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
