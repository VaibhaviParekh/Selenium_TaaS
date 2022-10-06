
from PageObjects.ACA_Record_Search import ACARecordSearchObject
from PageObjects.ACA_Record_Details import ACARecordDetailObject
from Views.ACA_Common_View import ACACommonView

class ACARecordSearchView:

    def __init__(self, drv):
        # Create instance of the ACA Record Search Objects
        self.obj_driver = drv
        self.obj_record_search = ACARecordSearchObject(drv)
        self.obj_record_details = ACARecordDetailObject(drv)
        self.obj_common = ACACommonView(drv)

    # Regular login flow.
    def aca_record_search(self, record_type, record_number):
        try:
            self.obj_record_search.select_record_type(record_type)
            self.obj_record_search.enter_record_id(record_number)
            self.obj_record_search.click_record_search()
            self.obj_common.aca_wait_for_spinner()
            self.obj_record_details.verify_premit_number(record_number)

        except Exception as e:
            print("Error : {}".format(e))