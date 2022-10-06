
from PageObjects.Login_Page import LoginPageObjects
import time

class LoginView:

    def __init__(self, drv):
        # Create instance of the Login Page Objects
        self.obj_driver = drv
        self.obj_login_page = LoginPageObjects(drv)

    # Regular login flow.
    def login(self, agency, user, pwd):
        try:
            self.obj_login_page.enter_agency(agency)
            self.obj_login_page.enter_user(user)
            self.obj_login_page.enter_password(pwd)
            self.obj_login_page.click_login()
        except Exception as e:
            print("Error : {}".format(e))

    def verify_login(self):
        try:
            if self.obj_login_page.check_login():
                print("Logged in successfully.")
            else:
                print("Error Logging in.")

        except Exception as e:
            print("Error : {}".format(e))