from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_css_selector("input")
    for element in elements:
        element.send_keys("Bla bla")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
