from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class InspectionObjects:

    btn_Add = (By.XPATH, "//img[@alt='Add New Inspection Group']")
    btn_Add_Type = (By.XPATH, "//img[@alt='Add Type']")
    btn_Update_Type = (By.XPATH, "//img[@alt='Update Type']")
    txt_Inspection_Group_Code = (By.ID,"id_txtINSP_CODE")
    txt_Inspection_Group_Name = (By.ID, "id_txtINSP_NAME")
    txt_Inspection_Type = (By.ID, "txtINSP_TYPE")
    txt_Inspection_Type_Add = (By.ID, "id_txtINSP_TYPE")
    rdo_Configured_by_Inspection_Flow = (By.ID, "id_selConfigureByFlowOrMilestone_F")
    rdo_Configured_by_Inspection_Milestone = (By.ID, "id_selConfigureByFlowOrMilestone_M")
    rdo_Configured_by_None = (By.ID, "id_selConfigureByFlowOrMilestone_NONE")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_add(self):
        self.obj_wrapper.click_button(self.btn_Add, "Add")

    def click_add_type(self):
        self.obj_wrapper.click_button(self.btn_Add_Type, "Add Type")

    def click_update_type(self):
        self.obj_wrapper.click_button(self.btn_Update_Type, "Update Type")

    def enter_inspection_group_code(self, inspection_group_code):
        self.obj_wrapper.enter_text(self.txt_Inspection_Group_Code, "Inspection Group Code", inspection_group_code)

    def enter_inspection_group_name(self, inspection_group_name):
        self.obj_wrapper.enter_text(self.txt_Inspection_Group_Name, "Inspection Group Name", inspection_group_name)

    def select_configured_by(self, configured_by):
        if configured_by == "Inspection Flow":
            self.obj_wrapper.click_button(self.rdo_Configured_by_Inspection_Flow, "Inspection Flow")
        elif configured_by == "Inspection Milestone":
            self.obj_wrapper.click_button(self.rdo_Configured_by_Inspection_Milestone, "Inspection Milestone")
        elif configured_by == "None":
            self.obj_wrapper.click_button(self.rdo_Configured_by_None, "None")

    def enter_inspection_type(self, inspection_type):
        control = (By.XPATH, "//th[contains(.,'Inspection Type')]//ancestor::tr[1]//following-sibling::tr[2]//td//input")
        self.obj_wrapper.enter_text(control, "Inspection Type", inspection_type)

    def enter_inspection_type_add(self, inspection_type):
        self.obj_wrapper.enter_text(self.txt_Inspection_Type_Add, "Inspection Type", inspection_type)

    # Generic Xpath written in order to update the inspection type
    # Value selection against inspection type(Same row)
    def select_value_inspection_type(self, inspection_type, value, column_index):
        control = (By.XPATH, "//input[@value='" + inspection_type + "']//..//..//td[" + str(column_index) + "]//select")
        self.obj_wrapper.select_value_from_dropdown(control, "Inspection type selection", value)

    # Value enter against inspection type(Same row)
    def enter_value_inspection_type(self, inspection_type, value, column_index):
        control = (By.XPATH, "//input[@value='" + inspection_type + "']//..//..//td[" + str(column_index) + "]//input")
        self.obj_wrapper.enter_text(control, "Inspection type enter", value)

    # Selection of radio against inspection type
    def check_radio_value(self, inspection_type, value, column_index, row_index):
        control = (By.XPATH, "//input[@value='" + inspection_type + "']/../../following-sibling::tr[4]//"
                             "td[contains(.,'" + value + ":')]//tr[" + str(row_index) + "]//input[" + str(column_index) + "]")
        self.obj_wrapper.click_checkbox(control)

    # Selection of values against radio button dropdown
    def select_inspection_value(self, inspection_type, label, value, column_index, row_index):
        control = (By.XPATH, "//input[@value='" + inspection_type + "']/../../following-sibling::tr[4]//"
                        "td[contains(.,'" + label + ":')]//tr[" + str(row_index) + "]//select[" + str(column_index) + "]")
        self.obj_wrapper.select_value_from_dropdown(control, "Select value", value)

    # Selection of value against inspection type( Using label of that field)
    def select_value_using_label(self, inspection_type, label, value, row_index):
        control = (By.XPATH, "//input[@value='" + inspection_type + "']/../..//following-sibling::tr[" + str(row_index) + "]"
                            "//label[contains(.,'" + label + "')]/..//select")
        self.obj_wrapper.select_value_from_dropdown(control, "Select value", value)

    def click_department_link(self, inspection_type):
        control = (By.XPATH, "//input[@value='" + inspection_type + "']/../..//following-sibling::tr[3]//td//a//img[@alt = 'Search for Department']")
        self.obj_wrapper.click_button(control, "Department")

    def select_department(self, department):
        control = (By.XPATH, "//a[.='" + department + "']")
        exists = self.obj_wrapper.object_exists(control, "Department Value")
        if exists == 1:
            self.obj_wrapper.click_button(control, "Department")
        else:
            return False

    # Verify Inspection in the list exists
    def verify_inspection_group_exists(self, inspection_group_code):
        control = (By.XPATH, "//table[@summary='Inspection Group']//td[contains(.,'"+inspection_group_code+"')]")
        exists = self.obj_wrapper.object_exists(control, "Inspection Group Code")
        if exists == 1:
            return True
        else:
            return False

    def select_inspection_group_from_list(self, inspection_group_code):
        control = (By.XPATH, "//table[@summary='Inspection Group']//td[contains(.,'" + inspection_group_code + "')]//..//td[1]//img")
        self.obj_wrapper.click_button(control, "Inspection Group Code in list")

    def switch_to_add_type_window(self):
        self.obj_wrapper.switch_to_window("Accela Automation: RINSPTYPedit42 - R0133-A")

    def switch_to_department_selection_window(self):
        self.obj_wrapper.switch_to_window("Accela Automation: SelectGroup40 - T8093")

    def select_inspection_type_delete(self, inspection_type):
        control = (By.XPATH, "//input[@value='" + inspection_type + "']//ancestor::tr[1]//td[17]//a")
        self.obj_wrapper.click_button(control, "Inspection Delete")

    def inspection_type_exists(self, inspection_type):
        control = (By.XPATH, "//input[@value='" + inspection_type + "']")
        exists = self.obj_wrapper.object_exists(control, "Inspection Type")
        if exists == 1:
            return True
        else:
            return False