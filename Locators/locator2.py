class WebLocators_PIM:
    """This class is used to contain all the data that are required to perform the testing for the orange HRM log in page

    """


    def __init__(self):
        self.UserNameInputFieldLocator="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        self.PassWordInputFieldLocator="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        self.SubmitButtonLocator="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        self.pimModuleLocator="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a"
        self.Add_EmployeeLocator="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]"
        self.Add_firstName_Locator="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input"
        self.Add_LastName_Locator="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input"
        self.Add_EmployeeId_Locator="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"
        self.Add_Save_Button_Locator="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"
        self.Employee_List_Locator="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]"
        self.Name_Locator="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
        self.Id_Locator="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input"
        self.search_Button_Locator="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"
        self.Edit_Button_Locator="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]"
        self.gender_Input_Locator="//label[normalize-space()='Female']"
        self.Edit_save_Button_Locator="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button"
        self.DeleteButton_Locator="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]"
        self.Alert_Delete_Button="/html/body/div/div[3]/div/div/div/div[3]/button[2]"
        self.success_message_locator="//div[@id='oxd-toaster_1']"


