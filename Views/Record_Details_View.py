from PageObjects.Record_Details import RecordDetailsObjects

class RecordDetailsView:

    PERMIT_ID = ""

    def __init__(self, drv):
        # Create an instance of the class
        self.obj_driver=drv
        self.obj_record_details = RecordDetailsObjects(drv)

    def verify_record_id(self, record_id):
        try:
            if self.obj_record_details.verify_record_id(record_id):
                print("Record ID: " + record_id + " verified successfully.")
            else:
                print("Unable to verify record id: " + record_id)
        except Exception as e:
            print("Error : {}".format(e))

    def get_record_id(self):
        try:
            self.PERMIT_ID = self.obj_record_details.get_record_value()
            return self.PERMIT_ID
        except Exception as e:
            print("Error : {}".format(e))

    def generate_report(self):
        try:
            self.obj_record_details.click_report()
        except Exception as e:
            print("Error : {}".format(e))

