from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ACARecordDetailObject:

    # Page Objects for Record Details
    lbl_permit_num = (By.ID, "ctl00_PlaceHolderMain_lblPermitNumber")
    lbl_expiration_date = (By.ID, "ctl00_PlaceHolderMain_lblExpirtionDate")
    lbl_application_status = (By.ID, "ctl00_PlaceHolderMain_lblRecordStatus")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def verify_premit_number(self, record_id):
        permit_num_exists = self.obj_wrapper.object_exists(self.lbl_permit_num, "Permit Number")
        if permit_num_exists == 1:
            permit_num = self.obj_wrapper.get_text_for_webelement(self.lbl_permit_num, "Permit Number")
            if permit_num == record_id:
                print("Record Number verified successfully to " + record_id)
            else:
                print("Record Number verified not successfully to " + record_id)

    def verify_status(self, status):
        status_exists = self.obj_wrapper.object_exists(self.lbl_application_status, "Application Status")
        if status_exists == 1:
            status_value = self.obj_wrapper.get_text_for_webelement(self.lbl_application_status, "Application Status")
            if status == status_value:
                print("Status successfully verified to " + status)
            else:
                print("Status not successfully verified to " + status + ". It is "+status_value)

    def verify_expiration_date(self, expiration_date):
        expiration_date_exists = self.obj_wrapper.object_exists(self.lbl_expiration_date, "Expiration Date")
        if expiration_date_exists == 1:
            expiration_date_value = self.obj_wrapper.get_text_for_webelement(self.lbl_expiration_date, "Expiration Date")
            if expiration_date == expiration_date_value:
                print("Expiration date successfully verified to " + expiration_date)
            else:
                print("Expiration date not verified to " + expiration_date + ". It is "+expiration_date_value)