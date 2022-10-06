from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class IntakeRecordDetailObjects:

    # Record Details option on New Record
    txt_application_name = (By.ID, "value(capModel*specialText)")
    txt_detailed_description = (By.ID, "value(capWorkDescriptionModel*description)")

    def __init__(self, drv):
        # Create instance of Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def enter_application_name(self, application_name):
        self.obj_wrapper.switch_to_window("New Record By Single")
        self.obj_wrapper.enter_text(self.txt_application_name, "Application Name", application_name)

    def enter_description(self, description):
        self.obj_wrapper.enter_text(self.txt_detailed_description, "Detailed Description", description)