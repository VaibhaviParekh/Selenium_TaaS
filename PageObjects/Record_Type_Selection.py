import time

from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class RecordTypeSelectionPageObjects:

    lbl_page_caption = (By.CSS_SELECTOR, "div.row>div>h1")
    txt_search_type = (By.ID, "txtRecordType")
    btn_create = (By.ID, "btnCreateApplication")

    def __init__(self, drv):
        # Create instance of Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def select_record_type(self, rec_type):
        self.obj_wrapper.switch_to_window("Select Record Type")
        lbl_record_type = (By.CSS_SELECTOR, "li[data-alias='" + rec_type + "']>div>span")
        self.obj_wrapper.enter_text(self.txt_search_type, "Record Type", rec_type)
        self.obj_wrapper.click_button(lbl_record_type, "Record Type Select")
        # Doesn't click for the first time for some reason so clicking twice so the Create Application button becomes enabled
        # A bit erratic application behavior. But ideally should not need this double click.
        self.obj_wrapper.click_button(lbl_record_type, "Record Type Select")

    def click_create(self):
        self.obj_wrapper.click_button(self.btn_create, "Create Application")
        self.obj_wrapper.switch_to_window("Accela Automation")


