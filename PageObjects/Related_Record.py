from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class RelatedRecordObject:

    # Page Objects for Related Record portlet
    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")

    btn_clone_single = (By.ID,"capTypePopup")
    btn_clone_multiple = (By.ID,"Clone Mult")
    btn_continue_clone_option = (By.ID,"continue")
    lbl_message = (By.ID,"err_msg")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_clone_single(self):
        self.obj_wrapper.switch_to_frame(self.frm1,"")
        self.obj_wrapper.click_button(self.btn_clone_single, "Clone Single")
        self.obj_wrapper.switch_to_default()

    def click_clone_multiple(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_clone_multiple, "Clone Multiple")
        self.obj_wrapper.switch_to_default()

    def select_record(self, record_type):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        record = (By.XPATH, "//span[contains(.,'" + record_type + "')]//..//..//input")
        self.obj_wrapper.click_checkbox(record)
        self.obj_wrapper.switch_to_default()

    def select_clone_options(self, clone_option):
        self.obj_wrapper.switch_to_window("Select Clone Options")
        select_option = (By.XPATH, "//label[.='" + clone_option + "']//..//input")
        self.obj_wrapper.click_checkbox(select_option)

    def click_continue_clone(self):
        self.obj_wrapper.click_button(self.btn_continue_clone_option, "Continue")

    def read_related_record(self, record_type):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        related_record = (By.XPATH, "//span[contains(.,('" + record_type + "')]")
        self.obj_wrapper.get_text_for_webelement(related_record, "Related Record")
        self.obj_wrapper.switch_to_default()

    def click_related_record(self, record_type):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        related_record = (By.XPATH, "//span[contains(.,('" + record_type + "')]")
        self.obj_wrapper.click_button(related_record, "Related Record")
        self.obj_wrapper.switch_to_default()

    def verify_related_record(self, record_type):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        related_record = (By.XPATH, "//span[contains(.,('" + record_type + "')]")
        exists = self.obj_wrapper.object_exists(related_record, "Related Record")
        if exists == 1:
            return True
        else:
            return False
        self.obj_wrapper.switch_to_default()