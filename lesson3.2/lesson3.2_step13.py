from selenium import webdriver
import time
import unittest


class TestRegistration(unittest.TestCase):
    @staticmethod
    def reg_process(link):
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет поля
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("petrov_ivan@mail.com")
        input4 = browser.find_element_by_css_selector(".second_block .first")
        input4.send_keys("3222322")
        input5 = browser.find_element_by_css_selector(".second_block .second")
        input5.send_keys("Russia, Smolensk")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст, записываем в переменную welcome_text текст из элемента
        welcome_text = browser.find_element_by_tag_name("h1").text
        # возвращаем этот текст
        return welcome_text

    def test_registration1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(self.reg_process(link1), "Congratulations! You have successfully registered!",
                         "No welcome text!")

    def test_registration2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(self.reg_process(link2), "Congratulations! You have successfully registered!",
                         "No welcome text!")


if __name__ == "__main__":
    unittest.main()
