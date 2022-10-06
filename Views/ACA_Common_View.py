from PageObjects.ACA_Record_Type_Selection import ACARecordTypeSelectionObject
from PageObjects.ACA_Common import ACACommonObject
import time


class ACACommonView:

    def __init__(self, drv):
        # Create instance of the ACA Login Page Objects
        self.obj_driver = drv
        self.obj_common = ACACommonObject(drv)
        self.obj_aca_record_select = ACARecordTypeSelectionObject(drv)

    def aca_continue_application(self):
        self.obj_common.click_continue_application()

    def aca_wait_for_spinner(self):
        self.obj_common.aca_wait_for_spinner()

    def aca_license_disclaimer(self):
        self.obj_common.check_disclaimer()

    def aca_select_license(self, license):
        self.obj_common.select_license(license)

    def verify_aca_error(self, error_message):
        self.obj_common.verify_error_message(error_message)

    def select_module(self, menu, sub_menu):
        self.obj_common.select_menu(menu)
        self.obj_common.select_sub_menu(sub_menu)
