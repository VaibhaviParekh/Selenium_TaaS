from PageObjects.Application_Submission import ApplicationSubmissionObjects

class ApplicationSubmissionView:

    def __init__(self, drv):
        # Create instance of the Application Submission Objects
        self.obj_driver = drv
        self.obj_app_submission = ApplicationSubmissionObjects(drv)

    # Verify application is submitted successfully
    def verify_successful_application_submission(self):
        try:
            success = self.obj_app_submission.verify_application_submitted()
            if success == 1:
                self.obj_app_submission.click_view_summary()
            else:
                print("Application not submitted successfully")

        except Exception as e:
            print("Error : {}".format(e))

    # Click on submit application
    def submit_application(self):
        try:
            self.obj_app_submission.click_submit()
        except Exception as e:
            print("Error : {}".format(e))