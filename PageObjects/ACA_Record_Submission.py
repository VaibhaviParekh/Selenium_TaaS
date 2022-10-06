from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ACARecordSubmissionObjects:

    lbl_record_no = (By.ID, "ctl00_PlaceHolderMain_addressList_ctl00_agenciesList_ctl00_capsList_ctl00_hlCAPDetail")
    lbl_success_msg = (By.ID, "ctl00_PlaceHolderMain_resultMessage_messageBar")
    lbl_condition = (By.CLASS_NAME, "ACA_Condition_Required ACA_Condition_Required_FontSize")
    view_record = (By.XPATH, "//span[.='View Record']")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def check_success_message(self):
        msg_exists = self.obj_wrapper.object_exists(self.lbl_success_msg,"Success Message")
        if msg_exists == 1:
            return True
        else:
            return False

    def get_record_id(self):
        record_id = self.obj_wrapper.get_text_for_webelement(self.lbl_record_no, "Record Number")
        return record_id

    def click_view_record(self):
        self.obj_wrapper.click_button(self.view_record, "View Record")

    def verify_condition_applied(self, condition):
        condition_val = self.obj_wrapper.get_text_for_webelement(self.lbl_condition,"Condition")
        if condition in condition_val:
            print("Condition verified successfully")
        else:
            print("Condition not verified successfully")