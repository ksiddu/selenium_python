import pytest
from time import sleep
import TestData
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getDataTwo):

        homepage = HomePage(self.driver)
        #print(getDataOne[0])
        #print(getDataOne[1])
        #print(getDataOne[2])
        #homepage.getName().send_keys(getDataOne[0])
        #homepage.getEmail().send_keys(getDataOne[1])
        #self.selectOptionByText(homepage.getGender(), getDataOne[2])

        homepage.getName().send_keys(getDataTwo["firstname"])
        homepage.getEmail().send_keys(getDataTwo["email"])
        self.selectOptionByText(homepage.getGender(), getDataTwo["gender"])
        homepage.getSubmit().click()
        expected_text = "Success! The Form has been submitted successfully!."
        actual_text = homepage.getSuccessMessage().text
        sleep(10)
        assert expected_text in actual_text
        self.driver.refresh()

    # using list of tuples
    @pytest.fixture(params=[("Siddu", "siddu@gmail.com", "Male"), ("June", "june@gmail.com", "Female")])
    def getDataOne(self, request):
        return request.param

    # using list of dictionaries from another test data file:
    @pytest.fixture(params=HomePageData.test_HomePageData)
    def getDataTwo(self, request):
        print("data from another file")
        return request.param

    # using list of dictionaries
    @pytest.fixture(params=[{"firstname": "Siddu", "email": "siddu@gmail.com", "gender": "Male"},
                            {"firstname": "June", "email": "june@gmail.com", "gender": "Female"}])
    def getDataThree(self, request):
        return request.param


