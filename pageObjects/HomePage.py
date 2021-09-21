from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    shop = (By.CSS_SELECTOR, "a[href='/angularpractice/shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    success_msg = (By.CSS_SELECTOR, "[class*='alert alert-success']")

    def __init__(self, driver):
          self.driver = driver

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def selectGender(self, value):
        select = Select(self.driver.find_element(*HomePage.gender))
        select.select_by_visible_text(value)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.success_msg)

