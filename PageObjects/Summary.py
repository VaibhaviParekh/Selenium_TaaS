from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class SummaryObjects:

    # All common objects of Summary portlet
    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")
    lbl_RecordID = (By.XPATH, "//span[contains(.,'Record ID:')]")
    lbl_Application_Status = (By.XPATH, "//th[contains(.,'Application Status:')]/..//td//a")
    lbl_Balance_Amount = (By.XPATH, "//th[contains(.,'Balance:')]/..//td")
    lbl_Assigned_to = (By.XPATH, "//th[contains(.,'Assigned To:')]/..//td")
    lbl_Application_Type = (By.XPATH, "//th[contains(.,'Application Type:')]/..//td//a")
    lbl_Application_Detail_Report = (By.XPATH, "//li//a[contains(.,'Application Detail Report')]")
    lnk_Reports = (By.ID, "reportMenu1Link")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    # On summary page we verify the details of the record
    def verify_record_id_value(self, record_id):
        self.obj_wrapper.switch_to_frame(self.frm1,"")
        value_record_id = self.obj_wrapper.get_text_for_webelement(self.lbl_RecordID, "Record ID")
        self.obj_wrapper.switch_to_default()
        if record_id == value_record_id:
            return True
        else:
            return False

    def verify_application_status_value(self, application_status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = self.obj_wrapper.object_exists(self.lbl_Application_Status, "Status")
        value_app_status = self.obj_wrapper.get_text_for_webelement(self.lbl_Application_Status, "Application Status")
        self.obj_wrapper.switch_to_default()
        if value_app_status == application_status:
            return True
        else:
            return False

    def verify_get_balance_amount_value(self, balance_amount):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        value_balance_amount = self.obj_wrapper.get_text_for_webelement(self.lbl_Balance_Amount, "Balance Amount")
        self.obj_wrapper.switch_to_default()
        if value_balance_amount == balance_amount:
            return True
        else:
            return False

    def verify_assigned_to_value(self, assigned_to):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        value_assigned_to = self.obj_wrapper.get_text_for_webelement(self.lbl_Assigned_to, "Assigned to")
        self.obj_wrapper.switch_to_default()
        if value_assigned_to == assigned_to:
            return True
        else:
            return False

    def verify_application_type_value(self, application_type):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        value_application_type = self.obj_wrapper.get_text_for_webelement(self.lbl_Application_Type, "Application Type")
        self.obj_wrapper.switch_to_default()
        if value_application_type == application_type:
            return True
        else:
            return False
