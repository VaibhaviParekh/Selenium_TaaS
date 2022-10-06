from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class InspectionChecklistObjects:
    btn_Add = (By.XPATH, "//img[@alt='Add Checklist Group']")
    btn_Add_Type = (By.XPATH, "//img[@alt='Add Guide Type']")
    txt_Result = (By.ID, "id_txtResult")
    txt_Group_Name = (By.ID, "id_txtGuideGroup")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_add(self):
        self.obj_wrapper.click_button(self.btn_Add, "Add")

    def click_add_type(self):
        self.obj_wrapper.click_button(self.btn_Add_Type, "Add Type")

    def enter_group_name(self, group_name):
        self.obj_wrapper.enter_text(self.txt_Group_Name, "Group Name", group_name)

    def select_group_name_edit(self, group_name):
        control = (By.XPATH, "//table[@summary = 'Checklist Group']//td[contains(.,'" + group_name + "')]//..//a")
        self.obj_wrapper.click_button(control, "Group Name Edit")

    def verify_group_name_exists(self, group_name):
        control = (By.XPATH, "//table[@summary = 'Checklist Group']//td[contains(.,'" + group_name + "')]//..//a")
        exists = self.obj_wrapper.object_exists(control, "Group name in list")
        if exists == 1:
            return True
        else:
            return False

    def verify_reference_checklist_exists(self, reference_checklist):
        control = (By.XPATH, "//form[@name = 'form1']//td[contains(.,'" + reference_checklist + "')]")
        exists = self.obj_wrapper.object_exists(control, "Reference Checklist Exists")
        if exists == 1:
            return True
        else:
            return False

    def enter_value(self, reference_checklist, value):
        control = (By.XPATH, "//form[@name = 'form1']//td[contains(.,'" + reference_checklist + "')]//..//td[1]//input")
        self.obj_wrapper.enter_text(control, "Enter value", value)

    def check_value(self, reference_checklist, value, column_index):
        control = (By.XPATH, "//form[@name = 'form1']//td[contains(.,'" + reference_checklist + "')]//..//td[" + column_index + "]//input")
        selection = self.obj_wrapper.get_checkbox_selection(control)
        if selection == "checked":
            if value == "yes":
                pass
            else:
                self.obj_wrapper.click_button(control, "Auto Create/ Ad Hoc")

        if selection == "unchecked":
            if value == "no":
                pass
            else:
                self.obj_wrapper.click_button(control, "Auto Create/ Ad Hoc")

    def remove_reference_checklist(self, reference_checklist):
        control = (By.XPATH, "//form[@name = 'form1']//td[contains(.,'" + reference_checklist + "')]//..//td[5]//img")
        self.obj_wrapper.click_button(control, "Delete Result")

    def select_reference_checklist(self, reference_checklist):
        control = (By.XPATH, "//label[.='" + reference_checklist + "']//..//..//input")
        self.obj_wrapper.click_button(control, "Reference Checklist")