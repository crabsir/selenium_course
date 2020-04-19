from selenium.common.exceptions import NoSuchElementException


def test_add_to_basket_presence(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    try:
        add_to_basket = browser.find_element_by_css_selector("button.btn-add-to-basket")
    except NoSuchElementException:
        add_to_basket = False

    assert add_to_basket, "'Add to basket' button not found!"
