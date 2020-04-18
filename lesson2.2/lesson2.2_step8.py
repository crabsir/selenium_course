from selenium import webdriver
import time
import os

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'upload_file.txt')

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Ivan")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Petrov")
    email = browser.find_element_by_name("email")
    email.send_keys("ivan_petrov@mail.com")

    upload = browser.find_element_by_id("file")
    upload.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
