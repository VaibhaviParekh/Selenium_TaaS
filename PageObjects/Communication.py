from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class CommunicationObjects:

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    # All page objects of Communication Portlet

    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")
    btn_Cancel = (By.ID, "cancel")
    lbl_No_Record = (By.CLASS_NAME, "portlet-msg-alert")
    lbl_Title = (By.ID, "formlayout-container-20")

    # Get the title content and verify the content
    def verify_email_content(self, title):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        email_title= self.obj_wrapper.get_text_for_webelement(self.lbl_Title, "Email Title")
        self.obj_wrapper.switch_to_default()
        if email_title == title:
            return True
        else:
            return False

    def click_cancel(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Cancel, "Cancel")
        self.obj_wrapper.switch_to_default()

    def verify_no_email_instance_exists(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        no_record = self.obj_wrapper.object_exists(self.lbl_No_Record, "No Record Exists")
        self.obj_wrapper.switch_to_default()
        if no_record == 1:
            return True
        else:
            return False

    def click_on_email_instance(self, event_code):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        email_title_link = (By.XPATH, "//tr/td[.='" + event_code +"']/../td[2]//a")
        self.obj_wrapper.click_button(email_title_link, "Event Code")
        self.obj_wrapper.switch_to_default()
