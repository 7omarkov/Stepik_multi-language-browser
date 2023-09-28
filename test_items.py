import time
from selenium.webdriver.common.by import By



def test_add_item_button_exist(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    time.sleep(2)

    add_item_button = browser.find_elements(By.XPATH, "//button[contains(@class,'add-to-basket')]")

    assert add_item_button, "Add to basket button not found"

    time.sleep(1)