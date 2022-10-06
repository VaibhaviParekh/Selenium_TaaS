from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By
from Common.Config import Config
import time

class InspectionObjects:

    # All common objects of Inspection portlet
    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")
    frm2 = (By.ID, "dialog-body")
    frm3 = (By.ID, "inspectionsFrame")
    frm4 = (By.ID, "inspectionList")
    frm5 = (By.ID, "menuFrame")
    lbl_message = (By.CLASS_NAME, "portlet-msg-alert")

    menu = (By.ID, "menu1Link")
    btn_manage_inspection = (By.ID, "resultMenu1Link")
    btn_delete = (By.ID, "delete")
    btn_search = (By.ID, "search")
    link_schedule_inspections = (By.XPATH, "//div[@id='dropMenu-5']//a[contains(.,'Schedule Inspections')]")
    link_result_inspections = (By.XPATH, "//div[@id='dropMenu-5']//a[contains(.,'Result Inspections')]")

    # All elements to schedule the inspection
    # Schedule Inspection
    move_right_all = (By.NAME, "move_right_all")
    move_right = (By.NAME, "move_right")
    move_left = (By.NAME, "move_left")
    move_left_all = (By.NAME, "move_left_all")
    cbo_inspection_group = (By.ID, "inspGroupSelector")
    btn_schedule_inspection = (By.ID, "acsubmit")
    btn_pending_inspection = (By.ID, "Pending")
    txt_inspection_schedule_date = (By.ID, "scheduledDateAll")
    cbo_department = (By.NAME, "value(deptOfUserAll)")
    lnk_Current_Dept = (By.LINK_TEXT, "Current Department")
    cbo_user = (By.NAME, "value(gaUserIDAll)")
    lnk_Current_User = (By.LINK_TEXT, "Current User")
    btn_submit = (By.ID, "acsubmit")
    btn_OK = (By.ID, "button-2")
    btn_Cancel = (By.ID, "button-5")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    # select the Schedule Inspection option
    def click_schedule_inspection_from_menu(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_manage_inspection, "Manage Inspection")
        time.sleep(3)
        abc = self.obj_wrapper.object_exists(self.link_schedule_inspections, "")
        self.obj_wrapper.click_button(self.link_schedule_inspections, "Schedule Inspection")
        self.obj_wrapper.switch_to_default()

    # Select the Result Inspection option
    def click_result_inspection_from_menu(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_manage_inspection, "Manage Inspection")
        self.obj_wrapper.click_button(self.link_result_inspections, "Result Inspection")
        self.obj_wrapper.switch_to_default()

    # Click the inspection link from the list
    def click_inspection_link(self, inspection_name, inspection_status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//a[.='" + inspection_name + "']//..//..//td[contains(.,'" + inspection_status + "')]//..//a")
        self.obj_wrapper.click_button(control, "Inspection Link")
        self.obj_wrapper.switch_to_default()

    # Click on checkbox against an inspection
    def click_inspection_checkbox(self, inspection_name, inspection_status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//table[@id='AccelaMainTable']//tr//td[contains(.,'" + inspection_name + "')]//..//td[contains(.,'" + inspection_status + "')]//..//input")
        self.obj_wrapper.click_checkbox(control)
        self.obj_wrapper.switch_to_default()

    # Verify Inspection in the List
    def verify_inspection(self, inspection_name, inspection_status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//table[@id='AccelaMainTable']//tr//td[contains(.,'" + inspection_name + "')]/../td[contains(.,'" + inspection_status + "')]")
        inspection = self.obj_wrapper.object_exists(control, "Inspection in List")
        self.obj_wrapper.switch_to_default()
        if inspection == 1:
            return True
        else:
            return False

    # Verify date of an inspection from the list against given inspection
    def verify_inspection_date(self, inspection_name, inspection_status, inspection_date):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//table[@id='AccelaMainTable']//tr//td[contains(.,'" + inspection_name + "')]/../td[contains(.,'" + inspection_status + "')]/..//td[contains(.,'" + inspection_date + "')]")
        date = self.obj_wrapper.object_exists(control, "Inspection in List")
        self.obj_wrapper.switch_to_default()
        if date == 1:
            return True
        else:
            return False

    # Verify Department of an inspection against given inspection in the list
    def verify_inspection_department(self, inspection_name, inspection_status, department):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//table[@id='AccelaMainTable']//tr//td[contains(.,'" + inspection_name + "')]/../td[contains(.,'" + inspection_status + "')]/..//td[contains(.,'" + department + "')]")
        dept = self.obj_wrapper.object_exists(control, "Inspection in List")
        self.obj_wrapper.switch_to_default()
        if dept == 1:
            return True
        else:
            return False

    # Verify User of an inspection against given inspection in the list
    def verify_inspection_user(self, inspection_name, inspection_status, user):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//table[@id='AccelaMainTable']//tr//td[contains(.,'" + inspection_name + "')]/../td[contains(.,'" + inspection_status + "')]/..//td[contains(.,'" + user + "')]")
        dept_user = self.obj_wrapper.object_exists(control, "Inspection in List")
        self.obj_wrapper.switch_to_default()
        if dept_user == 1:
            return True
        else:
            return False

    # Select the Inspection group under which main inspection is to be scheduled
    def select_inspection_group(self, inspection_group):
        self.obj_wrapper.switch_to_window("Inspection")
        if Config.browser_type == "Chrome":
            self.obj_wrapper.switch_to_frame(self.frm1, "")
            self.obj_wrapper.switch_to_frame(self.frm2, "")

        self.obj_wrapper.switch_to_frame(self.frm3, "")
        abc = self.obj_wrapper.object_exists(self.cbo_inspection_group, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_inspection_group, "Inspection Group", inspection_group)

    # Select the inspection that is to be scheduled
    def select_inspection_from_list(self, inspection_group, inspection_name):
        inspection = (By.XPATH, "//td[.='" + inspection_group + "']//..//td[.='" + inspection_name + "']")
        axyzbc = self.obj_wrapper.object_exists(inspection, "")
        self.obj_wrapper.click_button(inspection, "Inspection from the list")

    # Move inspection to Right side in the list to schedule
    def move_inspection_to_right(self):
        self.obj_wrapper.click_button(self.move_right, "Move Right")

    # Schedule inspection on a window
    def click_schedule_inspection(self):
        self.obj_wrapper.click_button(self.btn_schedule_inspection, "Schedule Inspection")
        self.obj_wrapper.switch_to_default()

    def click_pending_inspection(self):
        self.obj_wrapper.click_button(self.btn_pending_inspection, "Pending Inspection")
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    def enter_schedule_inspection_date(self, date):
        self.obj_wrapper.switch_to_window("Inspection")
        if Config.browser_type == "Chrome":
            self.obj_wrapper.switch_to_frame(self.frm1, "")
            self.obj_wrapper.switch_to_frame(self.frm2, "")

        self.obj_wrapper.switch_to_frame(self.frm3, "")
        self.obj_wrapper.switch_to_frame(self.frm4, "")
        self.obj_wrapper.enter_text(self.txt_inspection_schedule_date, "Inspection schedule date", date)

    def select_department_value(self, department):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_department, "Action by Department", department)

    def click_current_department(self):
        self.obj_wrapper.click_button(self.lnk_Current_Dept, "Current Department")

    def select_user_value(self, user):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_user, "Action by Staff", user)

    def click_current_user(self):
        self.obj_wrapper.click_button(self.lnk_Current_User, "Current User")

    def click_submit(self):
        temp = self.obj_wrapper.object_exists(self.btn_submit, "Sub")
        self.obj_wrapper.click_button(self.btn_submit, "Submit")
        if Config.browser_type == "Chrome":
            self.obj_wrapper.switch_to_default()
            self.obj_wrapper.switch_to_default()

        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    def message_from_webpage_click_OK(self):
        self.obj_wrapper.switch_to_window("Result Message")
        if Config.browser_type == "Chrome":
            self.obj_wrapper.switch_to_frame(self.frm1, "")
            self.obj_wrapper.switch_to_frame(self.frm2, "")

        self.obj_wrapper.switch_to_frame(self.frm3, "")
        self.obj_wrapper.switch_to_frame(self.frm5, "")
        self.obj_wrapper.click_button(self.btn_OK, "OK")

        self.obj_wrapper.switch_to_window("Accela Automation")
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

        if Config.browser_type == "Chrome":
            self.obj_wrapper.switch_to_default()
            self.obj_wrapper.switch_to_default()


    def handle_alert(self):
        self.obj_wrapper.close_browser_alert()
