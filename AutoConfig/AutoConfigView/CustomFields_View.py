from AutoConfig.AutoConfigPageObjects.CustomFields import CustomFieldsObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Common import ClassicAdminCommonPageObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Home import ClassicAdminHomePageObjects
import time


class CustomFieldsView:

    def __init__(self, drv):
        # Create instance of the Fees Page Objects
        self.obj_driver = drv
        self.obj_custom_field = CustomFieldsObjects(drv)
        self.obj_common = ClassicAdminCommonPageObjects(drv)
        self.obj_home = ClassicAdminHomePageObjects(drv)

    RETURN_VALUE = 0

    # Select Custom Fields from Menu
    def navigate_to_custom_field(self):
        try:
            self.obj_home.select_menu("Application")
            self.obj_home.select_menu_option("Custom Field")
        except Exception as e:
            print("Error : {}".format(e))

    # Search for existing custom fields
    def search_custom_fields(self, i, action, group_code, subgroup):
        try:
            self.obj_custom_field.enter_custom_fields_group_code(group_code)
            self.obj_custom_field.enter_custom_fields_subgroup(subgroup)
            self.obj_common.click_submit()
            record_found = self.obj_custom_field.verify_custom_field_in_list_exists(group_code)

            if record_found == 1:
                self.obj_custom_field.select_custom_field_from_list(group_code)
                self.RETURN_VALUE = 1
            else:
                no_rec = self.obj_common.no_record_found()
                if no_rec == 1:
                    print(str(i) + ", " + action + ", FAIL, " + group_code + " unable to find")
                    self.obj_common.click_search_new()
                    self.RETURN_VALUE = 0

        except Exception as e:
            print("Error : {}".format(e))

    # Select the subgroup. if exists select and if not report it and continue with next iteration.
    def select_subgroup(self, i, action, subgroup):
        try:
            subgroup_found = self.obj_custom_field.verify_custom_field_sub_group_exists(subgroup)
            if subgroup_found == 1:
                self.obj_custom_field.select_custom_field_sub_gorup_from_list(subgroup)
                self.RETURN_VALUE = 1
            else:
                print(str(i) + ", " + action + ", FAIL, " + subgroup + " unable to find subgroup")
                self.navigate_to_custom_field() # No other button available to go to home page
                self.RETURN_VALUE = 0

        except Exception as e:
            print("Error : {}".format(e))

    # Add new Custom Field
    def create_new_custom_field(self, i, group_code, subgroup, custom_list_group, group_display_order, first_field_label, field_label_alias,
                                field_type, display_order, default_value, unit, new_unit, fee_indicator, required_flag, req_for_fee_calc,
                                supervisor_edit_only, searchable_flag, max_len, display_len, aca_displayable, aca_searchable, justification,
                                default_apo_gis_layer, location_query, status):
        try:
            self.obj_custom_field.click_add()
            self.obj_custom_field.enter_custom_fields_group_code(group_code)
            self.obj_custom_field.enter_custom_fields_subgroup(subgroup)
            self.obj_custom_field.select_custom_lists_group(custom_list_group)
            self.obj_custom_field.enter_group_display_order(group_display_order)
            self.obj_custom_field.enter_first_field_label(first_field_label)
            self.obj_custom_field.enter_field_label_alias(field_label_alias)
            self.obj_custom_field.select_field_type(field_type)
            self.obj_custom_field.enter_display_order(display_order)
            self.obj_custom_field.enter_default_value(default_value)
            if unit != "":
                self.obj_custom_field.select_unit(unit)
            else:
                self.obj_custom_field.enter_new_unit(new_unit)
            self.obj_custom_field.enter_fee_indicator(fee_indicator)
            self.obj_custom_field.select_required_flag(required_flag, req_for_fee_calc)
            self.obj_custom_field.select_supervisor_edit_only(supervisor_edit_only)
            self.obj_custom_field.select_searchable_flag(searchable_flag)
            self.obj_custom_field.enter_max_len(max_len)
            self.obj_custom_field.enter_display_len(display_len)
            self.obj_custom_field.select_aca_displayable(aca_displayable)
            self.obj_custom_field.select_aca_searchable(aca_searchable)
            self.obj_custom_field.select_justification(justification)
            self.obj_custom_field.enter_default_apo_gis_layer(default_apo_gis_layer)
            self.obj_custom_field.select_location_query(location_query)
            self.obj_custom_field.select_status(status)
            self.obj_common.click_submit_data()
            alert = self.obj_common.does_alert_exists()
            if alert == 1:
                error = self.obj_common.read_alert_text()
                print(str(i) + ", CREATE, FAIL, " + group_code + ", Error:" + error)
                self.obj_common.handle_alert()
            else:
                print(str(i) + ", CREATE, PASS, " + group_code + ", added successfully")
                self.RETURN_VALUE = 0

            self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Update the custom field
    def update_custom_field(self, i, group_code, subgroup, field_label, field_label_alias, default_apo_gis, location_query,
                            field_type, display_order, default_value, unit, fee_indicator, required_flag, req_for_fee_calc,
                            supervisor_edit_only,searchable_flag, max_len, display_len, aca_displayable, aca_searchable, justification, status):
        try:
            self.search_custom_fields(i, "UPDATE", group_code, subgroup)
            if self.RETURN_VALUE == 1:
                self.select_subgroup(i, "UPDATE", subgroup)
                if self.RETURN_VALUE == 1:
                    self.obj_custom_field.enter_default_apo_gis_layer(default_apo_gis)
                    self.obj_custom_field.select_location_query(location_query)
                    self.obj_custom_field.update_select_value(field_label, field_type, 2)
                    self.obj_custom_field.update_enter_value(field_label, display_order, 3)
                    self.obj_custom_field.update_enter_value(field_label, field_label_alias, 4)
                    self.obj_custom_field.update_enter_value(field_label, fee_indicator, 5)
                    self.obj_custom_field.update_select_value(field_label, unit, 6)
                    self.obj_custom_field.update_enter_value(field_label, default_value, 7, 2)
                    self.obj_custom_field.update_select_value(field_label, required_flag, 8)
                    if required_flag == "Yes":
                        self.obj_custom_field.update_enter_value(field_label, req_for_fee_calc, 9)
                    self.obj_custom_field.update_select_value(field_label, supervisor_edit_only, 10)
                    self.obj_custom_field.update_select_value(field_label, searchable_flag, 11)
                    self.obj_custom_field.update_enter_value(field_label, max_len, 12)
                    self.obj_custom_field.update_enter_value(field_label, display_len, 13)
                    self.obj_custom_field.update_select_value(field_label, aca_displayable, 14)
                    self.obj_custom_field.update_select_value(field_label, aca_searchable, 15)
                    self.obj_custom_field.update_select_value(field_label,justification, 16)
                    self.obj_custom_field.update_select_value(field_label,status, 17)
                    self.obj_custom_field.click_update()

                    alert = self.obj_common.does_alert_exists()
                    if alert == 1:
                        error = self.obj_common.read_alert_text()
                        print(str(i) + ", UPDATE , FAIL, " + group_code + " Field: ," + field_label + " Error:" + error)
                        self.obj_common.handle_alert()
                        self.RETURN_VALUE = 0
                    else:
                        print(str(i) + ", UPDATE, PASS, " + group_code + " Field: ," + field_label + " updated successfully")
                        self.RETURN_VALUE = 1

                    self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Add a new field in existing custom field group.
    # Select the group and subgroup. and then add the field.
    def add_new_field(self, i, group_code, subgroup, apply_change_to, first_field_label, field_label_alias,
                      field_type, display_order, default_value, unit, new_unit, fee_indicator, required_flag, req_for_fee_calc,
                      supervisor_edit_only,searchable_flag, max_len, display_len, aca_displayable, aca_searchable, justification, status,
                      display_field_existing_record, display_field_existing_contact, display_field_existing_meeting, display_field_existing_education,
                      alternate_aca_label):
        try:
            self.search_custom_fields(i, "ADD FIELD", group_code, subgroup)
            if self.RETURN_VALUE == 1:
                self.select_subgroup(i, "ADD FIELD", subgroup)
                if self.RETURN_VALUE == 1:
                    self.obj_custom_field.click_add_new_field()
                    self.obj_custom_field.switch_to_add_field_window()
                    self.obj_custom_field.select_apply_changes_to(apply_change_to)
                    self.obj_custom_field.enter_first_field_label(first_field_label)
                    self.obj_custom_field.enter_field_label_alias(field_label_alias)
                    self.obj_custom_field.select_field_type(field_type)
                    self.obj_custom_field.enter_display_order(display_order)
                    self.obj_custom_field.enter_default_value(default_value)
                    if unit != "":
                        self.obj_custom_field.select_unit(unit)
                    else:
                        self.obj_custom_field.enter_new_unit(new_unit)
                    self.obj_custom_field.enter_fee_indicator(fee_indicator)
                    self.obj_custom_field.select_required_flag(required_flag, req_for_fee_calc)
                    self.obj_custom_field.select_supervisor_edit_only(supervisor_edit_only)
                    self.obj_custom_field.select_searchable_flag(searchable_flag)
                    self.obj_custom_field.enter_max_len(max_len)
                    self.obj_custom_field.enter_display_len(display_len)
                    self.obj_custom_field.select_justification(justification)
                    self.obj_custom_field.select_aca_displayable(aca_displayable)
                    self.obj_custom_field.select_aca_searchable(aca_searchable)
                    self.obj_custom_field.select_display_field_on_existing_record(display_field_existing_record)
                    self.obj_custom_field.select_display_field_on_existing_contact(display_field_existing_contact)
                    self.obj_custom_field.select_display_field_on_existing_meeting(display_field_existing_meeting)
                    self.obj_custom_field.select_display_field_on_existing_education(display_field_existing_education)
                    self.obj_custom_field.select_status(status)
                    self.obj_custom_field.enter_alternative_aca_label(alternate_aca_label)
                    self.obj_common.click_submit()

                    alert = self.obj_common.does_alert_exists()
                    if alert == 1:
                        error = self.obj_common.read_alert_text()
                        print(str(i) + ", ADD FIELD, FAIL, " + group_code + " Field: ," + field_label_alias + " Error:" + error)
                        self.obj_common.handle_alert()
                        self.obj_common.click_cancel()
                    else:
                        print(str(i) + ", ADD FIELD, PASS, " + group_code + " Field: ," + field_label_alias + ", Added successfully")

                    self.obj_common.switch_to_original_window()
                    self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Delete field
    def delete_field(self, i, group_code, subgroup, field_name, delete_contact, delete_cap_data, delete_checklist, delete_education, delete_meeting):
        try:
            self.search_custom_fields(i, "DELETE FIELD", group_code, subgroup)
            if self.RETURN_VALUE == 1:
                self.select_subgroup(i, "DELETE FIELD", subgroup)
                if self.RETURN_VALUE == 1:
                    exists = self.obj_custom_field.verify_field_exists(field_name)
                    if exists == 1:
                        self.obj_custom_field.select_field_to_delete(field_name)
                        self.obj_custom_field.switch_to_delete_field_window()
                        self.obj_custom_field.select_delete_contact(delete_contact)
                        self.obj_custom_field.select_delete_cap_data(delete_cap_data)
                        self.obj_custom_field.select_delete_checklist(delete_checklist)
                        self.obj_custom_field.select_delete_education(delete_education)
                        self.obj_custom_field.select_delete_meeting(delete_meeting)
                        self.obj_common.click_submit()
                        self.obj_common.switch_to_original_window()

                        print(str(i) + ", DELETE FIELD, PASS, " + group_code + " Field: ," + field_name + ", Deleted successfully")
                    else:
                        print(str(i) + ", DELETE FIELD, FAIL, " + group_code + " Field: ," + field_name + ", not exists.")
                    self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Delete Subgroup
    def delete_subgroup(self, i, group_code, subgroup,delete_contact, delete_cap_data, delete_checklist, delete_education, delete_meeting ):
        try:
            self.search_custom_fields(i, "DELETE SUB GROUP", group_code, subgroup)
            if self.RETURN_VALUE == 1:
                exists = self.obj_custom_field.verify_custom_field_sub_group_exists(subgroup)
                if exists == 1:
                    self.obj_custom_field.select_custom_field_sub_group_to_delete(subgroup)
                    self.obj_custom_field.switch_to_delete_field_window()
                    self.obj_custom_field.select_delete_contact(delete_contact)
                    self.obj_custom_field.select_delete_cap_data(delete_cap_data)
                    self.obj_custom_field.select_delete_checklist(delete_checklist)
                    self.obj_custom_field.select_delete_education(delete_education)
                    self.obj_custom_field.select_delete_meeting(delete_meeting)
                    self.obj_common.click_submit()
                    self.obj_common.switch_to_original_window()

                    print(str(i) + ", DELETE SUB GROUP, PASS, " + group_code + " Sub Group: ," + subgroup + ", Deleted successfully")
                else:
                    print(str(i) + ", DELETE SUB GROUP, FAIL, " + group_code + " Sub Group: ," + subgroup + ", not exists.")
                self.navigate_to_custom_field()

        except Exception as e:
            print("Error : {}".format(e))