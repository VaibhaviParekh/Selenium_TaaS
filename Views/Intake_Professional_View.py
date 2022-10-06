from PageObjects.Intake_Professional import IntakeProfessionalObjects
import time


class IntakeProfessionalView:

    def __init__(self, drv):
        # Create instance of the Professional Objects
        self.obj_driver = drv
        self.obj_professional = IntakeProfessionalObjects(drv)

    def search_license_professional(self, license_type, license_number):
        try:
            self.obj_professional.select_license_type(license_type)
            self.obj_professional.enter_license_number(license_number)
            self.obj_professional.click_search_professional()
            exists = self.obj_professional.verify_license_exists(license_number)
            if exists == 1:
                self.obj_professional.select_license_record(license_number)
                time.sleep(3)
                license_found = self.obj_professional.verify_professional_found()
                if license_found == 1:
                    print("License added successfully")
                else:
                    print("License not added successfully")
            else:
                print("License Number not found in the list")

        except Exception as e:
            print("Error : {}".format(e))

    def enter_license_professional(self, license_type, license_number, first_name, last_name, phone, email, address_line, city, state, business_name):
        try:
            self.obj_professional.select_license_type(license_type)
            self.obj_professional.enter_license_number(license_number)
            self.obj_professional.enter_first_name(first_name)
            self.obj_professional.enter_last_name(last_name)
            self.obj_professional.enter_phone(phone)
            self.obj_professional.enter_email(email)
            self.obj_professional.enter_business_name(business_name)
            self.obj_professional.enter_address_line(address_line)
            self.obj_professional.enter_city(city)
            self.obj_professional.enter_state(state)

        except Exception as e:
            print("Error : {}".format(e))
