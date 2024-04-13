class WebLocators:
    """
           This class is used to contain all the locators that are required to perform the testing for the orange HRM login page
        """

    def __init__(self):
        self.UserNameInputFieldLocator="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        self.PassWordInputFieldLocator="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        self.SubmitButtonLocator="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        self.Invalid_Message_Locator="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"
