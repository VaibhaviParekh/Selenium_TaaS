from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ACARecordTypeSelectionObject:

    # Page Objects for Register User Page
    txt_search_record = (By.ID, "ctl00_PlaceHolderMain_recordTypeFilterSelection_txtSearch")
    btn_search_record = (By.ID, "ctl00_PlaceHolderMain_recordTypeFilterSelection_btnSearch")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def enter_record_type(self, record_type):
        self.obj_wrapper.enter_text(self.txt_search_record, "Search Record", record_type)

    def click_search_record_type(self):
        self.obj_wrapper.click_button(self.btn_search_record, "Button Search Record")

    def select_record_type(self, sub_type, record_type):
        record_type_control = (By.XPATH, "//span[.='" + sub_type + "']//ancestor::div[2]//label[.='" + record_type + "']//..//input")
        self.obj_wrapper.click_checkbox(record_type_control)

    def verify_record_type_exists(self, sub_type, record_type):
        record = (By.XPATH, "//span[.='" + sub_type + "']//ancestor::div[2]//label[.='" + record_type + "']")
        exists = self.obj_wrapper.object_exists(record, "Record Type")
        if exists == 1:
            return True
        else:
            return False