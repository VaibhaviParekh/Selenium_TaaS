from AutoConfig.AutoConfigPageObjects.Inspection import InspectionObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Common import ClassicAdminCommonPageObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Home import ClassicAdminHomePageObjects
import math


class InspectionView:

    def __init__(self, drv):
        # Create instance of the Inspection Page Objects
        self.obj_driver = drv
        self.obj_ins = InspectionObjects(drv)
        self.obj_common = ClassicAdminCommonPageObjects(drv)
        self.obj_home = ClassicAdminHomePageObjects(drv)

    RETURN_VALUE = 0

    # Select Inspection from Menu
    def navigate_to_inspection(self):
        try:
            self.obj_home.select_menu("Inspection")
            self.obj_home.select_menu_option("Inspection")
        except Exception as e:
            print("Error : {}".format(e))

    # Search for Inspection
    def search_inspection_group(self, i, action, inspection_group_code, inspection_group_name):
        try:
            self.obj_ins.enter_inspection_group_code(inspection_group_code)
            self.obj_ins.enter_inspection_group_name(inspection_group_name)
            self.obj_common.click_submit()

            record_found = self.obj_ins.verify_inspection_group_exists(inspection_group_code)
            if record_found == 1:
                self.obj_ins.select_inspection_group_from_list(inspection_group_code)
                self.RETURN_VALUE = 1
            else:
                no_rec = self.obj_common.no_record_found()
                if no_rec == 1:
                    print(str(i) + ", " + action + ", FAIL, " + inspection_group_code + " unable to find")
                    self.obj_common.click_search_new()
                    self.RETURN_VALUE = 0

        except Exception as e:
            print("Error : {}".format(e))

    # Add New Inspection Group
    def create_inspection_group(self,i, inspection_group_code, inspection_group_name, configured_by, inspection_type, checklist_group,
                            result_group, grade_group, inspection_score, total_score, required_optional, aca_inspection_display,
                            aca_multi_inspection_schedule, auto_assign, unit, max_points, flow_enabled, ivr_number, display_order,
                            allow_failed_checklist_item, capture_and_carry_over_failed_checklist, department,
                            reschedule_restriction, cancel_restriction, edit_inspection, reschedule_hours_prior_value,
                            reschedule_days_prior_value, reschedule_days_prior_time, reschedule_days_prior_ampm, cancel_hours_prior_value,
                            cancel_days_prior_value, cancel_days_prior_time, cancel_days_prior_ampm):
        try:
            self.obj_ins.click_add()
            self.obj_ins.enter_inspection_group_code(inspection_group_code)
            self.obj_ins.enter_inspection_group_name(inspection_group_name)
            self.obj_common.click_submit()

            alert = self.obj_common.does_alert_exists()
            if alert == 1:
                error = self.obj_common.read_alert_text()
                print(str(i) + ", CREATE, FAIL, " + inspection_group_code + ", Error:" + error)
                self.obj_common.handle_alert()
            else:
                self.obj_ins.select_configured_by(configured_by)
                self.obj_ins.enter_inspection_type(inspection_type)
                self.obj_ins.click_update_type()
                self.inspection_type_details(inspection_type, checklist_group, result_group, grade_group, inspection_score,
                                             total_score, required_optional, aca_inspection_display, aca_multi_inspection_schedule,
                                             auto_assign, unit, max_points, flow_enabled, ivr_number, display_order, allow_failed_checklist_item,
                                             capture_and_carry_over_failed_checklist, department, reschedule_restriction, cancel_restriction, edit_inspection,
                                             reschedule_hours_prior_value, reschedule_days_prior_value, reschedule_days_prior_time, reschedule_days_prior_ampm,
                                             cancel_hours_prior_value, cancel_days_prior_value, cancel_days_prior_time, cancel_days_prior_ampm )
                self.obj_ins.click_update_type()
                print(str(i) + ", CREATE, PASS, " + inspection_group_code + ", Inspection group code added successfully")
            self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Add Type Inspection
    def add_inspection_type(self, i, inspection_group_code, inspection_group_name, inspection_type, checklist_group,
                            result_group, grade_group, inspection_score, total_score, required_optional, aca_inspection_display,
                            aca_multi_inspection_schedule, auto_assign, unit, max_points, flow_enabled, ivr_number, display_order,
                            allow_failed_checklist_item, capture_and_carry_over_failed_checklist, department,
                            reschedule_restriction, cancel_restriction, edit_inspection, reschedule_hours_prior_value,
                            reschedule_days_prior_value, reschedule_days_prior_time, reschedule_days_prior_ampm, cancel_hours_prior_value,
                            cancel_days_prior_value, cancel_days_prior_time, cancel_days_prior_ampm):
        try:
            self.search_inspection_group(i, "ADD TYPE", inspection_group_code, inspection_group_name)
            if self.RETURN_VALUE == 1:
                self.obj_ins.click_add_type()
                self.obj_ins.switch_to_add_type_window()
                self.obj_ins.enter_inspection_type_add(inspection_type)
                self.obj_common.click_save()

                alert = self.obj_common.does_alert_exists()
                if alert == 1:
                    error = self.obj_common.read_alert_text()
                    print(str(i) + ", ADD TYPE, FAIL, " + inspection_group_code + ", Error:" + error)
                    self.obj_common.handle_alert()
                    self.obj_common.switch_to_original_window()
                else:
                    self.obj_common.switch_to_original_window()
                    self.inspection_type_details(inspection_type, checklist_group, result_group, grade_group, inspection_score,
                                                 total_score, required_optional, aca_inspection_display,aca_multi_inspection_schedule,
                                                 auto_assign, unit, max_points, flow_enabled, ivr_number, display_order, allow_failed_checklist_item,
                                                 capture_and_carry_over_failed_checklist, department, reschedule_restriction, cancel_restriction, edit_inspection,
                                                 reschedule_hours_prior_value, reschedule_days_prior_value, reschedule_days_prior_time, reschedule_days_prior_ampm,
                                                 cancel_hours_prior_value, cancel_days_prior_value, cancel_days_prior_time, cancel_days_prior_ampm)
                    self.obj_ins.click_update_type()
                    print(str(i) + ", ADD TYPE, PASS, " + inspection_group_code + ", Inspection Type added successfully")
                    self.RETURN_VALUE = 1
            self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Update Inspection Type
    def update_inspection_type(self, i, inspection_group_code, inspection_group_name, inspection_group_name_update, configured_by,
                               inspection_type, inspection_type_name_update, checklist_group, result_group, grade_group, inspection_score,
                               total_score, required_optional, aca_inspection_display, aca_multi_inspection_schedule, auto_assign, unit,
                               max_points, flow_enabled, ivr_number, display_order, allow_failed_checklist_item, capture_and_carry_over_failed_checklist,
                               department, reschedule_restriction, cancel_restriction, edit_inspection, reschedule_hours_prior_value, reschedule_days_prior_value,
                               reschedule_days_prior_time, reschedule_days_prior_ampm, cancel_hours_prior_value, cancel_days_prior_value, cancel_days_prior_time, cancel_days_prior_ampm):
        try:
            self.search_inspection_group(i, "UPDATE", inspection_group_code, inspection_group_name)
            if self.RETURN_VALUE == 1:
                self.obj_ins.enter_inspection_group_name(inspection_group_name_update)
                self.obj_ins.select_configured_by(configured_by)
                exists = self.obj_ins.inspection_type_exists(inspection_type)
                if exists == 1:
                    self.inspection_type_details(inspection_type, checklist_group, result_group, grade_group, inspection_score, total_score, required_optional,
                                             aca_inspection_display,aca_multi_inspection_schedule, auto_assign, unit, max_points, flow_enabled, ivr_number,
                                             display_order, allow_failed_checklist_item, capture_and_carry_over_failed_checklist, department, reschedule_restriction,
                                             cancel_restriction, edit_inspection, reschedule_hours_prior_value, reschedule_days_prior_value, reschedule_days_prior_time,
                                             reschedule_days_prior_ampm, cancel_hours_prior_value, cancel_days_prior_value, cancel_days_prior_time, cancel_days_prior_ampm)
                self.obj_ins.enter_value_inspection_type(inspection_type, inspection_type_name_update, 1)
                self.obj_ins.click_update_type()

                alert = self.obj_common.does_alert_exists()
                if alert == 1:
                    error = self.obj_common.read_alert_text()
                    print(str(i) + ", UPDATE, FAIL, " + inspection_group_code + ", Error:" + error)
                    self.obj_common.handle_alert()
                else:
                    print(str(i) + ", UPDATE, PASS, " + inspection_group_code + ", Inspection Type Updated successfully")
                    self.RETURN_VALUE = 1
                self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Inspection Type Details
    def inspection_type_details(self, inspection_type, checklist_group, result_group, grade_group, inspection_score, total_score, required_optional,
                                aca_inspection_display, aca_multi_inspection_schedule, auto_assign, unit, max_points, flow_enabled, ivr_number,
                                display_order, allow_failed_checklist_item, capture_and_carry_over_failed_checklist, department,
                                reschedule_restriction, cancel_restriction, edit_inspection, reschedule_hours_prior_value, reschedule_days_prior_value,
                                reschedule_days_prior_time, reschedule_days_prior_ampm, cancel_hours_prior_value, cancel_days_prior_value,
                                cancel_days_prior_time, cancel_days_prior_ampm ):
        try:
            self.obj_ins.select_value_inspection_type(inspection_type, checklist_group, 2)
            self.obj_ins.select_value_inspection_type(inspection_type, result_group, 4)
            self.obj_ins.select_value_inspection_type(inspection_type, grade_group, 5)
            self.obj_ins.select_value_inspection_type(inspection_type, inspection_score, 6)
            self.obj_ins.enter_value_inspection_type(inspection_type, total_score, 7)
            self.obj_ins.select_value_inspection_type(inspection_type, required_optional, 8)
            self.obj_ins.select_value_inspection_type(inspection_type, aca_inspection_display, 9)
            self.obj_ins.select_value_inspection_type(inspection_type, aca_multi_inspection_schedule, 10)
            self.obj_ins.select_value_inspection_type(inspection_type, auto_assign, 11)
            self.obj_ins.enter_value_inspection_type(inspection_type, unit, 12)
            self.obj_ins.enter_value_inspection_type(inspection_type, max_points, 13)
            self.obj_ins.select_value_inspection_type(inspection_type, flow_enabled, 14)
            self.obj_ins.enter_value_inspection_type(inspection_type, ivr_number, 15)
            self.obj_ins.enter_value_inspection_type(inspection_type, display_order, 16)

            self.obj_ins.select_value_using_label(inspection_type, "Allow Failed Checklist Items", allow_failed_checklist_item, 1)
            self.obj_ins.select_value_using_label(inspection_type, "Capture and carry over failed checklist items", capture_and_carry_over_failed_checklist, 2)
            self.department_selection(inspection_type, department)

            if reschedule_restriction == "No Restriction":
                self.obj_ins.check_radio_value(inspection_type, "Reschedule Restriction", 1, 1)
            elif reschedule_restriction == "Hours Prior":
                self.obj_ins.check_radio_value(inspection_type,"Reschedule Restriction", 2, 1)
                self.obj_ins.select_inspection_value(inspection_type, "Reschedule Restriction", int(reschedule_hours_prior_value), 1, 1)
            elif reschedule_restriction == "Days Prior":
                self.obj_ins.check_radio_value(inspection_type, "Reschedule Restriction", 3, 1)
                self.obj_ins.select_inspection_value(inspection_type, "Reschedule Restriction", int(reschedule_days_prior_value), 2, 1)
                self.obj_ins.select_inspection_value(inspection_type, "Reschedule Restriction", reschedule_days_prior_time, 3, 1)
                self.obj_ins.select_inspection_value(inspection_type, "Reschedule Restriction", reschedule_days_prior_ampm, 4, 1)

            if cancel_restriction == "No Restriction":
                self.obj_ins.check_radio_value(inspection_type, "Cancel Restriction", 1, 2)
            elif cancel_restriction == "Hours Prior":
                self.obj_ins.check_radio_value(inspection_type,"Cancel Restriction", 2, 2)
                self.obj_ins.select_inspection_value(inspection_type, "Cancel Restriction", int(cancel_hours_prior_value), 1, 2)
            elif cancel_restriction == "Days Prior":
                self.obj_ins.check_radio_value(inspection_type, "Cancel Restriction", 3, 2)
                self.obj_ins.select_inspection_value(inspection_type, "Cancel Restriction", int(cancel_days_prior_value), 2, 2)
                self.obj_ins.select_inspection_value(inspection_type, "Cancel Restriction", cancel_days_prior_time, 3, 2)
                self.obj_ins.select_inspection_value(inspection_type, "Cancel Restriction", cancel_days_prior_ampm, 4, 2)

            self.obj_ins.select_value_using_label(inspection_type, "Allow to edit inspection result/inspection grade/checklist total score/checklist major violation",
                                                  edit_inspection, 5)

        except Exception as e:
            print("Error : {}".format(e))

    # Department Selection
    def department_selection(self, inspection_type, department):
        try:
            # Department is empty then skip the selection
            try:
                if math.isnan(department):
                    department = ""
            except:
                pass

            if department != "":
                self.obj_ins.click_department_link(inspection_type)
                self.obj_ins.switch_to_department_selection_window()
                self.obj_ins.select_department(department)
                self.obj_common.click_submit()
                self.obj_common.switch_to_original_window()

        except Exception as e:
            print("Error : {}".format(e))

    # Delete Inspection Type
    def inspection_type_delete(self,i, inspection_group_code, inspection_group_name, inspection_type):
        try:
            self.search_inspection_group(i, "DELETE TYPE", inspection_group_code, inspection_group_name)
            if self.RETURN_VALUE == 1:
                exists = self.obj_ins.inspection_type_exists(inspection_type)
                if exists == 1:
                    self.obj_ins.select_inspection_type_delete(inspection_type)
                    self.obj_common.handle_alert()
                    print(str(i) + ", DELETE TYPE, PASS, " + inspection_group_code + " - " + inspection_type + ", :Inspection Type deleted successfully")
                else:
                    print(str(i) + ", DELETE TYPE, PASS, " + inspection_group_code + " - " + inspection_type + ", :Inspection Type doesn't exist")
                self.obj_common.click_cancel()
        except Exception as e:
            print("Error : {}".format(e))

