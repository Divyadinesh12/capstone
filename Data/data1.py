
class WebData:
    """This class is used to contain all the data that are required to perform the testing for the orange HRM log in page

    """

    def __init__(self):
        self.url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.UserName="Admin"
        self.Password="admin123"
        self.InvalidPassWord = "Invalid Password"
        self.DashboardUrl="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"