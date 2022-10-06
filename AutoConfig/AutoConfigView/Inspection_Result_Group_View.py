from AutoConfig.AutoConfigPageObjects.Inspection_Result_Group import InspectionResultGroupObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Common import ClassicAdminCommonPageObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Home import ClassicAdminHomePageObjects
import math
import time


class InspectionResultGroupView:

    def __init__(self, drv):
        # Create instance of the Inspection Result Group Page Objects
        self.obj_driver = drv
        self.obj_ins = InspectionResultGroupObjects(drv)
        self.obj_common = ClassicAdminCommonPageObjects(drv)
        self.obj_home = ClassicAdminHomePageObjects(drv)

    RETURN_VALUE = 0

    # Select Inspection Result Group from Menu
    def navigate_to_inspection_result_group(self):
        try:
            self.obj_home.select_menu("Inspection")
            self.obj_home.select_menu_option("Inspection Result Group")
        except Exception as e:
            print("Error : {}".format(e))

    # Create new group
    def create_new_result_group(self, i, result_group, result, display_order, result_type, miminum_score, maximum_score,
                                minimum_major_violation, maximum_major_violation):
        try:
            self.obj_ins.click_add()
            self.obj_ins.enter_group_code(result_group)
            self.obj_common.click_submit()
            alert = self.obj_common.does_alert_exists()
            if alert == 1:
                error = self.obj_common.read_alert_text()
                print(str(i) + ", CREATE, FAIL, " + result_group + ", Error:" + error)
                self.obj_common.handle_alert()
            else:
                self.obj_ins.click_add_type()
                self.obj_ins.enter_new_result(result)
                self.obj_common.click_submit()
                alert = self.obj_common.does_alert_exists()
                if alert == 1:
                    error = self.obj_common.read_alert_text()
                    print(str(i) + ",CREATE, FAIL, " + result_group + ", Error:" + error)
                    self.obj_common.handle_alert()
                else:
                    self.result_detail_update(result, display_order, result_type, miminum_score, maximum_score,
                                              minimum_major_violation, maximum_major_violation)
                    self.obj_ins.click_update_type()
                    alert = self.obj_common.does_alert_exists()
                    if alert == 1:
                        error = self.obj_common.read_alert_text()
                        print(str(i) + ",CREATE, FAIL, " + result_group + ", Error:" + error)
                        self.obj_common.handle_alert()
                    else:
                        print(str(i) + ", CREATE, PASS, " + result_group + ", with - " + result + " result created successfully")
            self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Update Result Group
    def update_result_group(self,i, result_group, result, result_update, display_order, result_type, miminum_score, maximum_score,
                                minimum_major_violation, maximum_major_violation):
        try:
            self.select_existing_result_group(i, "UPDATE", result_group)
            if self.RETURN_VALUE == 1:
                exists = self.obj_ins.verify_result_exists(result)
                if exists == 1:
                    self.result_detail_update(result, display_order, result_type, miminum_score, maximum_score,
                                minimum_major_violation, maximum_major_violation)
                    self.obj_ins.enter_value(result, result_update, 1)
                    self.obj_ins.click_update_type()
                    alert = self.obj_common.does_alert_exists()
                    if alert == 1:
                        error = self.obj_common.read_alert_text()
                        print(str(i) + ", UPDATE, FAIL, " + result_group + ",- "+ result + ", Error:" + error)
                        self.obj_common.handle_alert()
                    else:
                        print(str(i) + ", UPDATE, PASS, " + result_group + ",- "+ result + " result updated successfully ")
                    self.obj_common.click_cancel()
        except Exception as e:
            print("Error : {}".format(e))

    # Verify the result group exists and select if exists
    def select_existing_result_group(self,i, action, result_group):
        try:
            exists = self.obj_ins.verify_group_name_exists(result_group)
            if exists == 1:
                self.obj_ins.select_group_name_edit(result_group)
                self.RETURN_VALUE = 1
            else:
                print(str(i) + ", " + action + ", FAIL, " + result_group + ", Result Group doesn't exists")
                self.RETURN_VALUE = 0
        except Exception as e:
            print("Error : {}".format(e))

    # Add new result into existing result group
    def add_new_result(self, i, result_group, result, display_order, result_type, miminum_score, maximum_score,
                                minimum_major_violation, maximum_major_violation):
        try:
            self.select_existing_result_group(i, "ADD TYPE", result_group)
            if self.RETURN_VALUE == 1:
                self.obj_ins.click_add_type()
                self.obj_ins.enter_new_result(result)
                self.obj_common.click_submit()
                alert = self.obj_common.does_alert_exists()
                if alert == 1:
                    error = self.obj_common.read_alert_text()
                    print(str(i) + ", ADD TYPE, FAIL, " + result_group + ", Error:" + error)
                    self.obj_common.handle_alert()
                    self.obj_common.click_cancel()
                else:
                    self.result_detail_update(result, display_order, result_type, miminum_score, maximum_score,
                                    minimum_major_violation, maximum_major_violation)
                    self.obj_ins.click_update_type()
                    print(str(i) + ", ADD TYPE, PASS, " + result_group + ", "+ result+" result added successfully")
                self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    def delete_result(self, i, result_group, result):
        try:
            self.select_existing_result_group(i, "DELETE TYPE", result_group)
            if self.RETURN_VALUE == 1:
                exists = self.obj_ins.verify_result_exists(result)
                if exists == 1:
                    self.obj_ins.delete_result(result)
                    self.obj_common.handle_alert()
                    print(str(i) + ", DELETE TYPE, PASS, " + result_group + " - " + result + ", :Result Type deleted successfully")
                else:
                    print(str(i) + ", DELETE TYPE, FAIL, " + result_group + " - " + result + ", :Result Type doesn't exists")
                self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    def result_detail_update(self, result, display_order, result_type, minimun_score, maximum_score, minimum_major_violation,
                             maximum_major_violation):
        try:
            self.obj_ins.enter_value(result, int(display_order), 1)
            self.obj_ins.select_value(result, result_type, 2)
            self.obj_ins.enter_value(result, int(minimun_score), 3)
            self.obj_ins.enter_value(result, int(maximum_score), 4)
            self.obj_ins.enter_value(result, int(minimum_major_violation), 5)
            self.obj_ins.enter_value(result, int(maximum_major_violation), 6)


        except Exception as e:
            print("Error : {}".format(e))