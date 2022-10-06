from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class IntakeApplicantContactObjects:

    # Applicant Objects
    frm1 = (By.ID, "applicantContactAddressListFrame")
    btn_search_applicant = (By.ID, "searchApplicant")
    lbl_applicant_success = (By.ID, "errorMsgPanel")
    txt_app_firstname = (By.ID, "value(applicant*firstName)")
    txt_app_lastname = (By.ID, "value(applicant*lastName)")
    txt_app_home_phone = (By.ID, "value(applicant*phone1_disp)")
    txt_app_business_phone = (By.ID, "value(applicant*phone2_disp)")
    txt_app_mobile_phone = (By.ID, "value(applicant*phone3_disp)")
    txt_app_email = (By.ID, "value(applicant*email)")

    # Contact Details
    frm2 = (By.ID, "contactListFrame")
    lbl_type = (By.ID, "value(capType)")
    btn_search_contact = (By.ID, "searchContact")
    lbl_contact_success = (By.ID, "err_msg")

    def __init__(self, drv):
        # Create instance of Wrappers class
        self.obj_wrapper = Wrappers(drv)

    # -------Applicant Search or Add
    # All action related to applicant search
    def click_search_applicant(self):
        self.obj_wrapper.click_button(self.btn_search_applicant, "Search Applicant")

    def verify_applicant_added(self):
        self.obj_wrapper.switch_to_window("New Record By Single")
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        success = self.obj_wrapper.get_text_for_webelement(self.lbl_applicant_success, "Contact Success")
        self.obj_wrapper.switch_to_default()
        if "1 contact address(es) added successfully." == success:
            return True
        else:
            return False

    def enter_app_firstname(self, firstname):
        self.obj_wrapper.enter_text(self.txt_app_firstname, "First Name", firstname)

    def enter_app_lastname(self, lastname):
        self.obj_wrapper.enter_text(self.txt_app_lastname, "Last Name", lastname)

    def enter_app_mobile_phone(self, mobile_phone):
        self.obj_wrapper.enter_text(self.txt_app_mobile_phone, "Mobile Phone", mobile_phone)

    def enter_app_business_phone(self, business_phone):
        self.obj_wrapper.enter_text(self.txt_app_business_phone, "Business Phone", business_phone)

    def enter_app_home_phone(self, home_phone):
        self.obj_wrapper.enter_text(self.txt_app_home_phone, "Home Phone", home_phone)

    def enter_app_email(self, email):
        self.obj_wrapper.enter_text(self.txt_app_email, "Email", email)

    # --------Contact Search or Add---------
    # Contact Search Objects
    def click_search_contact(self):
        self.obj_wrapper.click_button(self.btn_search_contact, "Search Contact")

    def verify_contact_added(self):
        self.obj_wrapper.switch_to_window("New Record By Single")
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        success = self.obj_wrapper.get_text_for_webelement(self.lbl_contact_success, "Contact Success")
        self.obj_wrapper.switch_to_default()
        if "1 contact address(es) added successfully." == success.strip():
            return True
        else:
            return False

    def update_contact_type(self, firstname, lastname, row_index, contact_type):
        self.obj_wrapper.switch_to_frame(self.frm2, "Contact Frame")
        con_type = (By.XPATH, "//td[contains(.,'" + firstname + "')]//..//td[contains(.,'" + lastname + "')]//tr[" + row_index+1 +"]//select[@name='value(contactsModel*contactType)']")
        self.obj_wrapper.select_value_from_dropdown(con_type, "Contact Type", contact_type)
        self.obj_wrapper.switch_to_default()