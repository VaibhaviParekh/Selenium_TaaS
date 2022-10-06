
from PageObjects.ACA_Login_Logout import ACALoginLogoutObject
from PageObjects.ACA_Common import ACACommonObject

class ACALoginView:

    def __init__(self, drv):
        # Create instance of the ACA Login Page Objects
        self.obj_driver = drv
        self.obj_aca_login = ACALoginLogoutObject(drv)
        self.obj_common = ACACommonObject(drv)

    # Regular login flow.
    def aca_login(self, user, pwd):
        try:
            self.obj_aca_login.enter_username(user)
            self.obj_aca_login.enter_password(pwd)
            self.obj_aca_login.click_login_button()
            self.obj_common.aca_wait_for_spinner()
            self.obj_aca_login.verify_logged_in()

        except Exception as e:
            print("Error : {}".format(e))


