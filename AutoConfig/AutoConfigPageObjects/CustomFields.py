from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class CustomFieldsObjects:

    # Page Objects related to Custom Fields

    btn_Add = (By.XPATH, "//img[@alt='Add New Custom Fields Group']")
    btn_Add_Subgroup = (By.XPATH, "//img[@alt = 'Add existing Custom Fields Subgroup']")
    btn_Update_Subgroup = (By.XPATH, "Update Subgroups")
    btn_New_Subgroup = (By.XPATH, "Add New Custom Fields Subgroup")
    btn_Update = (By.XPATH, "//input[@alt = 'Update with changes']")
    btn_Add_New_Field = (By.XPATH, "//img[@alt = 'Add new Field']")

    txt_Custom_Fields_Group_Code = (By.ID, "id_txtR1_CHECKBOX_CODE")
    txt_Custom_Fields_SubGroup = (By.ID, "id_txtR1_CHECKBOX_TYPE")
    cbo_Custom_Lists_Group = (By.ID, "tableGroupName")
    txt_Group_Display_Order = (By.ID, "id_txtR1_CHECKBOX_GROUP_ORDER")
    txt_First_Field_Label = (By.ID, "id_txtR1_CHECKBOX_DESC")
    txt_Field_Label_Alias = (By.ID, "id_txtR1_CHECKBOX_DESC_ALIAS")
    cbo_Field_Type = (By.ID, "txtR1_CHECKBOX_IND")
    txt_Display_Order = (By.ID, "id_txtR1_DISPLAY_ORDER")
    txt_Default_Value = (By.ID, "id_avalue")
    cbo_Unit = (By.ID, "aunitdd")
    txt_New_Unit = (By.ID, "id_aunit")
    txt_Fee_Indicator = (By.ID, "id_R1_FEE_INDICATOR")
    rdo_Required_Flag_Yes = (By.ID, "id_areqflag_Y")
    rdo_Required_Flag_No = (By.ID, "id_areqflag_N")
    rdo_Req_for_Fee_Calc_Yes = (By.ID, "id_reqfeecalc_Y")
    rdo_Req_for_Fee_Calc_No = (By.ID, "id_reqfeecalc_N")
    rdo_Supervisor_Edit_Only_Yes = (By.ID, "id_supervisoreditonly_Y")
    rdo_Supervisor_Edit_Only_No = (By.ID, "id_supervisoreditonly_N")
    rdo_Searchable_Flag_Yes = (By.ID, "id_searchableFlag_Y")
    rdo_Searchable_Flag_No = (By.ID, "id_searchableFlag_N")
    txt_Max_Len = (By.ID, "id_maxLength")
    txt_Display_Len = (By.ID, "id_displayLength")
    rdo_ACA_Displayable_Yes = (By.ID, "id_vchdisplayflag_Y")
    rdo_ACA_Displayable_Hidden = (By.ID, "id_vchdisplayflag_H")
    rdo_ACA_Displayable_No = (By.ID, "id_vchdisplayflag_N")
    rdo_ACA_Searchable_Yes = (By.ID, "id_searchableForACA_Y")
    rdo_ACA_Searchable_No = (By.ID, "id_searchableForACA_N")
    cbo_Justification = (By.ID, "id_alignmentflag")
    txt_Default_APO_GIS_Layer = (By.ID, "id_defaultAPOGISLayer")
    rdo_Location_Query_Yes = (By.ID, "id_locationQuery_Y")
    rdo_Location_Query_No = (By.ID, "id_locationQuery_N")
    rdo_Status_Enable = (By.ID, "id_aenableflag_Y")
    rdo_Status_Disable = (By.ID, "id_aenableflag_N")

    rdo_Apply_Changes_to_SubGroup = (By.ID, "id_applychange_one")
    rdo_Apply_Changes_to_AllGroup = (By.ID, "id_applychange_all")
    rdo_Display_Field_on_Existing_Record_Yes = (By.ID, "id_applyToOldFlag_Y")
    rdo_Display_Field_on_Existing_Record_No = (By.ID, "id_applyToOldFlag_N")
    rdo_Display_Field_on_Existing_Contact_Yes = (By.ID, "id_applyToOldContactFlag_Y")
    rdo_Display_Field_on_Existing_Contact_No = (By.ID, "id_applyToOldContactFlag_N")
    rdo_Display_Field_on_Existing_Meetings_Yes = (By.ID, "id_applyToOldMeetingFlag_Y")
    rdo_Display_Field_on_Existing_Meetings_No = (By.ID, "id_applyToOldMeetingFlag_Y")
    rdo_Display_Field_on_Existing_Education_Yes = (By.ID, "id_applyToOldLCFlag_Y")
    rdo_Display_Field_on_Existing_Education_No = (By.ID, "id_applyToOldLCFlag_N")
    txt_alternative_aca_label = (By.ID, "id_txtR1_CHECKBOX_ALT")

    chk_delete_cap_data = (By.ID, "id_selectOptions_CAP")
    chk_delete_checklist = (By.ID, "id_selectOptions_GS")
    chk_delete_contact = (By.ID, "id_selectOptions_CONTACT")
    chk_delete_meeting = (By.ID, "id_selectOptions_MEETING")
    chk_delete_education = (By.ID, "id_selectOptions_LC")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_add(self):
        self.obj_wrapper.click_button(self.btn_Add, "Add")

    def click_add_subgroup(self):
        self.obj_wrapper.click_button(self.btn_Add_Subgroup, "Add Subgroup")

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

    def enter_custom_fields_group_code(self, custom_fields_group_code):
        self.obj_wrapper.enter_text(self.txt_Custom_Fields_Group_Code, "Custom Fields Group Code", custom_fields_group_code)

    def enter_custom_fields_subgroup(self, custom_fields_subgroup):
        self.obj_wrapper.enter_text(self.txt_Custom_Fields_SubGroup, "Sub Group", custom_fields_subgroup)

    def select_custom_lists_group(self, custom_lists_group):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Custom_Lists_Group, "Custom Lists Group", custom_lists_group)

    def enter_group_display_order(self, group_display_order):
        self.obj_wrapper.enter_text(self.txt_Group_Display_Order, "Group Display Order", group_display_order)

    def enter_first_field_label(self, first_field_label):
        self.obj_wrapper.enter_text(self.txt_First_Field_Label, "First Field Label", first_field_label)

    def enter_field_label_alias(self, field_label_alias):
        self.obj_wrapper.enter_text(self.txt_Field_Label_Alias, "Field Label Alias", field_label_alias)

    def select_field_type(self, field_type):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Field_Type, "Field Type", field_type)

    def enter_display_order(self, display_order):
        self.obj_wrapper.enter_text(self.txt_Display_Order, "Display Order", display_order)

    def enter_default_value(self, default_value):
        self.obj_wrapper.enter_text(self.txt_Default_Value, "Default Value", default_value)

    def select_unit(self, unit):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Unit, "Unit", unit)

    def enter_new_unit(self, new_unit):
        self.obj_wrapper.enter_text(self.txt_New_Unit, "New Unit", new_unit)

    def enter_fee_indicator(self, fee_indicator):
        self.obj_wrapper.enter_text(self.txt_Fee_Indicator, "Fee Indicator", fee_indicator)

    def select_required_flag(self, required_flag, req_for_fee_calc):
        if required_flag == "Yes":
            self.obj_wrapper.click_button(self.rdo_Required_Flag_Yes, "Required Flag Yes")
            self.select_req_for_fee_calc(req_for_fee_calc)
        elif required_flag == "No":
            self.obj_wrapper.click_button(self.rdo_Required_Flag_No, "Required Flag No")

    def select_req_for_fee_calc(self, req_for_fee_calc):
        if req_for_fee_calc == "Yes":
            self.obj_wrapper.click_button(self.rdo_Req_for_Fee_Calc_Yes, "Req for fee calc Yes")
        elif req_for_fee_calc == "No":
            self.obj_wrapper.click_button(self.rdo_Req_for_Fee_Calc_No, "Req for fee calc No")

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

    def enter_max_len(self, max_len):
        self.obj_wrapper.enter_text(self.txt_Max_Len, "Max Len", max_len)

    def enter_display_len(self, display_len):
        self.obj_wrapper.enter_text(self.txt_Display_Len, "Display Len", display_len)

    def select_aca_displayable(self, aca_displayable):
        if aca_displayable == "Yes":
            self.obj_wrapper.click_button(self.rdo_ACA_Displayable_Yes, "ACA Displayable Yes")
        elif aca_displayable == "Hidden":
            self.obj_wrapper.click_button(self.rdo_ACA_Displayable_Hidden, "ACA Displayable Hidden")
        elif aca_displayable == "No":
            self.obj_wrapper.click_button(self.rdo_ACA_Displayable_No, "ACA Displayable No")

    def select_aca_searchable(self, aca_searchable):
        if aca_searchable == "Yes":
            self.obj_wrapper.click_button(self.rdo_ACA_Searchable_Yes, "ACA Searchable Yes")
        elif aca_searchable == "No":
            self.obj_wrapper.click_button(self.rdo_ACA_Searchable_No, "ACA Searchable No")

    def select_justification(self, justification):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Justification, "Justification", justification)

    def enter_default_apo_gis_layer(self, apo_gis_layer):
        self.obj_wrapper.enter_text(self.txt_Default_APO_GIS_Layer, "Default APO GIS Layer", apo_gis_layer)

    def select_location_query(self, location_query):
        if location_query == "Yes":
            self.obj_wrapper.click_button(self.rdo_Location_Query_Yes, "Location Query Yes")
        elif location_query == "No":
            self.obj_wrapper.click_button(self.rdo_Location_Query_No, "Location Query No")

    def select_status(self, status):
        if status == "Enabled":
            self.obj_wrapper.click_checkbox(self.rdo_Status_Enable)
        elif status == "Disabled":
            self.obj_wrapper.click_checkbox(self.rdo_Status_Disable)

    def verify_custom_field_in_list_exists(self, custom_field):
        control = (By.XPATH, "//table[@summary='Specific Information Groups']//td[contains(.,'" + custom_field + "')]/..//td[1]//img")
        exists = self.obj_wrapper.object_exists(control, "Custom Field in List")
        if exists == 1:
            return True
        else:
            return False

    def select_custom_field_from_list(self, custom_field):
        control = (By.XPATH, "//table[@summary='Specific Information Groups']//td[contains(.,'" + custom_field + "')]/..//td[1]//img")
        self.obj_wrapper.click_button(control, "Custom Field in List")

    def verify_custom_field_sub_group_exists(self, sub_group):
        control = (By.XPATH, "//table[@summary='Sub Groups']//td[contains(.,'" + sub_group + "')]/..//td[1]//img")
        exists = self.obj_wrapper.object_exists(control, "Custom Field Sub Group in List")
        if exists == 1:
            return True
        else:
            return False

    def select_custom_field_sub_gorup_from_list(self, sub_group):
        control = (By.XPATH, "//table[@summary='Sub Groups']//td[contains(.,'" + sub_group + "')]/..//td[1]//img")
        self.obj_wrapper.click_button(control, "Custom Field sub group in List")

    def select_custom_field_sub_group_to_delete(self, sub_group):
        control = (By.XPATH, "//table[@summary='Sub Groups']//td[contains(.,'" + sub_group + "')]/..//td[4]//a[3]")
        self.obj_wrapper.click_button(control, "Custom Field sub group in List")

    def select_display_field_on_existing_record(self, display_field_existing_record):
        if display_field_existing_record == "Yes":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Record_Yes, "Display Field existing record yes")
        elif display_field_existing_record == "No":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Record_No, "Display Field existing record No")

    def select_display_field_on_existing_contact(self, display_field_existing_contact):
        if display_field_existing_contact == "Yes":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Contact_Yes, "Display Field existing Contact yes")
        elif display_field_existing_contact == "No":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Contact_No, "Display Field existing Contact no")

    def select_display_field_on_existing_meeting(self, display_field_existing_meeting):
        if display_field_existing_meeting == "Yes":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Meetings_Yes, "Display Field existing meeting yes")
        elif display_field_existing_meeting == "No":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Meetings_No, "Display Field existing meeting yes")

    def select_display_field_on_existing_education(self, display_field_existing_education):
        if display_field_existing_education == "Yes":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Education_Yes, "Display Field existing education yes")
        elif display_field_existing_education == "No":
            self.obj_wrapper.click_button(self.rdo_Display_Field_on_Existing_Education_No, "Display Field existing education yes")

    def enter_alternative_aca_label(self, alternative_aca_label):
        self.obj_wrapper.enter_text(self.txt_alternative_aca_label, "Alternative ACA Label", alternative_aca_label)

    def select_apply_changes_to(self, group):
        if group == "Subgroup":
           self.obj_wrapper.click_button(self.rdo_Apply_Changes_to_SubGroup, "Apply change to subgroup")
        elif group == "All":
            self.obj_wrapper.click_button(self.rdo_Apply_Changes_to_AllGroup, "All Group")

    def select_field_to_delete(self, field_name):
        control = (By.XPATH, "//table[@summary='Task Specific Information']//td[contains(.,'" + field_name + "')]//..//td[21]//a")
        self.obj_wrapper.click_button(control, "Delete field")

    def verify_field_exists(self, field_name):
        control = (By.XPATH, "//table[@summary='Task Specific Information']//td[contains(.,'" + field_name + "')]")
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
        control = (By.XPATH, "//table[@summary='Task Specific Information']//td[contains(.,'" + field_name + "')]//..//td[" + str(column_index) + "]//input["+ str(input_index)+"]")
        self.obj_wrapper.enter_text(control, "Field Update", value)

    def update_select_value(self, field_name, value, column_index):
        control = (By.XPATH, "//table[@summary='Task Specific Information']//td[contains(.,'" + field_name + "')]//..//td[" + str(column_index) + "]//select")
        self.obj_wrapper.select_value_from_dropdown(control, "Field Update", value)

    def switch_to_add_field_window(self):
        self.obj_wrapper.switch_to_window("Accela Automation: Specific Info Field Add - R0072-E")

    def switch_to_delete_field_window(self):
        self.obj_wrapper.switch_to_window("Accela Automation: Custom Fields -Delete")

    def switch_to_delete_subgroup_window(self):
        self.obj_wrapper.switch_to_window("Accela Automation: Custom Fields Subgroup -Delete")