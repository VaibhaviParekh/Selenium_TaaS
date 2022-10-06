from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By
from Common.Config import Config


class InspectionResultObjects():

    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")

    txt_inspection_date = (By.ID, "date(activityModel*completionDate0)")
    cbo_inspection_status = (By.ID, "value(activityModel*status0)")
    txt_result_comment = (By.ID, "value(inspectionModel*resultComment0)")
    btn_save = (By.ID, "multEditNext")
    btn_cancel = (By.ID, "cancel")
    btn_send_email = (By.ID, "sendEmail")
    btn_cancel_email = (By.ID, "cancelEmail")
    txt_applicant_at = (By.ID, "value(contactEmail,0)")
    cbo_scheduled_start_time_hour = (By.ID, "value(startTimeHour0)")
    cbo_scheduled_start_time_minute = (By.ID, "value(startTimeMinute0)")
    cbo_scheduled_start_time_AMPM = (By.ID, "value(startTimeAMPM0)")
    cbo_department = (By.ID, "value(inspectorModel*deptOfUser0)")
    cbo_inspector = (By.ID, "value(inspectorModel*gaUserID0)")
    cbo_inspection_time_hour = (By.ID, "value(inspectionTimeHour0)")
    cbo_inspection_time_minute = (By.ID, "value(inspectionTimeMinute0)")
    cbo_inspection_time_AMPM = (By.ID, "value(inspectionTimeAMPM0)")
    lnk_Current_Dept = (By.LINK_TEXT, "Current Department")
    lnk_Current_User = (By.LINK_TEXT, "Current User")
    chk_display_in_ACA = (By.ID, "activityModel*displayinaca0")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def enter_inspection_date(self, date):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_inspection_date, "Inspection Date", date)
        self.obj_wrapper.switch_to_default()

    def select_inspection_status(self, inspection_status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_inspection_status, "Inspection Status", inspection_status)
        self.obj_wrapper.switch_to_default()

    def enter_result_comment(self, result_comment):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_result_comment, "Result Comment", result_comment)
        self.obj_wrapper.switch_to_default()

    def select_department_value(self, department):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_department, "Action by Department", department)
        self.obj_wrapper.switch_to_default()

    def click_current_department(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.lnk_Current_Dept, "Current Department")
        self.obj_wrapper.switch_to_default()

    def select_user_value(self, user):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_inspector, "Action by Staff", user)
        self.obj_wrapper.switch_to_default()

    def click_current_user(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.lnk_Current_User, "Current User")
        self.obj_wrapper.switch_to_default()

    def select_scheduled_start_time_hour(self, start_time_hour):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_scheduled_start_time_hour, "Scheduled Start Time Hour", start_time_hour)
        self.obj_wrapper.switch_to_default()

    def select_scheduled_start_time_minute(self, start_time_minute):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_scheduled_start_time_minute, "Scheduled start Time Minute", start_time_minute)
        self.obj_wrapper.switch_to_default()

    def select_start_time_ampm(self, start_time_am_pm):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_scheduled_start_time_AMPM, "Scheduled start Time AMPM" ,start_time_am_pm)
        self.obj_wrapper.switch_to_default()

    def inspection_time_hour(self, inspection_time_hour):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_inspection_time_hour, "Inspection time hour", inspection_time_hour)
        self.obj_wrapper.switch_to_default()

    def inspection_time_minute(self, inspection_time_min):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_inspection_time_minute, "Inspection Time Minute", inspection_time_min)
        self.obj_wrapper.switch_to_default()

    def inspection_time_ampm(self, inspection_time_ampm):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_inspection_time_AMPM, "Inspection time AMPM", inspection_time_ampm)
        self.obj_wrapper.switch_to_default()

    def check_display_in_ACA_checkbox(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_checkbox(self.chk_display_in_ACA)
        self.obj_wrapper.switch_to_default()

    def click_save(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        if Config.browser_type == "Ie":
            self.obj_wrapper.scroll_element(self.btn_save)
        self.obj_wrapper.click_button(self.btn_save, "Save")
        self.obj_wrapper.switch_to_default()

    def click_cancel(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_cancel, "Save")
        self.obj_wrapper.switch_to_default()

    def enter_applicant_email(self, email):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_applicant_at, "Applicant At", email)
        self.obj_wrapper.switch_to_default()

    def click_send_email(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_send_email, "Send Email")
        self.obj_wrapper.switch_to_default()

    def click_cancel_email(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_cancel_email, "Cancel Email")
        self.obj_wrapper.switch_to_default()