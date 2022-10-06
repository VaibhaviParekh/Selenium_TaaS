from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class ACALicenseProfessional:

    # License Professional Information
    frm1 = (By.ID, "ACADialogFrame")
    cbo_License_Type = (By.ID, "ctl00_phPopup_licenseInput_ddlLicenseType")
    txt_License_Number = (By.ID, "ctl00_phPopup_licenseInput_txtLicenseNum")
    btn_License_Search = (By.ID, "ctl00_phPopup_btnSearch")
    btn_License_Profession_Select_from_Account = (By.XPATH, "//div[@class='license_edit']//span[.='Select from Account']")
    btn_License_Professional_LookUp = (By.XPATH, "//div[@class='license_edit']//span[.='Look Up']")
    btn_continue = (By.ID, "ctl00_phPopup_btnContinue")
    lbl_success = (By.XPATH, "//div[.='Licensed Professional']//ancestor::div[2]//div[2]//span[@class='Notice_Message_Success']")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_select_from_account_license_professional(self):
        self.obj_wrapper.click_button(self.btn_License_Profession_Select_from_Account, "Select from Account")

    def click_look_up(self):
        self.obj_wrapper.click_button(self.btn_License_Professional_LookUp, "Lookup")

    def select_license_type(self, license_type):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_License_Type, "License Type", license_type)

    def enter_license_number(self, license_number):
        self.obj_wrapper.enter_text(self.txt_License_Number, "License Number", license_number)

    def click_license_search(self):
        self.obj_wrapper.click_button(self.btn_License_Search, "License Search")
        self.obj_wrapper.switch_to_default()

    def verify_license_professional_added(self):
        lp_success = self.obj_wrapper.object_exists(self.lbl_success, "Success")
        if lp_success == 1:
            return True
        else:
            return False