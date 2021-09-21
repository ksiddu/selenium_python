from selenium.webdriver.common.by import By


class ConfirmPage:

    country = (By.ID, "country")
    countryLink = (By.LINK_TEXT, "India")
    purchaseButton = (By.CSS_SELECTOR, "input[type='submit']")
    successText = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCountryTextBox(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCountryLink(self):
        return self.driver.find_element(*ConfirmPage.countryLink)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getSuccessText(self):
        return self.driver.find_element(*ConfirmPage.successText)


