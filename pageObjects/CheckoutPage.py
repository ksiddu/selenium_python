from selenium.webdriver.common.by import By


class CheckoutPage:

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")


    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooters(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkOutBtn)

    def checkOutItems(self):
        return self.driver.find_element(*CheckoutPage.checkOut)

