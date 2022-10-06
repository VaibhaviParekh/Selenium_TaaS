from PageObjects.Intake_Record_Details import IntakeRecordDetailObjects


class IntakeRecordDetailsView:

    def __init__(self, drv):
        # Create instance of the Record Details Objects
        self.obj_driver = drv
        self.obj_record_details = IntakeRecordDetailObjects(drv)

    def enter_record_details(self, application_name, description):
        try:
            self.obj_record_details.enter_application_name(application_name)
            self.obj_record_details.enter_description(description)

        except Exception as e:
            print("Error : {}".format(e))