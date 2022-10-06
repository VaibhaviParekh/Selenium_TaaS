from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class RecordDetailsObjects:
    # After submission of record. Page objects from Record Portlet
    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")
    frm2 = (By.ID, "capList")

    btn_Menu = (By.ID, "menu1")
    btn_Save = (By.ID, "editSave")
    btn_Reset = (By.ID, "accelareset")
    btn_Summary = (By.ID, "capPopup")
    btn_Report = (By.ID, "reportMenu1Link")
    txt_ALT_ID = (By.ID, "value(capModel*altID)")
    txt_Opened_Date = (By.ID, "date(capModel*fileDate)")
    txt_Application_Name = (By.ID, "value(capModel*specialText)")
    txt_Status = (By.ID, "value(capModel*capStatus)")
    txt_Record_Type = (By.ID, "value(capType)")
    txt_Short_Notes = (By.ID, "value(capDetailModel*shortNotes)")
    txt_Total_Fees_Invoiced = (By.ID, "value(capDetailModel*totalFee)")
    txt_Total_Pay = (By.ID, "value(capDetailModel*totalPay)")
    txt_Balance = (By.ID, "value(capDetailModel*balance)")
    txt_Assigned_Date = (By.ID, "date(capDetailModel*asgnDate)")
    txtarea_Detailed_Description = (By.ID, "value(capWorkDescriptionModel*description)")
    cbo_Department = (By.ID, "value(capDetailModel * asgnDept)")
    cbo_User = (By.ID, "value(capDetailModel * asgnStaff)")
    lbl_msg = (By.ID, "err_msg")

    div_Condition = (By.ID, "_$conditionDiv")
    lnk_asgn_dept = (By.LINK_TEXT, "Current Department")
    lnk_asgn_user = (By.LINK_TEXT, "Current User")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_save(self):
        self.obj_wrapper.switch_to_frame(self.frm1)
        self.obj_wrapper.click_button(self.btn_Save, "Save")
        self.obj_wrapper.switch_to_default()

    def click_summary(self):
        self.obj_wrapper.switch_to_frame(self.frm1)
        self.obj_wrapper.click_button(self.btn_Summary, "Summary")
        self.obj_wrapper.switch_to_default()

    def click_report(self):
        self.obj_wrapper.switch_to_frame(self.frm1)
        self.obj_wrapper.click_button(self.btn_Report, "Report")
        self.obj_wrapper.switch_to_default()

    def click_condition(self):
        self.obj_wrapper.switch_to_frame(self.frm1)
        self.obj_wrapper.click_button(self.div_Condition, "Condition")
        self.obj_wrapper.switch_to_default()

    def get_record_value(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        record_id = self.obj_wrapper.get_value(self.txt_ALT_ID, "Record ID")
        self.obj_wrapper.switch_to_default()
        return record_id


    def verify_record_id(self, record_id):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        record_number = self.obj_wrapper.get_value(self.txt_ALT_ID, "Record ID")
        self.obj_wrapper.switch_to_default()
        if record_id == record_number:
            return True
        else:
            return False

