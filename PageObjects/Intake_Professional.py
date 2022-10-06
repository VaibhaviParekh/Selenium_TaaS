from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By
import time


class IntakeProfessionalObjects:

    frm1 = (By.ID, "professionalListFrame")
    search_professional = (By.ID, "searchProfessional")
    txt_license = (By.ID, "value(professionalModel*licensenbr)")
    cbo_license_type = (By.ID, "value(professionalModel*licensetype)")
    txt_first_name = (By.ID, "value(professionalModel*contactfirstname)")
    txt_last_name = (By.ID, "value(professionalModel*contactlastname)")
    txt_phone = (By.ID, "value(professionalModel*phone1_disp)")
    txt_email = (By.ID, "value(professionalModel*email)")
    txt_business_name = (By.ID, "value(professionalModel*businessname)")
    txt_address_line1 = (By.ID, "value(professionalModel*address1)")
    txt_city = (By.ID, "value(professionalModel*city)")
    txt_state = (By.ID, "value(professionalModel*state)")
    btn_select_license = (By.ID, "select4Single")
    lbl_professional_message = (By.ID, "errorMsgPanel")

    # Professional add on new record page
    def __init__(self, drv):
        # Create instance of Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def select_license_type(self, license_type):
        #self.obj_wrapper.switch_to_window("New Record By Single")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_license_type, "License Type", license_type)

    def enter_license_number(self, license_number):
        self.obj_wrapper.enter_text(self.txt_license, "License Number", license_number)

    def click_search_professional(self):
        self.obj_wrapper.click_button(self.search_professional, "Search Professional")

    def verify_license_exists(self, license_number):
        time.sleep(5)
        self.obj_wrapper.switch_to_window("Professional List")
        control = (By.XPATH, "//table[@id='AccelaMainTable']//td[contains(.,'" + license_number + "')]//..//input")
        exits = self.obj_wrapper.object_exists(control, "License Number in list")
        if exits == 1:
            return True
        else:
            return False

    def select_license_record(self, license_number):
        control = (By.XPATH, "//table[@id='AccelaMainTable']//td[contains(.,'" + license_number + "')]//..//input")
        self.obj_wrapper.click_checkbox(control)
        self.obj_wrapper.click_button(self.btn_select_license, "Select License")

    def enter_first_name(self, first_name):
        self.obj_wrapper.enter_text(self.txt_first_name, "First Name", first_name)

    def enter_last_name(self, last_name):
        self.obj_wrapper.enter_text(self.txt_last_name, "Last Name", last_name)

    def enter_business_name(self, business_name):
        self.obj_wrapper.enter_text(self.txt_business_name, "Business Name", business_name)

    def enter_address_line(self, address_line):
        self.obj_wrapper.enter_text(self.txt_address_line1, "Address Line 1", address_line)

    def enter_city(self, city):
        self.obj_wrapper.enter_text(self.txt_city, "City", city)

    def enter_state(self, state):
        self.obj_wrapper.enter_text(self.txt_state, "State", state)

    def enter_phone(self, phone):
        self.obj_wrapper.enter_text(self.txt_phone, "Phone", phone)

    def enter_email(self, email):
        self.obj_wrapper.enter_text(self.txt_email, "Email", email)

    def verify_professional_found(self):
        self.obj_wrapper.switch_to_window("New Record By Single")
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        abc = self.obj_wrapper.object_exists(self.lbl_professional_message, "Professional Success")
        message = self.obj_wrapper.get_text_for_webelement(self.lbl_professional_message, "Professional Success")
        self.obj_wrapper.switch_to_default()
        if message == "1 record(s) added successfully.":
            return True
        else:
            return False