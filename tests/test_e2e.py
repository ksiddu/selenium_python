from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from time import sleep

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        print("##### within test: test_e2e() method #####")
        homePage.shopItems().click()
        checkoutPage = CheckoutPage(self.driver)
        cards = checkoutPage.getCardTitles()
        log.info("get all title cards")

        i = -1

        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                log.info(cardText)
                checkoutPage.getCardFooters()[i].click()

        checkoutPage.getCheckoutButton().click()
        checkoutPage.checkOutItems().click()
        log.info("click checkout button")

        confirmPage = ConfirmPage(self.driver)
        confirmPage.getCountryTextBox().send_keys("ind")

        self.verifyLinkPresence("India")
        log.info("entering country name")
        confirmPage.getCountryLink().click()

        confirmPage.getPurchaseButton().click()
        actual_text = confirmPage.getSuccessText().text
        log.info("text received from application is " + actual_text)
        expected_text = "Success! Thank you!"
        #expected_text = "Failure! Thank you!"
        assert expected_text in actual_text

