from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class StatusObjects:
    # Page Objects on Status Portlet

    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")
    btn_Save = (By.ID, "save")
    txt_Status_Date = (By.ID, "date(statusDate)")
    txtarea_Comments = (By.ID, "value(statusComment)")
    cbo_New_Status = (By.ID, "value(status)")
    cbo_Action_By_Department = (By.ID, "value(department)")
    cbo_Action_By_Staff = (By.ID, "value(sysuser*userID)")

    lnk_Current_Dept = (By.LINK_TEXT, "Current Department")
    lnk_Current_User = (By.LINK_TEXT, "Current User")

    lbl_msg = (By.ID, "err_msg")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_save(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Save, "Save")
        self.obj_wrapper.switch_to_default()

    def enter_status_date(self, status_date):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_Status_Date, "Status Date", status_date)
        self.obj_wrapper.switch_to_default()

    def enter_comments(self, comments):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txtarea_Comments, "Comments", comments)
        self.obj_wrapper.switch_to_default()

    def select_status(self, status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_New_Status,"New Status",status)
        self.obj_wrapper.switch_to_default()

    def select_department_value(self, department):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Action_By_Department, "Action by Department", department)
        self.obj_wrapper.switch_to_default()

    def click_current_department(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.lnk_Current_Dept,"Current Department")
        self.obj_wrapper.switch_to_default()

    def select_user_value(self, user):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Action_By_Staff, "Action by Staff", user)
        self.obj_wrapper.switch_to_default()

    def click_current_user(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.lnk_Current_User, "Current User")
        self.obj_wrapper.switch_to_default()

    def verify_status_updated(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        succ_msg = self.obj_wrapper.get_text_for_webelement(self.lbl_msg, "Renewal Info Success Message")
        self.obj_wrapper.switch_to_default()
        if succ_msg == "The Record Status updated successfully":
            return True
        else:
            return False

    def verify_status_value(self,status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        status_val = self.obj_wrapper.get_value(self.cbo_New_Status,"Status")
        self.obj_wrapper.switch_to_default()
        if status_val == status:
            return True
        else:
            return False

    def verify_date_value(self, date):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        status_date = self.obj_wrapper.get_value(self.txt_Status_Date, "Date")
        self.obj_wrapper.switch_to_default()
        if status_date == date:
            return True
        else:
            return False
