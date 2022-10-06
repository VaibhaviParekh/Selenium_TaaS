from PageObjects.ACA_Register_User import ACARegisterUserObject
from Views.ACA_Common_View import ACACommonView
from PageObjects.ACA_Login_Logout import ACALoginLogoutObject


class ACARegisterUserView:

    def __init__(self, drv):
        # Create instance of the ACA Register User Page Objects
        self.obj_driver = drv
        self.obj_aca_register_user = ACARegisterUserObject(drv)
        self.obj_aca_login = ACALoginLogoutObject(drv)
        self.obj_common = ACACommonView(drv)

    def aca_register_user(self, user_name, email, password, type_password, security_question, answer):
        self.obj_aca_register_user.click_register_user_link()
        #self.obj_common.aca_wait_for_spinner()
        self.obj_aca_register_user.click_disclaimer()
        self.obj_aca_register_user.click_continue_registration_1()
        self.obj_aca_register_user.enter_username(user_name)
        self.obj_aca_register_user.enter_email(email)
        self.obj_aca_register_user.enter_password(password)
        self.obj_aca_register_user.enter_password_again(type_password)
        self.obj_aca_register_user.enter_security_question(security_question)
        self.obj_aca_register_user.enter_answer(answer)

    def enter_contact_information(self,contact_type, firstname, lastname, country, email, mobile, workphone, homephone, businessname):
        self.obj_aca_register_user.click_add_new_contact_information()
        self.obj_aca_register_user.select_contact_type(contact_type)
        self.obj_aca_register_user.click_continue()

        self.obj_aca_register_user.enter_first_name(firstname)
        self.obj_aca_register_user.enter_last_name(lastname)
        self.obj_aca_register_user.select_country(country)
        self.obj_aca_register_user.enter_contact_email(email)
        self.obj_aca_register_user.enter_mobile_phone(mobile)
        self.obj_aca_register_user.enter_work_phone(workphone)
        self.obj_aca_register_user.enter_home_phone(homephone)
        self.obj_aca_register_user.enter_name_of_business(businessname)

    def enter_additional_contact_address(self, type_address, addressline1, city, state, zip):
        self.obj_aca_register_user.click_add_additional_info()
        self.obj_aca_register_user.select_address_type(type_address)
        self.obj_aca_register_user.enter_address_line1(addressline1)
        self.obj_aca_register_user.enter_city(city)
        self.obj_aca_register_user.select_state(state)
        self.obj_aca_register_user.enter_zip(zip)
        self.obj_aca_register_user.click_save_and_close()
        success = self.obj_aca_register_user.verify_contact_address_success()
        if success == 1:
            print("Additional Contact Information added successfully")
        else:
            print("Additional Contact Information not added")

        self.obj_aca_register_user.click_continue_contact_info()
        success_contact = self.obj_aca_register_user.verify_contact_success()
        if success_contact == 1:
            print("Contact Information added successfully")
        else:
            print("Contact Information not added")

    def verify_user_registered(self):
        self.obj_aca_register_user.click_continue_registration_2()
        self.obj_common.aca_wait_for_spinner()
        register = self.obj_aca_register_user.verify_success_registration()
        if register == 1:
            print("User Registered Successfully")
        else:
            print("User not Registered Successfully")
        self.obj_aca_login.click_login_link()