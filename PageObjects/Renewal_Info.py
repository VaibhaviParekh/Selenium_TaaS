from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class RenewalInfoObject:

    # Page Objects for Renewal Information portlet
    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")
    btn_Save = (By.ID, "Save")
    btn_Reset = (By.ID, "accelareset")
    cbo_Expiration_Status = (By.ID, "value(expStatus)")
    txt_Expiration_Date = (By.ID, "date(expDate)")
    lbl_msg = (By.ID, "errorMsgPanel")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def save_renewal_info(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Save, "Save")
        self.obj_wrapper.switch_to_default()

    def enter_expiration_date(self, expiration_date):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        temp = self.obj_wrapper.object_exists(self.txt_Expiration_Date,"Date")
        if temp == 1:
            self.obj_wrapper.enter_text(self.txt_Expiration_Date, "Expiration Date", expiration_date)
        else:
            print("Date not present")
        self.obj_wrapper.switch_to_default()

    def select_expiration_status(self, expiration_status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        temp1 = self.obj_wrapper.object_exists(self.cbo_Expiration_Status, "Expiration Status")
        if temp1 == 1:
            self.obj_wrapper.select_value_from_dropdown(self.cbo_Expiration_Status, "Expiration Status", expiration_status)
        else:
            print("Status not present")
        self.obj_wrapper.switch_to_default()

    def verify_renewal_info_updated(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        succ_msg = self.obj_wrapper.get_text_for_webelement(self.lbl_msg, "Renewal Info Success Message")
        self.obj_wrapper.switch_to_default()
        if succ_msg == "Renewal Info updated successfully.":
            return True
        else:
            return False

    def verify_expiration_date_value(self, expiration_date):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        value_expiration_date=self.obj_wrapper.get_value(self.txt_Expiration_Date, "Expiration Date")
        self.obj_wrapper.switch_to_default()
        if value_expiration_date == expiration_date:
            return True
        else:
            return False

    def verify_expiration_status_value(self, expiration_status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        value_expiration_status=self.obj_wrapper.get_value(self.cbo_Expiration_Status, "Expiration Status")
        self.obj_wrapper.switch_to_default()
        if value_expiration_status == expiration_status:
            return True
        else:
            return False





