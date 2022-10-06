
from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By
import time

class LoginPageObjects:
    frmFrame = (By.CSS_SELECTOR, "div#login_box>iframe")
    txtAgency = (By.ID, "servProvCode")
    txtUser = (By.ID, "username")
    txtPassword = (By.NAME, "password")
    btnLogin = (By.ID, "submit_")
    btnUserProfile = (By.CLASS_NAME, "user-profile-menu")

    def __init__(self, drv):
        # Create instance of Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def enter_agency(self, agency):
        self.obj_wrapper.switch_to_frame(self.frmFrame, "")
        self.obj_wrapper.enter_text(self.txtAgency, "Agency", agency)
        self.obj_wrapper.key_press(self.txtAgency, "TAB")

    def enter_user(self, user):
        self.obj_wrapper.enter_text(self.txtUser, "User Name", user)

    def enter_password(self, pwd):
        self.obj_wrapper.enter_text(self.txtPassword, "Password", pwd)

    def click_login(self):
        self.obj_wrapper.click_button(self.btnLogin, "Login")
        self.obj_wrapper.switch_to_default()

    def check_login(self):
        return self.obj_wrapper.is_visible(self.btnUserProfile, "Dashboard Page")

    def verify_successful_logout(self):
        self.obj_wrapper.switch_to_frame(self.frmFrame, "")
        exists = self.obj_wrapper.object_exists(self.txtAgency, "Login Page")
        self.obj_wrapper.switch_to_default()
        return exists
