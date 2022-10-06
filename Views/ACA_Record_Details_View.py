from PageObjects.ACA_Record_Details import ACARecordDetailObject


class ACARecordDetailsView:

    def __init__(self, drv):
        # Create instance of the ACA Record Details Objects
        self.obj_driver = drv
        self.obj_record_details = ACARecordDetailObject(drv)

    def aca_verify_record_details(self, application_status, expiration_date):
        try:
            self.obj_record_details.verify_status(application_status)
            self.obj_record_details.verify_expiration_date(expiration_date)

        except Exception as e:
            print("Error : {}".format(e))