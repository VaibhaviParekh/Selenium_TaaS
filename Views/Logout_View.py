
from PageObjects.Login_Page import LoginPageObjects
from PageObjects.Logout import LogOutObjects


class LogoutView:

    def __init__(self, drv):
        # Create instance of the Login Page Objects
        self.obj_driver = drv
        self.obj_logout_page = LogOutObjects(drv)
        self.obj_login_page = LoginPageObjects(drv)

    # Regular logout flow
    def logout(self):
        try:
            self.obj_logout_page.click_to_expand_menu()
            self.obj_logout_page.click_sign_out()
            self.check_logout()
        except Exception as e:
            print("Error : {}".format(e))

    # Navigate to Classic Admin
    def navigate_to_classic_admin(self):
        try:
            self.obj_logout_page.click_to_expand_menu()
            self.obj_logout_page.click_classic_admin()
        except Exception as e:
            print("Error : {}".format(e))

    def check_logout(self):
        try:
            if self.obj_login_page.verify_successful_logout():
                print("Logged Out successfully.")
            else:
                print("Error Logging Out.")

        except Exception as e:
            print("Error : {}".format(e))
