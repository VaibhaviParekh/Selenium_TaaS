from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers
import time

class ACARecordSearchObject:

    # Page Objects for Register User Page
    cbo_record_type = (By.ID, "ctl00_PlaceHolderMain_generalSearchForm_ddlGSPermitType")
    txt_record_number = (By.ID, "ctl00_PlaceHolderMain_generalSearchForm_txtGSPermitNumber")
    btn_record_search = (By.ID, "ctl00_PlaceHolderMain_btnNewSearch")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def select_record_type(self, record_type):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_record_type, "Select Record Type", record_type)
        time.sleep(5)

    def enter_record_id(self, record_id):
        self.obj_wrapper.enter_text(self.txt_record_number, "Enter Record ID", record_id)

    def click_record_search(self):
        self.obj_wrapper.click_button(self.btn_record_search, "Record Search")


