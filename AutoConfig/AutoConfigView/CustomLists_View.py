from AutoConfig.AutoConfigPageObjects.CustomLists import CustomListsObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Common import ClassicAdminCommonPageObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Home import ClassicAdminHomePageObjects
import time

class CustomListsView:

    def __init__(self, drv):
        # Create instance of the Fees Page Objects
        self.obj_driver = drv
        self.obj_custom_list = CustomListsObjects(drv)
        self.obj_common = ClassicAdminCommonPageObjects(drv)
        self.obj_home = ClassicAdminHomePageObjects(drv)

    RETURN_VALUE = 0

    # Select Custom Lists from Menu
    def navigate_to_custom_lists(self):
        try:
            self.obj_home.select_menu("Application")
            self.obj_home.select_menu_option("Custom List")
        except Exception as e:
            print("Error : {}".format(e))

    # Search for Custom List
    # If during Search record is found click that and if no record is found click cancel and return to next iteration
    def search_custom_lists(self, i, action, custom_list_group_code, custom_list_subgroup):
        try:
            self.obj_custom_list.enter_custom_lists_group_code(custom_list_group_code)
            self.obj_custom_list.enter_custom_lists_subgroup(custom_list_subgroup)
            self.obj_common.click_submit()
            record_found = self.obj_custom_list.verify_custom_list_in_list_exists(custom_list_group_code)

            if record_found == 1:
                self.obj_custom_list.select_custom_list_from_list(custom_list_subgroup)
                self.RETURN_VALUE = 1

            else:
                no_rec = self.obj_common.no_record_found()
                if no_rec == 1:
                    print(str(i) + ", " + action + ", FAIL, " + custom_list_group_code + " unable to find")
                    self.obj_common.click_search_new()
                    self.RETURN_VALUE = 0

        except Exception as e:
            print("Error : {}".format(e))

        # Select the subgroup. if exists select and if not report it and continue with next iteration.

    # Select Custom List Subgroup
    def select_subgroup(self, i, action, subgroup):
        try:
            subgroup_found = self.obj_custom_list.verify_custom_list_sub_group_exists(subgroup)
            if subgroup_found == 1:
                self.obj_custom_list.select_custom_list_sub_gorup_from_list(subgroup)
                self.RETURN_VALUE = 1
            else:
                print(str(i) + ", " + action + ", FAIL, " + subgroup + " unable to find subgroup")
                self.navigate_to_custom_lists()  # No other button available to go to home page
                self.RETURN_VALUE = 0

        except Exception as e:
            print("Error : {}".format(e))

    # Add new Custom List
    def create_new_custom_lists(self, i, group_code, subgroup, group_display_order, column_name, type, display_order, default_value, required_flag,
                                req_for_fee_calc, supervisor_edit_only, searchable_flag, display_len, aca_displayable, aca_searchable, status):
        try:
            self.obj_custom_list.click_add()
            self.obj_custom_list.enter_custom_lists_group_code(group_code)
            self.obj_custom_list.enter_custom_lists_subgroup(subgroup)
            self.obj_custom_list.enter_group_display_order(group_display_order)
            self.obj_custom_list.enter_column_name(column_name)
            self.obj_custom_list.select_type(type)
            self.obj_custom_list.enter_display_order(display_order)
            self.obj_custom_list.enter_default_value(default_value)
            self.obj_custom_list.select_required_flag(required_flag)
            if required_flag == "Yes":
                self.obj_custom_list.select_req_for_fee_calc(req_for_fee_calc)
            self.obj_custom_list.select_supervisor_edit_only(supervisor_edit_only)
            self.obj_custom_list.select_searchable_flag(searchable_flag)
            self.obj_custom_list.enter_display_len(display_len)
            self.obj_custom_list.select_aca_displayable(aca_displayable)
            self.obj_custom_list.select_aca_searchable(aca_searchable)
            self.obj_custom_list.select_status(status)
            self.obj_common.click_submit_data()

            success = self.obj_custom_list.verify_new_record_added()
            if success == 1:
                print(str(i) + ", CREATE, PASS, " + group_code + " added successfully.")
                self.RETURN_VALUE = 1
            else:
                alert = self.obj_common.does_alert_exists()
                if alert == 1:
                    error = self.obj_common.read_alert_text()
                    print(str(i) + ", CREATE, FAIL, " + group_code + ", Error:" + error)
                    self.obj_common.handle_alert()
                else:
                    print(str(i) + ", CREATE, FAIL, " + group_code + ", Some Error")
                self.RETURN_VALUE = 0
            self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Update Custom List
    def update_custom_lists(self, i, group_code, subgroup, column_name, type, display_order, default_value, required_flag, req_for_fee_calc,
                            supervisor_edit_only, searchable, display_len, aca_displayable, aca_searchable, status):
        try:
            self.search_custom_lists(i, "UPDATE", group_code, subgroup)
            if self.RETURN_VALUE == 1:
                self.select_subgroup(i, "UPDATE", subgroup)
                if self.RETURN_VALUE == 1:
                    exists = self.obj_custom_list.verify_column_name_exists(column_name)
                    if exists == 1:
                        self.obj_custom_list.update_select_value(column_name, type, 2)
                        self.obj_custom_list.update_enter_value(column_name, display_order, 3)
                        self.obj_custom_list.update_enter_value(column_name, default_value, 4, 2)
                        self.obj_custom_list.update_select_value(column_name, required_flag, 5)
                        if required_flag == "Yes":
                            self.obj_custom_list.update_select_value(column_name, req_for_fee_calc, 6)
                        self.obj_custom_list.update_select_value(column_name, supervisor_edit_only, 7)
                        self.obj_custom_list.update_select_value(column_name, searchable, 8)
                        self.obj_custom_list.update_enter_value(column_name, display_len, 9)
                        self.obj_custom_list.update_select_value(column_name, aca_displayable, 10)
                        self.obj_custom_list.update_select_value(column_name, aca_searchable, 11)
                        self.obj_custom_list.update_select_value(column_name, status, 12)
                        self.obj_custom_list.click_update()

                        alert = self.obj_common.does_alert_exists()
                        if alert == 1:
                            error = self.obj_common.read_alert_text()
                            print(str(i) + ", UPDATE , FAIL, " + group_code + ", Column Name: ," + column_name + " Error:" + error)
                            self.obj_common.handle_alert()
                        else:
                            print(str(i) + ", UPDATE, PASS, " + group_code + ", Column Name: ," + column_name + " updated successfully")
                    else:
                        print(str(i) + ", UPDATE, FAIL, " + group_code + ", Column Name: ," + column_name + " doesn't exists in the list")

                    self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Add new type under custom field
    def add_new_type(self, i, group_code, subgroup, column_name, type, display_order, default_value, required_flag, req_for_fee_calc,
                     supervisor_edit_only, searchable_flag, display_len, aca_displayable, aca_searchable, display_field_existing_record,
                     display_field_existing_contact, display_field_existing_meeting, display_field_existing_education, status):
        try:
            self.search_custom_lists(i, "ADD FIELD", group_code, subgroup)
            if self.RETURN_VALUE == 1:
                self.select_subgroup(i, "ADD FIELD", subgroup)
                if self.RETURN_VALUE == 1:
                    self.obj_custom_list.click_add_new_field()
                    self.obj_custom_list.switch_to_add_field_window()
                    self.obj_custom_list.enter_column_name(column_name)
                    self.obj_custom_list.select_type(type)
                    self.obj_custom_list.enter_display_order(display_order)
                    self.obj_custom_list.enter_default_value(default_value)
                    self.obj_custom_list.select_required_flag(required_flag)
                    if required_flag == "Yes":
                        self.obj_custom_list.select_req_for_fee_calc_add_field(req_for_fee_calc)
                    self.obj_custom_list.select_supervisor_edit_only(supervisor_edit_only)
                    self.obj_custom_list.select_searchable_flag(searchable_flag)
                    self.obj_custom_list.enter_display_len(display_len)
                    self.obj_custom_list.select_aca_displayable(aca_displayable)
                    self.obj_custom_list.select_aca_searchable(aca_searchable)
                    self.obj_custom_list.select_display_field_on_existing_record(display_field_existing_record)
                    self.obj_custom_list.select_display_field_on_existing_contact(display_field_existing_contact)
                    self.obj_custom_list.select_display_field_on_existing_meeting(display_field_existing_meeting)
                    self.obj_custom_list.select_display_field_on_existing_education(display_field_existing_education)
                    self.obj_custom_list.select_status_add_field(status)
                    self.obj_common.click_submit()

                    alert = self.obj_common.does_alert_exists()
                    if alert == 1:
                        error = self.obj_common.read_alert_text()
                        print(str(i) + ", ADD FIELD, FAIL, " + group_code + " Field: ," + column_name + " Error:" + error)
                        self.obj_common.handle_alert()
                        self.obj_common.click_cancel()
                        self.RETURN_VALUE = 0
                    else:
                        column_added = self.obj_custom_list.verify_column_name_exists(column_name)
                        if column_added == 1:
                            print(str(i) + ", ADD FIELD, PASS, " + group_code + " Field: ," + column_name + ", added successfully")
                            self.RETURN_VALUE = 1
                        else:
                            print(str(i) + ", ADD FIELD, PASS, " + group_code + " Field: ," + column_name + ", not added successfully")

                    self.obj_common.switch_to_original_window()
                    self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Delete custom field
    def delete_custom_lists_type(self, i, group_code, subgroup, column_name, delete_contact, delete_cap_data, delete_checklist, delete_education, delete_meeting):
        try:
            self.search_custom_lists(i, "DELETE FIELD", group_code, subgroup)
            if self.RETURN_VALUE == 1:
                self.select_subgroup(i, "DELETE FIELD", subgroup)
                if self.RETURN_VALUE == 1:
                    exists = self.obj_custom_list.verify_column_name_exists(column_name)
                    if exists == 1:
                        self.obj_custom_list.select_column_name_to_delete(column_name)

                        self.obj_custom_list.switch_to_delete_subgroup_window()
                        self.obj_custom_list.select_delete_contact(delete_contact)
                        self.obj_custom_list.select_delete_cap_data(delete_cap_data)
                        self.obj_custom_list.select_delete_checklist(delete_checklist)
                        self.obj_custom_list.select_delete_education(delete_education)
                        self.obj_custom_list.select_delete_meeting(delete_meeting)
                        self.obj_common.click_submit()

                        print(str(i) + ", DELETE FIELD, PASS, " + group_code + " Field: ," + column_name + ", deleted successfully")
                    else:
                        print(str(i) + ", DELETE FIELD, FAIL, " + group_code + " Field: ," + column_name + ", not exists.")
                    self.obj_common.switch_to_original_window()
                    self.obj_common.click_cancel()
        except Exception as e:
            print("Error : {}".format(e))

    # Delete custom List sub group
    def delete_custom_list_group(self, i, group_code, subgroup, delete_contact, delete_cap_data, delete_checklist, delete_education, delete_meeting):
        try:
            self.search_custom_lists(i, "DELETE FIELD", group_code, subgroup)
            if self.RETURN_VALUE == 1:
                self.obj_custom_list.delete_custom_list_sub_gorup_from_list(subgroup)
                self.obj_custom_list.switch_to_delete_field_window()
                self.obj_custom_list.select_delete_contact(delete_contact)
                self.obj_custom_list.select_delete_cap_data(delete_cap_data)
                self.obj_custom_list.select_delete_checklist(delete_checklist)
                self.obj_custom_list.select_delete_education(delete_education)
                self.obj_custom_list.select_delete_meeting(delete_meeting)
                self.obj_common.click_submit()

                print(str(i) + ", DELETE FIELD, PASS, " + group_code + " Field: ," + subgroup + ", deleted successfully")
            else:
                print(str(i) + ", DELETE FIELD, FAIL, " + group_code + " Field: ," + subgroup + ", not exists.")

            self.obj_common.switch_to_original_window()
            self.navigate_to_custom_lists()

        except Exception as e:
            print("Error : {}".format(e))