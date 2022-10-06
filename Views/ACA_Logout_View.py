from PageObjects.ACA_Login_Logout import ACALoginLogoutObject
from PageObjects.ACA_Common import ACACommonObject


class ACALogoutView:

    def __init__(self, drv):
        # Create instance of the Logout Page Objects
        self.obj_driver = drv
        self.obj_aca_login = ACALoginLogoutObject(drv)
        self.obj_common = ACACommonObject(drv)

    # Regular logout flow.
    def aca_logout(self):
        try:
            self.obj_aca_login.click_logout()
            self.obj_common.aca_wait_for_spinner()
            self.obj_aca_login.verify_logged_out()

        except Exception as e:
            print("Error : {}".format(e))


