from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    variant = Select(browser.find_element_by_id("dropdown"))
    variant.select_by_visible_text(str(num1 + num2))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
