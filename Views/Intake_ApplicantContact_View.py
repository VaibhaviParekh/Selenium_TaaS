from PageObjects.Intake_Applicant_Contact import IntakeApplicantContactObjects
from PageObjects.Intake_Contact_Search import IntakeContactSearchObjects
import time

class IntakeApplicantContactView:

    def __init__(self, drv):
        # Create instance of the Applicant Page Objects
        self.obj_driver = drv
        self.obj_contact = IntakeApplicantContactObjects(drv)
        self.obj_search = IntakeContactSearchObjects(drv)

    # Search and add the applicant
    def search_applicant(self, firstname, lastname, email):
        try:
            self.obj_contact.click_search_applicant()
            self.obj_search.enter_firstname_search(firstname)
            self.obj_search.enter_lastname_search(lastname)
            self.obj_search.click_submit_search()
            time.sleep(5)

            exists = self.obj_search.verify_contact_in_list(firstname, lastname)
            if exists == 1:
                time.sleep(5)
                self.obj_search.select_contact(firstname, lastname)
                added = self.obj_contact.verify_applicant_added()
                if added == 1:
                    print("Applicant added successfully")
                else:
                    print("Applicant not added successfully")
            else:
                print("Unable to find applicant")

        except Exception as e:
            print("Error : {}".format(e))

    # Enter the applicant details on new record page
    def enter_applicant_details(self, firstname, lastname, homephone, businessphone, mobilephone, email):
        try:
            self.obj_contact.enter_app_firstname(firstname)
            self.obj_contact.enter_app_lastname(lastname)
            self.obj_contact.enter_app_home_phone(homephone)
            self.obj_contact.enter_app_business_phone(businessphone)
            self.obj_contact.enter_app_mobile_phone(mobilephone)
            self.obj_contact.enter_app_email(email)

        except Exception as e:
            print("Error : {}".format(e))

    # This action can be used to search the complaint or Facility Owner
    def search_contact(self, firstname, lastname):
        try:
            self.obj_contact.click_search_contact()
            self.obj_search.enter_firstname_search(firstname)
            self.obj_search.enter_lastname_search(lastname)
            self.obj_search.click_submit_search()

            exists = self.obj_search.verify_contact_in_list(firstname, lastname)
            if exists == 1:
                self.obj_search.select_contact(firstname, lastname)
                added = self.obj_contact.verify_contact_added()
                if added == 1:
                    print("Contact added successfully")
                else:
                    print("Contact not added successfully")
            else:
                print("Unable to find Contact")

        except Exception as e:
            print("Error : {}".format(e))

    # Search the contact and update the contact type
    def search_contact_and_with_contact_type(self, firstname, lastname, contact_type, row_index='1'):
        self.search_contact(firstname, lastname)
        self.obj_contact.update_contact_type(firstname, lastname, row_index, contact_type)
