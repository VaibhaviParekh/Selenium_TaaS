from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers
import math


class ClassicAdminCommonPageObjects:

    # There are some common things that we use across auto config
    # No Result is found after search of any data
    # If any error appear then a message window appears. We need to verify if that occurs

    lbl_no_record = (By.CLASS_NAME, "NoRecord")
    btn_Save = (By.NAME, "Save")  # Save data
    btn_Cancel = (By.XPATH, "//img[@alt='Cancel']")
    btn_Submit = (By.NAME, "Submit")  # Submit after search
    btn_Submit_Data = (By.XPATH, "//img[@alt='Submit']")
    btn_Search_New = (By.XPATH, "//img[@alt='New Search']")
    btn_Search = (By.XPATH, "//img[@alt='Search']")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def no_record_found(self):
        no_record = self.obj_wrapper.object_exists(self.lbl_no_record, "No Record")
        if no_record == 1:
            return True
        else:
            return False

    def mesage_window_exists(self):
        exists = self.obj_wrapper.window_exists("", "Message from Webpage")
        if exists == 1:
            return True
        else:
            return False

    def does_alert_exists(self):
        alert_exists = self.obj_wrapper.alert_exists()
        if alert_exists == 1:
            return True
        else:
            return False

    def handle_alert(self):
        self.obj_wrapper.close_browser_alert()

    def read_alert_text(self):
        alert_text = self.obj_wrapper.get_text_alert()
        return alert_text

    def click_save(self):
        self.obj_wrapper.click_button(self.btn_Save, "Save")

    def click_cancel(self):
        self.obj_wrapper.click_button(self.btn_Cancel, "Cancel")

    def click_search_new(self):
        self.obj_wrapper.click_button(self.btn_Search_New, "Search")

    def click_search(self):
        self.obj_wrapper.click_button(self.btn_Search, "Search")

    # Submit after Search
    def click_submit(self):
        self.obj_wrapper.click_button(self.btn_Submit, "Submit")

    def click_submit_data(self):
        self.obj_wrapper.click_button(self.btn_Submit_Data, "Submit")

    # Original Window is same. So putting this into common
    def switch_to_original_window(self):
        self.obj_wrapper.switch_to_window("Accela Automation")