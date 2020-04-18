from selenium import webdriver
import time

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id("button")

finally:
    time.sleep(10)
    browser.quit()
