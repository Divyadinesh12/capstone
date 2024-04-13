"""
Test case dealing with PIM add new employee in the pim module,edit  exist employee in the pim module,delete exist employee in the pim module using pytest, POM
"""

# own package
from Data import data2
from Locators import locator2
from Methods import methods2
# common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# Exception
from selenium.common.exceptions import NoSuchElementException
# sleep
from time import sleep
# keys
from selenium.webdriver.common.keys import Keys
# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# pytest
import pytest

class TestValidatePIm:

    @pytest.fixture()
    def boot(self):
        """
        This method open the url and maximize window
        :return:None
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data2.WebData_PIM().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    @pytest.fixture()
    def login(self):
        """
        this method login webpage and go to home page
        :return:Move to home page
        """
        # enter username in the username input field
        methods2.WebMethods().enterText(self.driver,locator2.WebLocators_PIM().UserNameInputFieldLocator,data2.WebData_PIM().UserName)
        # enter password in the password input field
        methods2.WebMethods().enterText(self.driver,locator2.WebLocators_PIM().PassWordInputFieldLocator,data2.WebData_PIM().Password)
        # click the submit button and check it move home page from log in page
        methods2.WebMethods().clickButton(self.driver,locator2.WebLocators_PIM().SubmitButtonLocator)
        assert self.driver.current_url == data2.WebData_PIM().DashboardUrl
        # sleep method stop  python script at given time
        sleep(5)

    @pytest.mark.html
    def test_add_Employee(self,boot,login):
        """
        This method add employee in the PIM module
        :param boot:
        :param login:
        :return: successfully saved
        """
        try:
            # click PIM module
           methods2.WebMethods().clickButton(self.driver,locator2.WebLocators_PIM().pimModuleLocator)
           assert self.driver.current_url == data2.WebData_PIM().PimPageUrl
           sleep(5)
           # go to add employee list
           methods2.WebMethods().clickButton(self.driver,locator2.WebLocators_PIM().Add_EmployeeLocator)
            # send the first name to first name input field
           methods2.WebMethods().enterText(self.driver,locator2.WebLocators_PIM().Add_firstName_Locator,data2.WebData_PIM().FirstName)
            # send the last name to last name input field
           methods2.WebMethods().enterText(self.driver,locator2.WebLocators_PIM().Add_LastName_Locator,data2.WebData_PIM().LastName)
           # click employee id input field
           methods2.WebMethods().clickButton(self.driver,locator2.WebLocators_PIM().Add_EmployeeId_Locator)
           # select all existing text
           methods2.WebMethods().enterText(self.driver,locator2.WebLocators_PIM().Add_EmployeeId_Locator,Keys.CONTROL+"a")
           # Delete the existing text
           methods2.WebMethods().enterText(self.driver,locator2.WebLocators_PIM().Add_EmployeeId_Locator,Keys.DELETE)
            # send employee Id to employee id input field
           methods2.WebMethods().enterText(self.driver,locator2.WebLocators_PIM().Add_EmployeeId_Locator,data2.WebData_PIM().EmployeeId)
            # save the employee
           methods2.WebMethods().clickButton(self.driver,locator2.WebLocators_PIM().Add_Save_Button_Locator)
           sleep(2)
           # print success message from webpage
           success_message=self.wait.until(EC.presence_of_element_located((By.XPATH, locator2.WebLocators_PIM().success_message_locator))).text
           sleep(5)
           print(success_message)
           assert "Successfully Saved" in success_message
        except NoSuchElementException as e:
            print("Error:Element is not present in the web page")

    def test_Edit_Exist_Employee(self,boot,login):
        """
        This method edit an exist employee in the PIM module
        :param boot:
        :param login:
        :return:successfully updated
        """

        try:
            sleep(2)
            # navigate  to pim module in the left pane in the web page
            methods2.WebMethods().clickButton(self.driver, locator2.WebLocators_PIM().pimModuleLocator)
            # check it navigate to PIM module page
            assert self.driver.current_url == data2.WebData_PIM().PimPageUrl
            # move to employee list page
            methods2.WebMethods().clickButton(self.driver,locator2.WebLocators_PIM().Employee_List_Locator)
            # search employee to sent employee name and employee id
            methods2.WebMethods().enterText(self.driver,locator2.WebLocators_PIM().Name_Locator,data2.WebData_PIM().Exist_Employee_Name)
            methods2.WebMethods().enterText(self.driver,locator2.WebLocators_PIM().Id_Locator,data2.WebData_PIM().Exist_Employee_Id)
            # click search button to search employee according to our search
            methods2.WebMethods().clickButton(self.driver,locator2.WebLocators_PIM().search_Button_Locator)
            # click edit button to update the employee information
            methods2.WebMethods().clickButton(self.driver,locator2.WebLocators_PIM().Edit_Button_Locator)
            sleep(2)
            # enter gender
            methods2.WebMethods().clickButton(self.driver,locator2.WebLocators_PIM().gender_Input_Locator)
            # save the employee
            methods2.WebMethods().clickButton(self.driver,locator2.WebLocators_PIM().Edit_save_Button_Locator)
            sleep(2)
            # print success message from webpage
            success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, locator2.WebLocators_PIM().success_message_locator))).text
            sleep(5)
            print(success_message)
            assert "Successfully Updated" in success_message
        except NoSuchElementException as e:
            print("Error: Element is not present in the web page ")

    def test_delete_Exist_Employee(self,boot,login):
        """
        This method delete an exist employee in the PIM module
        :param boot:
        :param login:
        :return:successfully deleted
        """

        try:
            sleep(3)
            # Navigate to PIM page
            methods2.WebMethods().clickButton(self.driver, locator2.WebLocators_PIM().pimModuleLocator)
            assert self.driver.current_url == data2.WebData_PIM().PimPageUrl
            # move to employee list page for deleting purpose
            methods2.WebMethods().clickButton(self.driver, locator2.WebLocators_PIM().Employee_List_Locator)
            # search employee for delete from employee list to sent name and employee id
            methods2.WebMethods().enterText(self.driver, locator2.WebLocators_PIM().Name_Locator,data2.WebData_PIM().Exist_Employee_Name)
            methods2.WebMethods().enterText(self.driver, locator2.WebLocators_PIM().Id_Locator,data2.WebData_PIM().Exist_Employee_Id)
            # click search Button to search employee from employee list depend on our search
            methods2.WebMethods().clickButton(self.driver, locator2.WebLocators_PIM().search_Button_Locator)
            # click delete button
            sleep(2)
            methods2.WebMethods().clickButton(self.driver,locator2.WebLocators_PIM().DeleteButton_Locator)
            # deleted employee information from the exist employee
            methods2.WebMethods().clickButton(self.driver,locator2.WebLocators_PIM().Alert_Delete_Button)
            sleep(2)
            # print success message from webpage
            success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, locator2.WebLocators_PIM().success_message_locator))).text
            sleep(5)
            print(success_message)
            assert "Successfully Deleted" in success_message
        except NoSuchElementException as e:
            # this block of code execute when error occur
            print("Error: Element is not present in the web page ")






