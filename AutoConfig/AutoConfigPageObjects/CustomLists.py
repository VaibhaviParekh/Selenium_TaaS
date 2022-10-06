from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class CustomListsObjects:

    # Page Objects related to Custom Lists

    btn_Add = (By.XPATH, "//img[@alt='Add New Custom Lists Group']")
    btn_Update = (By.XPATH, "//input[@alt = 'Update with changes']")
    btn_Add_New_Field = (By.XPATH, "//img[@alt = 'Add new Field']")

    txt_Custom_Lists_Group_Code = (By.ID, "id_txtR1_CHECKBOX_CODE")
    txt_Custom_Lists_Subgroup = (By.ID, "id_txtR1_CHECKBOX_TYPE")
    txt_Group_Display_Order = (By.ID, "id_txtR1_CHECKBOX_GROUP_ORDER")
    txt_Column_Name = (By.ID, "id_txtR1_CHECKBOX_DESC")
    cbo_Type = (By.ID, "txtR1_CHECKBOX_IND")
    txt_Display_Order = (By.ID, "id_txtR1_DISPLAY_ORDER")
    txt_Default_Value = (By.ID, "id_avalue")
    rdo_Required_Flag_Yes = (By.ID, "id_areqflag_y")
    rdo_Required_Flag_No = (By.ID, "id_areqflag_n")
    rdo_Required_Flag_Yes_Add_Field = (By.ID, "id_areq_fee_calc_y")
    rdo_Required_Flag_No_Add_Field = (By.ID, "id_areq_fee_calc_n")
    rdo_Req_for_Fee_Calc_Yes = (By.ID, "id_reqfeecalc_y")
    rdo_Req_for_Fee_Calc_No = (By.ID, "id_reqfeecalc_n")
    rdo_Supervisor_Edit_Only_Yes = (By.ID, "id_supervisoreditonly_y")
    rdo_Supervisor_Edit_Only_No = (By.ID, "id_supervisoreditonly_n")
    rdo_Searchable_Flag_Yes = (By.ID, "id_searchableFlag_y")
    rdo_Searchable_Flag_No = (By.ID, "id_searchableFlag_n")
    txt_Display_Len = (By.ID, "id_displayLength")
    rdo_ACA_Displayable_Yes = (By.ID, "id_vchdisplayflag_y")
    rdo_ACA_Displayable_No = (By.ID, "id_vchdisplayflag_n")
    rdo_ACA_Displayable_Hidden = (By.ID, "id_vchdisplayflag_h")
    rdo_ACA_Searchable_Yes = (By.ID, "id_searchableForACA_Y")
    rdo_ACA_Searchable_No = (By.ID, "id_searchableForACA_N")
    rdo_Status_Enable = (By.ID, "id_aenableflag_y")
    rdo_Status_Disable = (By.ID, "id_aenableflag_n")
    # On add field page enabled and disabled controls have different IDs
    rdo_Status_Enable_Field = (By.ID, "id_aenableflag_a")
    rdo_Status_Disable_Field = (By.ID, "id_aenableflag_i")


    txt_Custom_Lists_Subgroup_Alias = (By.ID, "ASISubgroupAlias")
    chk_delete_cap_data = (By.ID, "id_selectOptions_CAP")
    chk_delete_checklist = (By.ID, "id_selectOptions_GS")
    chk_delete_contact = (By.ID, "id_selectOptions_Contact")
    chk_delete_meeting = (By.ID, "id_selectOptions_Meeting")
    chk_delete_education = (By.ID, "id_selectOptions_LC")

    rdo_Apply_Changes_to_SubGroup = (By.ID, "id_applychange_one")
    rdo_Apply_Changes_to_AllGroup = (By.ID, "id_applychange_all")
    rdo_Display_Field_on_Existing_Record_Yes = (By.ID, "id_applyToOldFlag_y")
    rdo_Display_Field_on_Existing_Record_No = (By.ID, "id_applyToOldFlag_n")
    rdo_Display_Field_on_Existing_Contact_Yes = (By.ID, "id_applyToOldContactFlag_y")
    rdo_Display_Field_on_Existing_Contact_No = (By.ID, "id_applyToOldContactFlag_n")
    rdo_Display_Field_on_Existing_Meetings_Yes = (By.ID, "id_applyToOldMeetingFlag_y")
    rdo_Display_Field_on_Existing_Meetings_No = (By.ID, "id_applyToOldMeetingFlag_n")
    rdo_Display_Field_on_Existing_Education_Yes = (By.ID, "id_applyToOldLCFlag_y")
    rdo_Display_Field_on_Existing_Education_No = (By.ID, "id_applyToOldLCFlag_n")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_add(self):
        self.obj_wrapper.click_button(self.btn_Add, "Add")

    def click_update(self):
        self.obj_wrapper.click_button(self.btn_Update, "Update")

    def click_add_new_field(self):
        self.obj_wrapper.click_button(self.btn_Add_New_Field, "Add New Field")

    def verify_new_record_added(self):
        exists = self.obj_wrapper.object_exists(self.btn_Update, "Added Successfully")
        if exists == 1:
            return True
        else:
            return False

    def enter_custom_lists_group_code(self, group_code):
        self.obj_wrapper.enter_text(self.txt_Custom_Lists_Group_Code, "Group Code", group_code)

    def enter_custom_lists_subgroup(self, subgroup_alias):
        self.obj_wrapper.enter_text(self.txt_Custom_Lists_Subgroup, "Sub Group", subgroup_alias)

    def enter_subgroup_alias(self, subgroup_alias):
        self.obj_wrapper.enter_text(self.txt_Custom_Lists_Subgroup_Alias, "Sub Group Alias", subgroup_alias)

    def enter_group_display_order(self, group_display_order):
        self.obj_wrapper.enter_text(self.txt_Group_Display_Order, "Display Order", group_display_order)

    def enter_column_name(self, column_name):
        self.obj_wrapper.enter_text(self.txt_Column_Name, "Column Name", column_name)

    def select_type(self, type):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Type, "Type", type)

    def enter_display_order(self, display_order):
        self.obj_wrapper.enter_text(self.txt_Display_Order, "Display Order", display_order)

    def enter_default_value(self, default_value):
        self.obj_wrapper.enter_text(self.txt_Default_Value, "Default Value", default_value)

    def select_required_flag(self, required_flag):
        if required_flag == "Yes":
            self.obj_wrapper.click_button(self.rdo_Required_Flag_Yes, "Required Flag Yes")
        elif required_flag == "No":
            self.obj_wrapper.click_button(self.rdo_Required_Flag_No, "Required Flag No")

    def select_req_for_fee_calc(self, req_for_fee_calc):
        if req_for_fee_calc == "Yes":
            self.obj_wrapper.click_button(self.rdo_Req_for_Fee_Calc_Yes, "Req for Fee Calc Yes")
        elif req_for_fee_calc == "No":
            self.obj_wrapper.click_button(self.rdo_Req_for_Fee_Calc_No, "Req for fee Calc No")

    # Control selection on Add Type
    def select_req_for_fee_calc_add_field(self, req_for_fee_calc):
        if req_for_fee_calc == "Yes":
            self.obj_wrapper.click_button(self.rdo_Required_Flag_Yes_Add_Field, "Req for Fee Calc Yes")
        elif req_for_fee_calc == "No":
            self.obj_wrapper.click_button(self.rdo_Required_Flag_No_Add_Field, "Req for fee Calc No")

    def select_supervisor_edit_only(self, supervisor_edit_only):
        if supervisor_edit_only == "Yes":
            self.obj_wrapper.click_button(self.rdo_Supervisor_Edit_Only_Yes, "Supervisor Edit Only Yes")
        elif supervisor_edit_only == "No":
            self.obj_wrapper.click_button(self.rdo_Supervisor_Edit_Only_No, "Supervisor Edit Only No")

    def select_searchable_flag(self, searchable_flag):
        if searchable_flag == "Yes":
            self.obj_wrapper.click_button(self.rdo_Searchable_Flag_Yes, "Searchable Flag Yes")
        elif searchable_flag == "No":
            self.obj_wrapper.click_button(self.rdo_Searchable_Flag_No, "Searchable Flag No")

    def enter_display_len(self, display_len):
        self.obj_wrapper.enter_text(self.txt_Display_Len, "Display Len", display_len)

    def select_aca_displayable(self, aca_displayable):
        if aca_displayable == "Yes":
            self.obj_wrapper.click_button(self.rdo_ACA_Displayable_Yes, "ACA Displayable Yes")
        elif aca_displayable == "No":
            self.obj_wrapper.click_button(self.rdo_ACA_Displayable_No, "ACA Displayable No")
        elif aca_displayable == "Hidden":
            self.obj_wrapper.click_button(self.rdo_ACA_Displayable_Hidden, "ACA Displayable Hidden")

    def select_aca_searchable(self, aca_searchable):
        if aca_searchable == "Yes":
            self.obj_wrapper.click_button(self.rdo_ACA_Searchable_Yes, "ACA Searchable Yes")
        elif aca_searchable == "No":
            self.obj_wrapper.click_button(self.rdo_ACA_Searchable_No, "ACA Searchable No")

    def select_status(self, status):
        if status == "Enabled":
            self.obj_wrapper.click_checkbox(self.rdo_Status_Enable)
        elif status == "Disabled":
            self.obj_wrapper.click_checkbox(self.rdo_Status_Disable)

    def select_status_add_field(self, status):
        if status == "Enabled":
            self.obj_wrapper.click_checkbox(self.rdo_Status_Enable_Field)
        elif status == "Disabled":
            self.obj_wrapper.click_checkbox(self.rdo_Status_Disable_Field)

    # In the list of custom lists column verify if the field exists and delete it.
    def select_column_name_to_delete(self, field_name):
        control = (By.XPATH, "//table[@summary='Custom Lists Group']//td[contains(.,'" + field_name + "')]//..//td[15]//a")
        self.obj_wrapper.click_button(control, "Delete field")

    def verify_column_name_exists(self, field_name):
        control = (By.XPATH, "//table[@summary='Custom Lists Group']//td[contains(.,'" + field_name + "')]")
        exists = self.obj_wrapper.object_exists(control, "Field exists")
        if exists == 1:
            return True
        else:
            return False

    def select_delete_cap_data(self, delete_cap_data):
        if delete_cap_data == "Yes":
            self.obj_wrapper.click_checkbox(self.chk_delete_cap_data)

    def select_delete_checklist(self, delete_checklist):
        if delete_checklist == "Yes":
            self.obj_wrapper.click_checkbox(self.chk_delete_checklist)

    def select_delete_contact(self, delete_contact):
        if delete_contact == "Yes":
            self.obj_wrapper.click_checkbox(self.chk_delete_contact)

    def select_delete_meeting(self, delete_meeting):
        if delete_meeting == "Yes":
            self.obj_wrapper.click_checkbox(self.chk_delete_meeting)

    def select_delete_education(self, delete_education):
        if delete_education == "Yes":
            self.obj_wrapper.click_checkbox(self.chk_delete_education)

    # When we want to update a value of field, we need to write generic xpath because the field to be udpated is against a field name
    # So we are writing a generic code to update and enter values against that field
    # pass the column index(i.e. in which column the field exists on the webpage
    def update_enter_value(self, field_name, value, column_index, input_index = '1'):
        control = control = (By.XPATH, "//table[@summary='Custom Lists Group']"
                                       "//td[contains(.,'" + field_name + "')]//..//td[" + str(column_index) + "]//input["+ str(input_index)+"]")
        self.obj_wrapper.enter_text(control, "Field Update", value)

    def update_select_value(self, field_name, value, column_index):
        control = control = (By.XPATH, "//table[@summary='Custom Lists Group']"
                                       "//td[contains(.,'" + field_name + "')]//..//td[" + str(column_index) + "]//select")
        self.obj_wrapper.select_value_from_dropdown(control, "Field Update", value)

    # Selection of Custom List and Custom List subgroup
    def verify_custom_list_in_list_exists(self, custom_list):
        control = (By.XPATH, "//table[@summary='Custom Lists Group']//td[contains(.,'" + custom_list + "')]/..//td[1]//img")
        exists = self.obj_wrapper.object_exists(control, "Custom List in List")
        if exists == 1:
            return True
        else:
            return False

    def select_custom_list_from_list(self, custom_list_in_group):
        control = (By.XPATH, "//table[@summary='Custom Lists Group']//td[contains(.,'" + custom_list_in_group + "')]/..//td[1]//img")
        self.obj_wrapper.click_button(control, "Custom Field in List")

    def verify_custom_list_sub_group_exists(self, sub_group):
        control = (By.XPATH, "//form[@id='form1']//table//td[contains(.,'" + sub_group + "')]/..//td[1]//img")
        exists = self.obj_wrapper.object_exists(control, "Custom Field Sub Group in List")
        if exists == 1:
            return True
        else:
            return False

    def select_custom_list_sub_gorup_from_list(self, sub_group):
        control = (By.XPATH, "//form[@id='form1']//table//td[contains(.,'" + sub_group + "')]/..//td[1]//img")
        self.obj_wrapper.click_button(control, "Custom Field sub group in List")

    def delete_custom_list_sub_gorup_from_list(self, sub_group):
        control = (By.XPATH, "//form[@id='form1']//table//td[contains(.,'" + sub_group + "')]/..//td[5]//img[@alt='Delete Subgroup']")
        self.obj_wrapper.click_button(control, "Custom Field sub group in List")

    def select_display_field_on_existing_record(self, display_field_existing_record):
        if display_field_existing_record == "Yes":
            self.obj_wrapper.click_checkbox(self.rdo_Display_Field_on_Existing_Record_Yes)
        elif display_field_existing_record == "No":
            self.obj_wrapper.click_checkbox(self.rdo_Display_Field_on_Existing_Record_No)

    def select_display_field_on_existing_contact(self, display_field_existing_contact):
        if display_field_existing_contact == "Yes":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Contact_Yes,
                                          "Display Field existing Contact yes")
        elif display_field_existing_contact == "No":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Contact_No,
                                          "Display Field existing Contact no")

    def select_display_field_on_existing_meeting(self, display_field_existing_meeting):
        if display_field_existing_meeting == "Yes":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Meetings_Yes,
                                          "Display Field existing meeting yes")
        elif display_field_existing_meeting == "No":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Meetings_No,
                                          "Display Field existing meeting yes")

    def select_display_field_on_existing_education(self, display_field_existing_education):
        if display_field_existing_education == "Yes":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Education_Yes,
                                          "Display Field existing education yes")
        elif display_field_existing_education == "No":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Education_No,
                                          "Display Field existing education yes")

    def select_apply_changes_to(self, group):
        if group == "Subgroup":
            self.obj_wrapper.click_button(self.rdo_Apply_Changes_to_SubGroup, "Apply change to subgroup")
        elif group == "All":
            self.obj_wrapper.click_button(self.rdo_Apply_Changes_to_AllGroup, "All Group")

    def switch_to_add_field_window(self):
        self.obj_wrapper.switch_to_window("Accela Automation: Specific Info Table Column Add - R0205-E")

    def switch_to_delete_field_window(self):
        self.obj_wrapper.switch_to_window("admin/index.cfm")

    def switch_to_delete_subgroup_window(self):
        self.obj_wrapper.switch_to_window("Accela Automation: Custom Lists Subgroup - Delete")
