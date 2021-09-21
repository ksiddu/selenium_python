from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self):

        homepage = HomePage(self.driver)

        homepage.getName().send_keys("Siddu")
        homepage.getEmail().send_keys("siddu@gmail.com")
        self.selectOptionByText(homepage.getGender(), "Male")
        homepage.getSubmit().click()
        expected_text = "Success! The Form has been submitted successfully!."
        actual_text = homepage.getSuccessMessage().text
        assert expected_text in actual_text
