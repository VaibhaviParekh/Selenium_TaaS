from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class ApplicationSubmissionObjects:

    # Submit an application
    btn_Submit = (By.ID, "newCap")
    lbl_Validate_Message = (By.ID, "err_msg")
    btn_Cancel = (By.ID, "popWindowClose")
    div_success_msg = (By.CLASS_NAME, "success-message")
    btn_View_Summary = (By.ID, "button-5")
    btn_View_List = (By.ID, "button-8")

    def __init__(self, drv):
        # Create instance of Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_submit(self):
        self.obj_wrapper.click_button(self.btn_Submit, "Submit")

    def click_cancel(self):
        self.obj_wrapper.click_button(self.btn_Cancel, "Cancel")

    def verify_validation_message(self, message):
        msg = self.obj_wrapper.get_text_for_webelement(self.lbl_Validate_Message, "Validation Message")
        if msg.strip() == message:
            return True
        else:
            return False

    def verify_application_submitted(self):
        self.obj_wrapper.switch_to_window("Add SUPER success")
        msg = self.obj_wrapper.get_text_for_webelement(self.div_success_msg, "Success Message")
        if msg.strip() == "The new record was successfully submitted":
            return True
        else:
            return False

    def click_view_summary(self):
        self.obj_wrapper.click_button(self.btn_View_Summary, "View Summary")
        self.obj_wrapper.switch_to_window("Accela Automation")

