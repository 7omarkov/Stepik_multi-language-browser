import time
from selenium.webdriver.common.by import By

class Test_selenium1py_pythonanywhere():

    def test_add_item_button_exist(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

        time.sleep(3)

        add_item_button = browser.find_elements(By.XPATH, "//button[contains(@class,'add-to-basket')]")

        assert add_item_button, "Add to basket button not found"

        time.sleep(3)