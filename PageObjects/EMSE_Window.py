from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class EMSEObjects:

    # All common objects of EMSE Window
    lbl_message = (By.XPATH, "//table[@id='displayBody']//tbody//table//td[contains(.,'Action Cancelled')]")
    btn_cancel = (By.ID, "popWindowClose")


    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    # On EMSE Window get message and verify
    def verify_emse_message(self, message):
        self.obj_wrapper.switch_to_window("EMSE Message List")
        value_emse_message = self.obj_wrapper.get_text_for_webelement(self.lbl_message, " EMSE Message")
        pos = value_emse_message.find(message)
        if pos > 0:
            return True
        else:
            return False

    # Click on Cancel button
    def click_cancel(self):
        self.obj_wrapper.click_button(self.btn_cancel, "Cancel")
        self.obj_wrapper.switch_to_window("Accela Automation")

