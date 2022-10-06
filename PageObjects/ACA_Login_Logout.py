from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ACALoginLogoutObject:

    # Page Objects for Register User Page
    link_login = (By.ID, "ctl00_HeaderNavigation_lblLogin")
    txt_username = (By.ID, "ctl00_PlaceHolderMain_LoginBox_txtUserId")
    txt_password = (By.ID,"ctl00_PlaceHolderMain_LoginBox_txtPassword")
    btn_login = (By.ID,"ctl00_PlaceHolderMain_LoginBox_btnLogin")
    btn_logout = (By.ID,"ctl00_HeaderNavigation_com_headIsLoggedInStatus_label_logout")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_login_link(self):
        self.obj_wrapper.click_button(self.link_login, "Login Link")

    def enter_username(self, username):
        self.obj_wrapper.enter_text(self.txt_username, "ACA User Name", username)

    def enter_password(self, password):
        self.obj_wrapper.enter_text(self.txt_password, "ACA Password", password)

    def click_login_button(self):
        self.obj_wrapper.click_button(self.btn_login, "Login Button")

    def verify_logged_in(self):
        success = self.obj_wrapper.is_visible(self.btn_logout, "Success Login")
        if success == 1:
            print("Successfully logged into ACA")
        else:
            print("Error Logging into ACA")

    def click_logout(self):
        self.obj_wrapper.click_button(self.btn_logout, "Logout")

    def verify_logged_out(self):
        success = self.obj_wrapper.object_exists(self.txt_username, "Success Logout")
        if success == 1:
            print("Successfully logged out from ACA")
        else:
            print("Error Logging out from ACA")