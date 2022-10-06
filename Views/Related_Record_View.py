from PageObjects.Related_Record import RelatedRecordObject


class RelatedRecordView:

    # Create an instance of class
    def __init__(self, drv):
        self.obj_driver = drv
        self.obj_renewal_info = RelatedRecordObject(drv)

    # Read the related record id. Pass the type of record ex. Building,Commercial,Alteration,NA
    def read_related_record(self, record_type):
        try:
            exists = self.obj_renewal_info.verify_related_record(record_type)
            if exists == 1:
                related_record = self.obj_renewal_info.read_related_record(record_type)
                return related_record
            else:
                print("Unable to find Related Record")

        except Exception as e:
            print("Error : {}".format(e))

    # Verify Related Record exists in the tab
    def verify_related_record(self, record_type):
        try:
            exists = self.obj_renewal_info.verify_related_record(record_type)
            if exists == 1:
                print("Related Record of type " + record_type + " verified successfully")
            else:
                print("Unable to find Related Record")

        except Exception as e:
            print("Error : {}".format(e))

    # Select given record type and clone the record.
    # record type can be an permit number or record type ex. Building,Commercial,Alteration,NA
    # Any unique field through which we can find correct element to clone
    def clone_single_record(self, record_type):
        try:
            self.obj_renewal_info.click_related_record(record_type)
            self.obj_renewal_info.click_clone_single()

        except Exception as e:
            print("Error : {}".format(e))

     # Pass clone option ex. Fee, Custom Fields etc. The same name from UI
    def select_clone_options(self, clone_option):
        try:
            self.obj_renewal_info.select_clone_options(clone_option)

        except Exception as e:
            print("Error : {}".format(e))

    # Continue button on Related record option selection
    def click_continue_on_related_record_option(self):
        try:
            self.obj_renewal_info.btn_continue_clone_option()

        except Exception as e:
            print("Error : {}".format(e))