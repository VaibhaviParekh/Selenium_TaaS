from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ClassicAdminLoginLogoutObjects:

    # Page Objects related to Login Logout from classic admin

    lnk_Logout = (By.LINK_TEXT, "Logout")
    txt_username = (By.ID, "userID")
    txt_password = (By.ID, "passwordID")
    btn_login = (By.ID, "submit")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_logout(self):
        self.obj_wrapper.click_button(self.lnk_Logout, "Logout")

    def verify_success_logout(self):
        exists = self.obj_wrapper.object_exists(self.txt_username, "Success Logout")
        if exists == 1:
            return True
        else:
            return False

    def enter_username(self, username):
        self.obj_wrapper.enter_text(self.txt_username, "Username")

    def enter_password(self, password):
        self.obj_wrapper.enter_text(self.txt_password, "Password")
    
    def click_login(self):
        self.obj_wrapper.click_button(self.btn_login, "Login")

    def verify_success_login(self):
        exists = self.obj_wrapper.object_exists(self.lnk_Logout, "Success Login")
        if exists == 1:
            return True
        else:
            return False
