from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ACAContactInformationObject:

    # Page Objects Contact Information in ACA
    btn_Applicant_Select_from_Account = (By.XPATH, "//div[@class='contact_edit']//span[.='Select from Account']")

    frm1 = (By.ID, "ACADialogFrame")
    btn_Type_Contact = (By.ID, "ctl00_phPopup_ddlContactType")
    btn_Continue = (By.ID, "ctl00_phPopup_btnContinueContact")
    btn_Contact_Continue = (By.ID, "ctl00_phPopup_btnContinueContactAddress")
    lbl_Applicant_Success_Message = (By.XPATH, "//div[.='Applicant']//ancestor::div[2]//div[@class='contact_edit']//div//div[2]//span")
    lbl_Contact_Success_Message = (By.XPATH, "//h1[.='Contacts']//ancestor::div[3]//div[@class='contact_edit']//div//div[2]//span")
    lbl_Contact_List_Success = (By.XPATH, "//div[.='Contact List']//ancestor::div[2]//div[@class='contact_edit']//div//div[2]//span")

    # Contact Address Information
    Address_Type = (By.ID, "ctl00_phPopup_ucContactAddressEdit_ddlAddressType")
    Address_Line_1 = (By.ID, "ctl00_phPopup_ucContactAddressEdit_txtAddressLine1")
    Address_Line_2 = (By.ID, "ctl00_phPopup_ucContactAddressEdit_txtAddressLine2")
    City = (By.ID, "ctl00_phPopup_ucContactAddressEdit_txtCity")
    State = (By.ID, "ctl00_phPopup_ucContactAddressEdit_txtState_State1")
    Zip = (By.ID, "ctl00_phPopup_ucContactAddressEdit_txtZip")
    Continue_Address = (By.ID, "ctl00_phPopup_btnSave")
    Save_and_Close = (By.LINK_TEXT, "Sava and Close")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_select_from_account_applicant(self):
        self.obj_wrapper.click_button(self.btn_Applicant_Select_from_Account, "Applicant Select from Account")

    def select_address_type(self, address_type):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//span[contains(.,'" + address_type + "')]//ancestor::tr[1]//input")
        self.obj_wrapper.click_checkbox(control)
        self.obj_wrapper.switch_to_default()

    def click_continue(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Continue, "Continue")
        self.obj_wrapper.switch_to_default()

    def select_contact_type(self, contact_type):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//span[contains(.,'" + contact_type + "')]//ancestor::tr[1]//input")
        self.obj_wrapper.click_checkbox(control)
        self.obj_wrapper.switch_to_default()

    def click_contact_type_continue(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Contact_Continue, "Contact Continue")
        self.obj_wrapper.switch_to_default()

    def verify_contact_added(self):
        contact_success = self.obj_wrapper.get_text_for_webelement(self.lbl_Contact_Success_Message, "Success")
        if contact_success.strip() == "Contact added successfully.":
            return True
        else:
            return False

    def verify_applicant_added(self):
        applicant_success = self.obj_wrapper.get_text_for_webelement(self.lbl_Applicant_Success_Message, "Success")
        if applicant_success.strip() == "Contact added successfully.":
            return True
        else:
            return False

    def verify_contact_list_added(self):
        contact_list_success = self.obj_wrapper.get_text_for_webelement(self.lbl_Contact_List_Success, "Success")
        if contact_list_success.strip() == "Contact added successfully.":
            return True
        else:
            return False