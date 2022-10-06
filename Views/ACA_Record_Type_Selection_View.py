from PageObjects.ACA_Record_Type_Selection import ACARecordTypeSelectionObject
from Views.ACA_Common_View import ACACommonView


class ACARecordTypeSelectionView:

    def __init__(self, drv):
        # Create instance of the ACA Login Page Objects
        self.obj_driver = drv
        self.obj_aca_record_select = ACARecordTypeSelectionObject(drv)
        self.obj_common = ACACommonView(drv)

    def aca_select_record_type(self, sub_type, record_type):
        try:
            self.obj_aca_record_select.enter_record_type(record_type)
            self.obj_aca_record_select.click_search_record_type()
            record_type_exists = self.obj_aca_record_select.verify_record_type_exists(sub_type,record_type)
            if record_type_exists == 1:
                self.obj_aca_record_select.select_record_type(sub_type, record_type)
                self.obj_common.aca_continue_application()
            else:
                print("Record type " + record_type + " doesn't exists")

        except Exception as e:
            print("Error : {}".format(e))
