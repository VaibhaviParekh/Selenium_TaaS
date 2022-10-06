
from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class AddtlInfoObjects:

    # Addtl Info page objects
    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")

    txt_Application_Job_Value = (By.ID, "value(bValuatnModel*estimatedValue)")
    txt_Number_of_Buildings = (By.ID, "value(capDetailModel*buildingCount)")
    txt_Housing_Units = (By.ID, "value(capDetailModel*houseCount)")
    cbo_Construction_Type = (By.ID, "value(capDetailModel*constTypeCode)")
    cbo_Public_Owned = (By.ID, "value(capDetailModel*publicOwned)")

    btn_Menu = (By.ID, "menu1Link")
    btn_Save = (By.ID, "Save")
    btn_Reset = (By.ID, "Reload")
    btn_Help = (By.ID, "Help")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def enter_application_job_value(self,app_job_value):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_Application_Job_Value, "Application Job Value", app_job_value)
        self.obj_wrapper.switch_to_default()

    def enter_number_of_buildings(self, no_of_buildings):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_Number_of_Buildings, "Number of Buildings", no_of_buildings)
        self.obj_wrapper.switch_to_default()

    def enter_housing_unit(self, housing_units):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_Housing_Units, "Housing Units", housing_units)
        self.obj_wrapper.switch_to_default()

    def select_construction_type(self, construction_type):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Construction_Type, "Construction Type", construction_type)
        self.obj_wrapper.switch_to_default()

    def select_public_owned(self, public_owned):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Public_Owned, "Public Owned", public_owned)
        self.obj_wrapper.switch_to_default()

    def save_addtl_info_data(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Save, "Save")
        self.obj_wrapper.switch_to_default()



