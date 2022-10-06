from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By
from Common.Config import Config

class CashierSessionObjects:

    # Cashier Session Window
    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")
    frm2 = (By.ID, "dialog-body")
    frm3 = (By.ID, "inspectionsFrame")

    btn_continue_session = (By.ID, "restart")
    btn_cancel = (By.ID, "popWindowClose")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_continue_session(self):
        self.obj_wrapper.switch_to_window("Cashier Session")
        if Config.browser_type == "Chrome":
            self.obj_wrapper.switch_to_frame(self.frm1, "")
            self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.switch_to_frame(self.frm3, "")
        self.obj_wrapper.click_button(self.btn_continue_session, "Continue Session")

    def click_cancel(self):
        self.obj_wrapper.click_button(self.btn_cancel, "Cancel")
        self.obj_wrapper.switch_to_window("Accela Automation")
        self.obj_wrapper.switch_to_default()
        if Config.browser_type == "Chrome":
            self.obj_wrapper.switch_to_default()
            self.obj_wrapper.switch_to_default()