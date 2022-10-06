from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ACACommonObject:

    # Page Objects common in ACA
    spinner = (By.ID, "divGlobalLoading")
    btn_continue_application = (By.LINK_TEXT, "Continue Application »")
    chk_disclaimer = (By.ID, "ctl00_PlaceHolderMain_termAccept")
    cbo_license =(By.ID, "ctl00_PlaceHolderMain_ddlLicenseID")
    lbl_error = (By.ID, "messageSpan_messages")


    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def aca_wait_for_spinner(self):
        self.obj_wrapper.is_not_visible(self.spinner, "Loading Icon")

    def click_continue_application(self):
        self.obj_wrapper.click_button(self.btn_continue_application, "Continue Application")

    def check_disclaimer(self):
        self.obj_wrapper.click_checkbox(self.chk_disclaimer)

    def select_license(self, license):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_license, "License", license)

    def verify_error_message(self, message):
        msg = self.obj_wrapper.get_text_for_webelement(self.lbl_error, "Error")

        if msg in message:
            print("Error verified successfully")
        else:
            print("Error not verified successfully. It is "+ msg)

    def select_menu(self, menu):
        control = (By.XPATH, "//a[.='" + menu + "']")
        temp = self.obj_wrapper.object_exists(control, "Control")
        self.obj_wrapper.click_button(control, "Menu")

    def select_sub_menu(self, sub_menu):
        control = (By.XPATH, "//a[contains(.,'" + sub_menu + "')]")
        temp = self.obj_wrapper.object_exists(control, "Control")
        self.obj_wrapper.click_button(control, "Sub Menu")