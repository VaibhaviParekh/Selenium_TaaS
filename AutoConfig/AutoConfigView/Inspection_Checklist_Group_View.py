from AutoConfig.AutoConfigPageObjects.Inspection_Checklist_Group import InspectionChecklistObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Common import ClassicAdminCommonPageObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Home import ClassicAdminHomePageObjects
import math
import time


class InspectionResultGroupView:

    def __init__(self, drv):
        # Create instance of the Inspection Checklist Group Page Objects
        self.obj_driver = drv
        self.obj_ins = InspectionChecklistObjects(drv)
        self.obj_common = ClassicAdminCommonPageObjects(drv)
        self.obj_home = ClassicAdminHomePageObjects(drv)

    RETURN_VALUE = 0

    # Select Inspection Checklist Group from Menu
    def navigate_to_inspection_checklist_group(self):
        try:
            self.obj_home.select_menu("Inspection")
            self.obj_home.select_menu_option("Inspection Checklist Group")
        except Exception as e:
            print("Error : {}".format(e))

    # Checklist reference detail

    # Create new Inspection Checklist Group
    def create_inspection_checklist_group(self,i, checklist_group, reference_checklist, display_order, auto_create, ad_hoc):
        try:
            self.obj_ins.click_add()
            self.obj_ins.enter_group_name(checklist_group)
            self.obj_common.click_submit()
            alert = self.obj_common.does_alert_exists()
            if alert == 1:
                error = self.obj_common.read_alert_text()
                print(str(i) + ", CREATE, FAIL, " + checklist_group + ", Error:" + error)
                self.obj_common.handle_alert()
                self.obj_common.click_cancel()
            else:

                self.obj_common.click_submit()
                print(str(i) + ", ADD TYPE, PASS, " + checklist_group + ", " + reference_checklist + " Inspection Checklist Group created successfully")
            self.obj_common.click_cancel()



        except Exception as e:
            print("Error : {}".format(e))