from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ACAAddressObject:

    # Page Objects Address in ACA
    txt_Street_Number = (By.ID, "ctl00_PlaceHolderMain_WorkLocationEdit_txtStreetNo")
    txt_Street_Name = (By.ID, "ctl00_PlaceHolderMain_WorkLocationEdit_txtStreetName")
    txt_Zip = (By.ID, "ctl00_PlaceHolderMain_WorkLocationEdit_txtZip")
    txt_Parcel_Number = (By.ID, "ctl00_PlaceHolderMain_ParcelEdit_txtParcelNo")
    txt_Unit_Number = (By.ID, "ctl00_PlaceHolderMain_WorkLocationEdit_txtUnitNo")
    txt_City = (By.ID, "ctl00_PlaceHolderMain_WorkLocationEdit_txtCity")
    cbo_Street_Type = (By.ID, "ctl00_PlaceHolderMain_WorkLocationEdit_ddlStreetSuffix")
    cbo_State = (By.ID, "ctl00_PlaceHolderMain_WorkLocationEdit_txtState_State1")
    cbo_Direction = (By.ID, "ctl00_PlaceHolderMain_WorkLocationEdit_ddlStreetDirection")
    btn_Search = (By.ID, "ctl00_PlaceHolderMain_WorkLocationEdit_btnSearch")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def enter_street_number(self, street_number):
        self.obj_wrapper.enter_text(self.txt_Street_Number, "Street Name", street_number)

    def select_direction(self, direction):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Direction, "Direction", direction)

    def enter_street_name(self, street_name):
        self.obj_wrapper.enter_text(self.txt_Street_Name, "Street Name", street_name)

    def select_street_type(self, street_type):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Street_Type, "Street Type", street_type)

    def enter_zip(self, zip):
        self.obj_wrapper.enter_text(self.txt_Zip, "Zip", zip)

    def click_search(self):
        self.obj_wrapper.click_button(self.btn_Search, "Search")

