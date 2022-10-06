from PageObjects.ACA_Record_Submission import ACARecordSubmissionObjects
from PageObjects.ACA_Common import ACACommonObject

class ACARecordSubmissionView:

    def __init__(self, drv):
        # Create instance of the ACA Login Page Objects
        self.obj_driver = drv
        self.obj_aca_record_submit = ACARecordSubmissionObjects(drv)
        self.obj_common = ACACommonObject(drv)

    def aca_verify_record_submitted(self):
        success = self.obj_aca_record_submit.check_success_message()
        if success == 1:
            permit_id = self.obj_aca_record_submit.get_record_id()
            print("Record submitted successfully")
            return permit_id
        else:
            print("Record not submitted successfully")

    def aca_verify_condition_applied(self, condition):
        self.obj_aca_record_submit.verify_condition_applied(condition)

    def aca_view_record(self):
        self.obj_aca_record_submit.click_view_record()