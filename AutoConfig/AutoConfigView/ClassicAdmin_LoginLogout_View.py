from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Login_Logout import ClassicAdminLoginLogoutObjects
from PageObjects.Logout import LogOutObjects


class ClassicAdminLoginLogoutView:

    def __init__(self, drv):
        # Create instance of the Fees Page Objects
        self.obj_driver = drv
        self.obj_login_logout = ClassicAdminLoginLogoutObjects(drv)
        self.obj_logout = LogOutObjects(drv)

    # Login to classic admin
    def login_classic_admin(self, username, password):
        try:
            self.obj_login_logout.enter_username(username)
            self.obj_login_logout.enter_password(password)
            self.obj_login_logout.click_login()
            success = self.obj_login_logout.verify_success_login()
            if success == 1:
                print("Successfully Login")
            else:
                print("Unable to Login to Classic Admin")

        except Exception as e:
            print("Error : {}".format(e))

    # Logout from classic admin
    def logout_classic_admin(self):
        try:
            self.obj_login_logout.click_logout()
            success = self.obj_login_logout.verify_success_logout()
            if success == 1:
                print("Logged out successfully")
            else:
                print("Unable to Logout from Classic Admin")

        except Exception as e:
            print("Error : {}".format(e))
