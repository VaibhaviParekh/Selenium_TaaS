from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers

class LogOutObjects:

    # Objects on Sign out menu option.

    frmFrame = (By.CSS_SELECTOR, "div#login_box>iframe")
    txtAgency = (By.ID, "servProvCode")
    expander_Menu = (By.CSS_SELECTOR, "div.user-profile-container>i.accelicons-chevron-down.user-profile-chevron")
    lnk_Administration = (By.LINK_TEXT, "Administration")
    lnk_Exit_Administration = (By.LINK_TEXT, "Exit Administration")
    lnk_Classic_Admin = (By.LINK_TEXT, "Classic Admin")
    lnk_Sign_Out = (By.LINK_TEXT, "Sign Out")
    lnk_Help = (By.LINK_TEXT, "Help")
    lnk_Switch_to_V360 = (By.LINK_TEXT, "Switch to V360")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_to_expand_menu(self):
        self.obj_wrapper.click_button(self.expander_Menu, "Expand Profile Menu")

    def click_administration(self):
        self.obj_wrapper.click_button(self.lnk_Administration, "Administration")

    def click_exit_administration(self):
        self.obj_wrapper.click_button(self.lnk_Exit_Administration, "Exit Administration")

    def click_classic_admin(self):
        self.obj_wrapper.click_button(self.lnk_Classic_Admin, "Classic Admin")

    def click_sign_out(self):
        self.obj_wrapper.click_button(self.lnk_Sign_Out, "Sign Out")

    def click_help(self):
        self.obj_wrapper.click_button(self.lnk_Help, "Help")

    def click_switch_v360(self):
        self.obj_wrapper.click_button(self.lnk_Switch_to_V360, "Switch to V360")
