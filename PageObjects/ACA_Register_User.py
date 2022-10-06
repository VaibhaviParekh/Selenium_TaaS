from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ACARegisterUserObject:

    # Page Objects for Register User Page
    link_register_user = (By.ID, "ctl00_HeaderNavigation_lblRegister")
    chk_disclaimer = (By.ID, "ctl00_PlaceHolderMain_termAccept")
    btn_continue_registration_1 = (By.ID,"ctl00_PlaceHolderMain_btnRegister")
    btn_continue_registration_2 = (By.ID, "ctl00_PlaceHolderMain_StartNextButton2")
    txt_username = (By.ID, "ctl00_PlaceHolderMain_UserRegistration_txbUserName")
    txt_email = (By.ID, "ctl00_PlaceHolderMain_UserRegistration_txbEmail")
    txt_password = (By.ID, "ctl00_PlaceHolderMain_UserRegistration_txbPassword1")
    txt_type_password_again = (By.ID, "ctl00_PlaceHolderMain_UserRegistration_txbPassword2")
    txt_security_question = (By.ID, "ctl00_PlaceHolderMain_UserRegistration_ddlQuestionForDaily_ChildControl0")
    txt_answer = (By.ID, "ctl00_PlaceHolderMain_UserRegistration_txbAnswerForDaily_ChildControl0")

    btn_add_new_contact_information = (By.ID, "ctl00_PlaceHolderMain_contactEdit_btnAddNew")
    frm1 = (By.ID, "ACADialogFrame")
    cbo_select_contact_type = (By.ID, "ctl00_phPopup_ddlContactType")
    btn_continue = (By.ID, "ctl00_phPopup_btnContinue")

    # Contact details objects
    txt_FirstName = (By.ID, "ctl00_phPopup_ucContactInfo_txtAppFirstName")
    txt_MiddleName = (By.ID, "")
    txt_LastName = (By.ID, "ctl00_phPopup_ucContactInfo_txtAppLastName")
    txt_Email_Cont = (By.ID, "ctl00_phPopup_ucContactInfo_txtAppEmail")
    cbo_Country = (By.ID, "ctl00_phPopup_ucContactInfo_ddlAppCountry")
    txt_Mobile_phone = (By.ID, "ctl00_phPopup_ucContactInfo_txtAppPhone2")
    txt_Home_phone = (By.ID, "ctl00_phPopup_ucContactInfo_txtAppPhone1")
    txt_Work_Phone = (By.ID, "ctl00_phPopup_ucContactInfo_txtAppPhone3")
    txt_Business_Name = (By.ID, "ctl00_phPopup_ucContactInfo_txtAppOrganizationName")
    btn_Contact_Continue = (By.ID, "ctl00_phPopup_btnSave")
    btn_Add_Additional_Contact_Information = (By.ID, "ctl00_phPopup_ucContactInfo_contactAddressList_btnAddContactAddress")
    txt_userCreated = (By.ID, "ctl00_PlaceHolderMain_registerSuccessInfo_lblMessage")

    cbo_Address_Type = (By.ID, "ctl00_phPopup_ucContactAddressEdit_ddlAddressType")
    txt_Address_Line1 = (By.ID, "ctl00_phPopup_ucContactAddressEdit_txtAddressLine1")
    txt_Address_Line2 = (By.ID, "ctl00_phPopup_ucContactAddressEdit_txtAddressLine2")
    txt_Address_Line3 = (By.ID, "ctl00_phPopup_ucContactAddressEdit_txtAddressLine3")
    txt_City = (By.ID, "ctl00_phPopup_ucContactAddressEdit_txtCity")
    cbo_State = (By.ID, "ctl00_phPopup_ucContactAddressEdit_txtState_State1")
    txt_Zip_Code = (By.ID, "ctl00_phPopup_ucContactAddressEdit_txtZip")
    btn_Save_and_Close = (By.ID, "ctl00_phPopup_btnSave")

    lbl_success = (By.ID, "ctl00_phPopup_ucContactInfo_contactAddressList_lblActionNoticeAddSuccess")
    lbl_success_contact = (By.ID, "ctl00_PlaceHolderMain_contactEdit_lblActionNoticeAddSuccess")
    lbl_success_register = (By.ID, "ctl00_PlaceHolderMain_registerSuccessInfo_messageBar")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def verify_success_registration(self):
        success = self.obj_wrapper.object_exists(self.lbl_success_register, "Register")
        if success == 1:
            return True
        else:
            return False

    def click_register_user_link(self):
        self.obj_wrapper.click_button(self.link_register_user, "Link Register User")

    def click_disclaimer(self):
        abc = self.obj_wrapper.object_exists(self.chk_disclaimer, "Disclaimer")
        self.obj_wrapper.click_checkbox(self.chk_disclaimer)

    def click_continue_registration_1(self):
        self.obj_wrapper.click_button(self.btn_continue_registration_1, "Continue Registration 1")

    def click_continue_registration_2(self):
        self.obj_wrapper.click_button(self.btn_continue_registration_2, "Continue Registration 2")

    def enter_username(self, username):
        self.obj_wrapper.enter_text(self.txt_username, "User Name", username)

    def enter_email(self, email):
        self.obj_wrapper.enter_text(self.txt_email, "Email", email)

    def enter_password(self, password):
        self.obj_wrapper.enter_text(self.txt_password, "Password", password)

    def enter_password_again(self, password_again):
        self.obj_wrapper.enter_text(self.txt_type_password_again, "Type Password again", password_again)

    def enter_security_question(self, security_question):
        self.obj_wrapper.enter_text(self.txt_security_question, "Security Question", security_question)

    def enter_answer(self, answer):
        self.obj_wrapper.enter_text(self.txt_answer, "Answer", answer)

    def click_add_new_contact_information(self):
        self.obj_wrapper.click_button(self.btn_add_new_contact_information, "Add New")

    def select_contact_type(self, type):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_select_contact_type, "Contact Type", type)

    def click_continue(self):
        self.obj_wrapper.click_button(self.btn_continue, "Continue")
        self.obj_wrapper.switch_to_default()

    def enter_first_name(self, first_name):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_FirstName, "First Name", first_name)

    def enter_middle_name(self, middle_name):
        self.obj_wrapper.enter_text(self.txt_MiddleName, "Middle Name", middle_name)

    def enter_last_name(self, last_name):
        self.obj_wrapper.enter_text(self.txt_LastName, "Last Name", last_name)

    def select_country(self, country):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Country, "Country", country)

    def enter_contact_email(self, email):
        self.obj_wrapper.enter_text(self.txt_Email_Cont, "Email", email)

    def enter_mobile_phone(self, mobile_phone):
        self.obj_wrapper.enter_text(self.txt_Mobile_phone, "Mobile Phone", mobile_phone)

    def enter_work_phone(self, work_phone):
        self.obj_wrapper.enter_text(self.txt_Work_Phone, "Work Phone", work_phone)

    def enter_home_phone(self, home_phone):
        self.obj_wrapper.enter_text(self.txt_Home_phone, "Home Phone", home_phone)

    def enter_name_of_business(self, name_of_business):
        self.obj_wrapper.enter_text(self.txt_Business_Name, "Business Name", name_of_business)
        #self.obj_wrapper.switch_to_default()

    def click_continue_contact_info(self):
        #self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Contact_Continue, "Contact Continue")
        self.obj_wrapper.switch_to_default()

    def click_add_additional_info(self):
        #self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Add_Additional_Contact_Information, "Additional Contact Info")
        #self.obj_wrapper.switch_to_default()

    def select_address_type(self, address_type):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Address_Type, "Address Type", address_type)

    def enter_address_line1(self, address_line1):
        self.obj_wrapper.enter_text(self.txt_Address_Line1, "Address Line", address_line1)

    def enter_address_line2(self, address_line2):
        self.obj_wrapper.enter_text(self.txt_Address_Line2, "Address Line", address_line2)

    def enter_address_line3(self, address_line3):
        self.obj_wrapper.enter_text(self.txt_Address_Line3, "Address Line", address_line3)

    def enter_city(self, city):
        self.obj_wrapper.enter_text(self.txt_City, "City", city)

    def select_state(self, state):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_State, "State", state)

    def enter_zip(self, zip):
        self.obj_wrapper.enter_text(self.txt_Zip_Code, "Zip Code", zip)

    def click_save_and_close(self):
        self.obj_wrapper.click_button(self.btn_Save_and_Close, "Save and Close")
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    def verify_contact_address_success(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        success = self.obj_wrapper.get_text_for_webelement(self.lbl_success, "Success")
        if success.strip() == "Contact address added successfully.":
            return True
        else:
            return False

    def verify_contact_success(self):
        success = self.obj_wrapper.get_text_for_webelement(self.lbl_success_contact, "Success")
        if success.strip() == "Contact added successfully.":
            return True
        else:
            return False