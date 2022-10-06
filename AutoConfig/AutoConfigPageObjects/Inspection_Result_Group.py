from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class InspectionResultGroupObjects:

    btn_Add = (By.XPATH, "//img[@alt='add']")
    btn_Add_Type = (By.XPATH, "//img[@alt='Add Result']")
    btn_Update_Type = (By.XPATH, "//img[@alt='Update Result']")
    txt_Result = (By.ID, "id_txtResult")
    txt_Group_Name = (By.ID, "id_txtResultGroup")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_add(self):
        self.obj_wrapper.click_button(self.btn_Add, "Add")

    def click_add_type(self):
        self.obj_wrapper.click_button(self.btn_Add_Type, "Add Type")

    def click_update_type(self):
        self.obj_wrapper.click_button(self.btn_Update_Type, "Update Type")

    def select_group_name_edit(self, group_name):
        control = (By.XPATH, "//form[@name = 'form1']//td[contains(.,'" + group_name  + "') and @class = 'InfoColumn']//..//a")
        self.obj_wrapper.click_button(control, "Group Name Edit")

    def verify_group_name_exists(self, group_name):
        control = (By.XPATH, "//form[@name = 'form1']//td[contains(.,'" + group_name + "') and @class = 'InfoColumn']")
        exists = self.obj_wrapper.object_exists(control, "Group name in list")
        if exists == 1:
            return True
        else:
            return False

    def enter_value(self, result, value, column_index):
        control = (By.XPATH, "//input[@value='" + result + "']/../following-sibling::td[" + str(column_index) + "]//input")
        self.obj_wrapper.enter_text(control, "Enter value", value)

    def select_value(self, result, value, column_index):
        control = (By.XPATH, "//input[@value='" + result + "']/../following-sibling::td[" + str(column_index) + "]//select")
        self.obj_wrapper.select_value_from_dropdown(control, "Select value", value)

    def delete_result(self, result):
        control = (By.XPATH, "//input[@value='" + result + "']/../following-sibling::td[7]//img")
        self.obj_wrapper.click_button(control, "Delete Result")

    def verify_result_exists(self, value):
        control = (By.XPATH, "//input[@value='" + value + "']")
        exists = self.obj_wrapper.object_exists(control, "Result Exists")
        if exists == 1:
            return True
        else:
            return False

    def enter_new_result(self, result):
        self.obj_wrapper.enter_text(self.txt_Result, "Result", result)

    def enter_group_code(self, group_code):
        self.obj_wrapper.enter_text(self.txt_Group_Name, "Group Code", group_code)

