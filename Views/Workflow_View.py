from PageObjects.Workflow import WorkflowObjects


class WorkflowView:

    def __init__(self,drv):
        # Initialize an instance of a class
        self.obj_drive=drv
        self.obj_workflow = WorkflowObjects(drv)

    # Verify the workflow status against workflow task. in progress, Issuued etc.
    # Expand Section ex. Completed Task, Upcoming Task etc.
    def verify_workflow_status(self, workflow_task, workflow_status, expand_section):
        try:
            if expand_section != "":
                self.obj_workflow.expand_workflow_section(expand_section)
            if self.obj_workflow.verify_workflow_task_exists(workflow_task, workflow_status):
                print("Workflow task " + workflow_task + " successfully verified to status " + workflow_status)
            else:
                print("Workflow task " + workflow_task + " not verified to status " + workflow_status)

        except Exception as e:
            print("Error : {}".format(e))

    # If condition is applied to the record workflow tasks are locked for edit. No textbox or edit controls are visible
    def verify_workflow_task_is_not_editable(self,workflow_task, workflow_status, expand_section):
        try:
            self.obj_workflow.expand_workflow_section(expand_section)
            if self.obj_workflow.verify_workflow_task_not_editable(workflow_task,workflow_status):
                print("Workflow task " + workflow_task + " isn't editable.")
            else:
                print("Workflow task " + workflow_task +" is editable.")

        except Exception as e:
            print("Error : {}".format(e))

    # Update the given workflow task to specific status
    def update_workflow_task(self, workflow_task, workflow_status, status_date, comment, department,user, due_date, start_time_hour, start_time_min, end_time_hour, end_time_min, submit_workflow='yes'):
        try:
            self.obj_workflow.expand_workflow_task(workflow_task)
            self.obj_workflow.select_workflow_status(workflow_status)
            self.obj_workflow.enter_status_date(status_date)
            self.obj_workflow.enter_standard_comment(comment)

            if department != "":
                if department == "current":
                    self.obj_workflow.click_current_department()
                else:
                    self.obj_workflow.select_department_value(department)

            if user != "":
                if user == "current":
                    self.obj_workflow.click_current_user()
                else:
                    self.obj_workflow.select_user_value(user)

            self.obj_workflow.select_start_time_hour(start_time_hour)
            self.obj_workflow.select_start_time_minute(start_time_min)
            self.obj_workflow.select_end_time_hour(end_time_hour)
            self.obj_workflow.select_end_time_minute(end_time_min)

            if submit_workflow == "yes":
                self.obj_workflow.click_submit_workflow()

        except Exception as e:
            print("Error : {}".format(e))

    # Verify the error message while updating the workflow
    def verify_workflow_error_message(self, error_message):
        try:
            error_verified = self.obj_workflow.verify_workflow_error(error_message)
            if error_verified == 1:
                print("Error message verified successfully to " + error_message)
            else:
                print("Error message not verified")

        except Exception as e:
            print("Error : {}".format(e))