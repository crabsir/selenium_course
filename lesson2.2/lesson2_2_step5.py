from selenium import webdriver

link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_tag_name("button")

# browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)
browser.execute_script("return window.scrollBy(0, 150);")

button.click()

assert True
