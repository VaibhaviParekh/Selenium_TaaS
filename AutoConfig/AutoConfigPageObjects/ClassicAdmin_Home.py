from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ClassicAdminHomePageObjects:

    # Home page of Classic Admin. Where we can see all the menu options, Logout etc
    lnk_Civic_Platform = (By.LINK_TEXT, "Civic Platform")

    lnk_Menu_Agency_Profile = (By.ID, "Menu_AAgencyProfile")
    lnk_Menu_Fees = (By.ID, "Menu_AFees")
    lnk_Menu_Inspection = (By.ID, "Menu_AInspection")
    lnk_Menu_Workflow = (By.ID, "Menu_AWorkflow")
    lnk_Menu_Application = (By.ID, "Menu_AApplication")

    lnk_Fee_Schedule = (By.ID, "AFees_Fee Schedules")
    lnk_Fee_Item = (By.ID, "AFees_Fee Items")
    lnk_Custom_Fields = (By.ID, "AApplicationTD_Custom Fields")
    lnk_Custom_Lists = (By.ID, "AApplication_Custom Lists")
    lnk_Inspection = (By.ID, "AInspection_Inspection")
    lnk_Inspection_Result_Group = (By.ID, "AInspection_Inspection Result Group")
    lnk_Checklist = (By.ID, "AInspection_Checklist")
    lnk_Checklist_Group = (By.ID, "AInspection_Checklist Group")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_civic_platform(self):
        self.obj_wrapper.click_button(self.lnk_Civic_Platform, "Civic Platform")

    def select_menu(self, menu):
        if menu == "Inspection":
            self.navigate_inspection_menu()
        elif menu == "Fee":
            self.navigate_fee_menu()
        elif menu == "Workflow":
            self.navigate_workflow_menu()
        elif menu == "Application":
            self.navigate_application_menu()

    def select_menu_option(self, menu_option):
        if menu_option == "Fee Schedule":
            self.click_fee_schedule()
        elif menu_option == "Fee Item":
            self.click_fee_item()
        elif menu_option == "Custom Field":
            self.click_custom_field()
        elif menu_option == "Custom List":
            self.click_custom_list()
        elif menu_option == "Inspection":
            self.click_inspection()
        elif menu_option == "Inspection Result Group":
            self.click_inspection_result_group()
        elif menu_option == "Checklist":
            self.click_checklist()
        elif menu_option == "Checklist Group":
            self.click_checklist_group()

    def navigate_fee_menu(self):
        temp1 = self.obj_wrapper.is_clickable(self.lnk_Menu_Fees, "")
        self.obj_wrapper.click_button(self.lnk_Menu_Fees, "")

    def navigate_inspection_menu(self):
        self.obj_wrapper.mouse_hover(self.lnk_Menu_Inspection)

    def navigate_workflow_menu(self):
        self.obj_wrapper.mouse_hover(self.lnk_Menu_Workflow)

    def navigate_application_menu(self):
        self.obj_wrapper.mouse_hover(self.lnk_Menu_Application)

    def click_fee_item(self):
        self.obj_wrapper.click_button(self.lnk_Fee_Item, "Fee Item")

    def click_fee_schedule(self):
        self.obj_wrapper.click_button(self.lnk_Fee_Schedule, "Fee Schedule")

    def click_custom_field(self):
        self.obj_wrapper.click_button(self.lnk_Custom_Fields, "Custom Field")

    def click_custom_list(self):
        self.obj_wrapper.click_button(self.lnk_Custom_Lists, "Custom List")

    def click_inspection(self):
        self.obj_wrapper.click_button(self.lnk_Inspection, "Inspection")

    def click_inspection_result_group(self):
        self.obj_wrapper.click_button(self.lnk_Inspection_Result_Group, "Inspection Result Group")

    def click_checklist(self):
        self.obj_wrapper.click_button(self.lnk_Checklist, "Checklist")

    def click_checklist_group(self):
        self.obj_wrapper.click_button(self.lnk_Checklist_Group, "Checklist Group")