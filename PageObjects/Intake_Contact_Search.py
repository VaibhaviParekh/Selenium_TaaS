from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By

class IntakeContactSearchObjects:

    # Objects on applicant search page
    txt_firstname_search = (By.ID, "value(firstName)")
    txt_lastname_search = (By.ID, "value(lastName)")
    txt_email_search = (By.ID, "value(email)")
    btn_submit_search = (By.ID, "acsubmit")
    btn_select = (By.ID, "doSelect4Multiple")
    btn_search = (By.ID, "search")
    lbl_contact_success = (By.ID, "errorMsgPanel")

    def __init__(self, drv):
        # Create instance of Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def enter_firstname_search(self, firstname):
        self.obj_wrapper.switch_to_window("Contact Search")
        self.obj_wrapper.enter_text(self.txt_firstname_search, "First Name", firstname)

    def enter_lastname_search(self, lastname):
        self.obj_wrapper.enter_text(self.txt_lastname_search, "Last Name", lastname)

    def click_submit_search(self):
        self.obj_wrapper.click_button(self.btn_submit_search, "Submit Search")
        self.obj_wrapper.switch_to_window("New Record By Single")

    # Verify contact or applicant in the list
    def verify_contact_in_list(self, firstname, lastname):
        self.obj_wrapper.switch_to_window("Contact List")
        control = (By.XPATH, "//table[@id='AccelaMainTable']//td[contains(.,'" + firstname + "')]//..//td[contains(.,'" + lastname + "')]")
        app_exists = self.obj_wrapper.object_exists(control, "Contact in List")
        if app_exists == 1:
            return True
        else:
            return False

    def select_contact(self, firstname, lastname):
        control = (By.XPATH, "//table[@id='AccelaMainTable']//td[contains(.,'" + firstname + "')]//..//td[contains(.,'" + lastname +"')]//..//input")
        self.obj_wrapper.click_button(control, "Contact from List")

    def click_select(self):
        self.obj_wrapper.click_button(self.btn_select, "Select")

    def click_search(self):
        self.obj_wrapper.click_button(self.btn_search, "Search")
