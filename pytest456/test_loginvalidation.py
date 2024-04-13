"""
Test dealing with login for valid and invalid credentials using pytest, pom
"""


# own package
from Data import data1
from Locators import locator1
from Methods import methods1
# common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Exception
from selenium.common.exceptions import NoSuchElementException
# sleep
from time import sleep
# pytest
import pytest
class TestLogInPageValidation:

    @pytest.fixture()
    def boot(self):
        """
        This method open the url and maximize window and close the browser
        :return:None
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data1.WebData().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        yield
        # using yield keyword this block of code execute after function block of code executed
        self.driver.quit()

    @pytest.mark.html
    def test_Valid_crendential(self,boot):
        """
        This method check login page with valid username and password
        :param boot:
        :return: Move to DashBoard page
        """
        # this block of code execute when exception not occur
        try:
            # send username,password to the username input field and password input field
            methods1.WebMethods().enterText(self.driver,locator1.WebLocators().UserNameInputFieldLocator,data1.WebData().UserName)
            methods1.WebMethods().enterText(self.driver,locator1.WebLocators().PassWordInputFieldLocator,data1.WebData().Password)
            # clik submit Button
            methods1.WebMethods().clickButton(self.driver,locator1.WebLocators().SubmitButtonLocator)
            sleep(5)
            #  check navigate to home page
            assert self.driver.current_url == data1.WebData().DashboardUrl
            print("login successful")

        except NoSuchElementException as e:
            # element not present in the web page then this block of code execute
            print("Error:Element is not present in the web page")

    @pytest.mark.html
    def test_invalid_credential(self,boot):
        """
        This method check whether valid error message displayed in the  login page with invalid credentials
        :return:Invalid password
        """
        # try block of code execute when exception s not present
        try:
            # send username to the username input field
            methods1.WebMethods().enterText(self.driver,locator1.WebLocators().UserNameInputFieldLocator,data1.WebData().UserName)
            # send password to the password input field
            methods1.WebMethods().enterText(self.driver,locator1.WebLocators().PassWordInputFieldLocator,data1.WebData().InvalidPassWord)
            # click submit button
            methods1.WebMethods().clickButton(self.driver,locator1.WebLocators().SubmitButtonLocator)
            sleep(2)
            # fetch error message for invalid login from web page
            print(self.driver.find_element(By.XPATH, locator1.WebLocators().Invalid_Message_Locator).text)
            sleep(3)
            # assert check current url not equal to dashboard url
            assert self.driver.current_url != data1.WebData().DashboardUrl

        except NoSuchElementException as e:
            # this block of code execute when exception occur
            print("Error:Element is not present in the wep page")




