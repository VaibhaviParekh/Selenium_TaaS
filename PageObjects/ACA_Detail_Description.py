from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ACAApplicationDetailsObject:

    # Page Objects Application Details in ACA
    txt_Detailed_Description = (By.XPATH, "//label[contains(.,'Detailed Description:')]/ancestor::tr[2]//textarea")
    txt_Application_Name = (By.XPATH, "//label[contains(.,'Application Name')]/ancestor::tr[2]//input")
    txt_Business_Name = (By.XPATH, "//label[contains(.,'Business Name')]/ancestor::tr[2]//input")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def enter_detailed_description(self, detailed_description):
        self.obj_wrapper.enter_text(self.txt_Detailed_Description, "Detailed Description", detailed_description)

    def enter_application_name(self, application_name):
        self.obj_wrapper.enter_text(self.txt_Application_Name, "Application Name", application_name)

    def enter_business_name(self, business_name):
        self.obj_wrapper.enter_text(self.txt_Business_Name, "Business Name", business_name)