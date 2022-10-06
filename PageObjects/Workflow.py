from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By
from Common.Config import Config


class WorkflowObjects:
    # All common objects of workflow portlet
    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")
    frm2 = (By.ID, "workflow-iframe-1")

    # Workflow status selection and submission page objects

    lnk_Current_Dept = (By.LINK_TEXT, "Current Department")
    lnk_Current_User = (By.LINK_TEXT, "Current User")
    lbl_msg = (By.ID, "errorMsgPanel")
    btn_Menu = (By.ID, "menu1Link")
    btn_Help = (By.ID, "Help")
    btn_Submit = (By.ID, "acSubmit")
    btn_Assign = (By.ID, "assign")
    btn_Reset = (By.ID, "accelareset")
    btn_Calculate_Hour = (By.ID, "calculateHour")
    btn_Supervisor = (By.ID, "Supervisor")
    cbo_Action_By_Department = (By.ID, "value(department)")
    cbo_Action_By_Staff = (By.ID, "value(actionUser*userID)")
    cbo_Status = (By.ID, "value(taskItem*disposition)")
    cbo_Start_Time_Hours = (By.ID, "value(startHours)")
    cbo_Start_Time_Minute = (By.ID, "value(startMinutes)")
    cbo_End_Time_Hours = (By.ID, "value(endHours)")
    cbo_End_Time_Minute = (By.ID, "value(endMinutes)")
    txt_Status_Date = (By.ID, "date(taskItem*statusDate)")
    txt_Due_Date = (By.ID, "date(taskItem*dueDate)")
    txt_Hours_Spent = (By.ID, "value(hoursSpent)")
    txtarea_Comment = (By.ID, "value(taskItem*dispositionComment)")

    # Delete Worklfow history page objects
    btn_Delete_and_Submit_Workflow = (By.ID, "asnAndDelSubmit")
    rbo_Delete_Workflow_History_Yes = (By.ID, "value(isDeleteHistory)_1")
    rbo_Delete_Workflow_History_No = (By.ID, "value(isDeleteHistory)_2")
    btn_Save = (By.ID, "save")
    cbo_New_Workflow = (By.ID, "value(newWorkflow)")

    # Assign Department section workflow items page objects
    lnk_Delete_and_Assign_Workflow = (By.ID, "drop_asnAndDel")
    cbo_Department_Assign = (By.ID, "value(asgnDepValue)")
    cbo_Staff_Assign = (By.ID, "value(user*userID)")
    cbo_Workflow_Calendar = (By.ID, "date(dueDate)")
    txt_Due_Date_Assign = (By.ID, "value(calendarID)")
    btn_Submit_Assign = (By.ID, "acsubmit")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    # Select new status from dropdown
    def select_workflow_status(self, status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        control = self.obj_wrapper.object_exists(self.cbo_Status,"Status")
        if control == 1:
            self.obj_wrapper.select_value_from_dropdown(self.cbo_Status, "Status", status)
        else:
            print("Control doesn't exists")
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    # Select Department value
    def select_department_value(self, department):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Action_By_Department, "Action by Department",department)
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    # Click on Current Department Link
    def click_current_department(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.click_button(self.lnk_Current_Dept, "Current Department")
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    # Select Current User value
    def select_user_value(self, user):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Action_By_Staff, "Action by Staff", user)
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    # Click on current user link
    def click_current_user(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.click_button(self.lnk_Current_User, "Current User")
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    # Select status date value
    def enter_status_date(self,status_date):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.enter_text(self.txt_Status_Date, "Status Date", status_date)
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    # Enter standard Comment
    def enter_standard_comment(self, standard_comment):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.enter_text(self.txtarea_Comment, "Standard Comment", standard_comment)
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    # Select Start time hour value
    def select_start_time_hour(self, start_time_hour):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Start_Time_Hours, "Start time hour", start_time_hour)
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    # Select Start time minute value
    def select_start_time_minute(self, start_time_minute):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Start_Time_Minute, "Start time minute", start_time_minute)
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    # Select End time hour value
    def select_end_time_hour(self, end_time_hour):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_End_Time_Hours, "End time hour", end_time_hour)
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    # Select Start time minute value
    def select_end_time_minute(self, end_time_minute):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_End_Time_Minute, "End time minute", end_time_minute)
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    # Click on workflow submit button
    def click_submit_workflow(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")

        if Config.browser_type == "Ie":
            self.obj_wrapper.scroll_element(self.btn_Submit)
            submit_visible = self.obj_wrapper.object_exists(self.btn_Submit, "")
        self.obj_wrapper.click_button(self.btn_Submit, "Submit Workflow")
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    # Click on workflow Assign button
    def click_assign_workflow(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.click_button(self.btn_Assign, "Assign Workflow")
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    # Verify workflow task with given status exists or no
    def verify_workflow_task_exists(self, workflow_task, status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        workflow_task_control=(By.XPATH,"//span[.='" + workflow_task + "']/ancestor::div[2]//div/span[.='" + status +"']")
        value_workflow_task = self.obj_wrapper.object_exists(workflow_task_control, workflow_task + " : Workflow Task")
        self.obj_wrapper.switch_to_default()
        if value_workflow_task == 1:
            return True
        else:
            return False

    # Click on workflow task to expand it and expand the section
    def expand_workflow_task(self, workflow_task):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        workflow_task_control = (By.XPATH, "//span[.='" + workflow_task + "']")
        value_workflow_task = self.obj_wrapper.object_exists(workflow_task_control,workflow_task + " : Workflow Task")
        if value_workflow_task == 1:
            self.obj_wrapper.click_button(workflow_task_control, "Workflow task")
        self.obj_wrapper.switch_to_default()

    # Click on workflow task with given status and expand the section
    def expand_workflow_with_status(self, workflow_task, status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        workflow_task_control=(By.XPATH,"//span[.='" + workflow_task + "']/ancestor::div[2]//div/span[.='" + status +"']")
        value_workflow_task = self.obj_wrapper.object_exists(workflow_task_control, workflow_task + " : Workflow Task")
        if value_workflow_task == 1:
            self.obj_wrapper.click_button(value_workflow_task, "Workflow task")
        self.obj_wrapper.switch_to_default()

    # if workflow task isn't editable then the status combobox control isn't editable.
    def verify_workflow_task_not_editable(self, workflow_task, status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        workflow_task_control=(By.XPATH,"//span[.='" + workflow_task + "']/ancestor::div[2]//div/span[.='" + status +"']")
        value_workflow_task = self.obj_wrapper.object_exists(workflow_task_control, workflow_task + " : Workflow Task")
        self.obj_wrapper.switch_to_default()
        if value_workflow_task == 1:
            self.obj_wrapper.switch_to_frame(self.frm1, "")
            task_editable = self.obj_wrapper.object_exists(self.cbo_Status, "Status")
            self.obj_wrapper.switch_to_default()
            if task_editable == 1:
                return False
            else:
                return True

    # Expand the workflow section Completed Tasks, In Progress or Up Next
    def expand_workflow_section(self, workflow_section):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        section = (By.XPATH, "//span[.='" + workflow_section + "']")
        self.obj_wrapper.click_button(section, workflow_section+" workflow section")
        self.obj_wrapper.switch_to_default()

    # Get error message from workflow
    def verify_workflow_error(self, error_message):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        error = self.obj_wrapper.get_text_for_webelement(self.lbl_msg, "Message")
        pos = error_message.find(error)
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()
        if pos > 0:
            return True
        else:
            return False
