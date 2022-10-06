from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers
import time


class DocumentUploadObjects:

    frm2 = (By.ID, "menuFrame")
    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")
    btn_Continue_doc_upload = (By.ID, "button-5")
    btn_Select_File = (By.ID, "button-2")
    txt_File_Name = (By.ID, "1148")
    btn_Open = (By.ID, "&Open")
    btn_Cancel = (By.ID, "Cancel")
    file_dialog = (By.ID, "uploadfiles")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    # if we upload document from new record that has only one iframe
    # Document upload from record section has two iframes. so we pass the section name here.
    def click_select_file(self, section):
        time.sleep(5)
        self.obj_wrapper.switch_to_window("Batch Upload")
        if section == "record":
            self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.change_control_visibility(self.file_dialog)

    def click_continue(self, section):
        self.obj_wrapper.click_button(self.btn_Continue_doc_upload, "Continue")
        self.obj_wrapper.switch_to_default()
        if section == "record":
            self.obj_wrapper.switch_to_default()
        time.sleep(5)

    def enter_file_name(self, file_name):
        self.obj_wrapper.key_press(self.file_dialog, file_name)

    def click_open(self):
        self.obj_wrapper.click_button(self.btn_Open, "Open")
