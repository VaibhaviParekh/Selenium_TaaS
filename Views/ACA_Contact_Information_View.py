from PageObjects.ACA_Contact_information import ACAContactInformationObject
from Views.ACA_Common_View import ACACommonView


class ACAContactInformationView:

    def __init__(self, drv):
        # Create instance of the ACA Contact Information Page Objects
        # Contact, Applicant select from account
        self.obj_driver = drv
        self.obj_aca_contact = ACAContactInformationObject(drv)
        self.obj_aca_common = ACACommonView(drv)

    def select_applicant_from_account(self):
        try:
            self.obj_aca_contact.click_select_from_account_applicant()
            self.obj_aca_common.aca_wait_for_spinner()
            self.verify_applicant_added()
        except Exception as e:
            print("Error : {}".format(e))

    # Select applicant from account and verify applicant is added
    def applicant_select_from_account_with_address_or_contact_type(self, address_type, contact_type):
        try:
            self.obj_aca_contact.click_select_from_account_applicant()
            self.obj_aca_common.aca_wait_for_spinner()

            if address_type != "":
                self.obj_aca_contact.select_address_type(address_type)
                self.obj_aca_contact.click_contact_type_continue()
                self.obj_aca_common.aca_wait_for_spinner()

            if contact_type != "":
                self.obj_aca_contact.select_contact_type(contact_type)
                self.obj_aca_contact.click_continue()
                self.obj_aca_common.aca_wait_for_spinner()

        except Exception as e:
            print("Error : {}".format(e))

    def verify_applicant_added(self):
        app_add = self.obj_aca_contact.verify_applicant_added()
        if app_add == 1:
            print("Applicant Added Successfully")
        else:
            print("Applicant not added successfully")

    def verify_contact_added(self):
        con_add = self.obj_aca_contact.verify_contact_added()
        if con_add == 1:
            print("Contact Added Successfully")
        else:
            print("Contact not added successfully")

    def verify_contact_list_added(self):
        con_add = self.obj_aca_contact.verify_contact_list_added()
        if con_add == 1:
            print("Contact Added Successfully")
        else:
            print("Contact not added successfully")




