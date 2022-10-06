from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class FeeScheduleObjects:

    # Page Objects related to Fee Schedule

    txt_Fee_Schedule = (By.ID, "id_txtFeeSchedule")
    txt_Fee_Schedule_Alias = (By.ID, "id_txtFeeScheduleAlias")
    txt_Version = (By.ID, "id_txtVersion")
    txt_Effective_Date = (By.ID, "id_txtEffectiveDate")
    rdo_Status_All = (By.ID, "id_txtRecStatus_All")
    rdo_Status_Enable = (By.ID, "id_txtRecStatus_A")
    rdo_Status_Disable = (By.ID, "id_txtRecStatus_I")
    txt_Comment = (By.ID, "id_txtComment")
    txt_Disable_Date = (By.ID, "id_txtDisableDate")
    btn_Add = (By.XPATH, "//img[@alt='Add New Fee Schedule']")
    btn_Create_New_Version = (By.XPATH, "//img[@alt='Create New Version']")

    txt_Search_Fee_Schedule = (By.ID, "txtFeeSchedule")
    txt_Search_Fee_Schedule_Alias = (By.ID, "txtFeeScheduleAlias")
    txt_Search_Version = (By.ID, "txtVersion")
    txt_Search_Effective_Date = (By.ID, "txtEffectiveDate")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def enter_fee_schedule(self, fee_schedule):
        self.obj_wrapper.enter_text(self.txt_Fee_Schedule, "Fee Schedule", fee_schedule)

    def enter_fee_schedule_alias(self, fee_schedule_alias):
        self.obj_wrapper.enter_text(self.txt_Fee_Schedule_Alias, "Fee Schedule Alias", fee_schedule_alias)

    def enter_version(self, version):
        self.obj_wrapper.enter_text(self.txt_Version, "Version", version)

    def enter_effective_date(self, effective_date):
        self.obj_wrapper.enter_text(self.txt_Effective_Date, "Effective Date", effective_date)

    def select_status(self, status):
        if status == "All":
            self.obj_wrapper.click_button(self.rdo_Status_All, "Radio All")
        elif status == "Enabled":
            self.obj_wrapper.click_button(self.rdo_Status_Enable, "Enabled")
        elif status == "Disabled":
            self.obj_wrapper.click_button(self.rdo_Status_Disable, "Disabled")

    def enter_comment(self, comment):
        self.obj_wrapper.enter_text(self.txt_Comment, "Comment", comment)

    def enter_disable_date(self, disable_date):
        self.obj_wrapper.enter_text(self.txt_Disable_Date, "Disable Date", disable_date)

    def click_add(self):
        self.obj_wrapper.click_button(self.btn_Add, "Add")

    def click_create_new_version(self):
        self.obj_wrapper.click_button(self.btn_Create_New_Version, "Create New Version")

    def verify_fee_schedule_exists(self, fee_schedule, version):
        control = (By.XPATH, "//table[@summary='Fee Schedule']//td[contains(.,'" + fee_schedule + "')]"
                                            "//ancestor::tr[1]//td[contains(.,'" + str(version) + "')]//ancestor::tr[1]//img")
        exists = self.obj_wrapper.object_exists(control, "Fee Schedule Control")
        if exists == 1:
            return True
        else:
            return False

    def verify_fee_schedule_added(self):
        success = self.obj_wrapper.object_exists(self.btn_Create_New_Version, "Fee Added")
        if success == 1:
            return True
        else:
            return False

    def select_fee_schedule(self, fee_schedule, version):
        control = (By.XPATH, "//table[@summary='Fee Schedule']//td[contains(.,'" + fee_schedule + "')]"
                                                   "//ancestor::tr[1]//td[contains(.,'" + str(version) + "')]//ancestor::tr[1]//img")
        self.obj_wrapper.click_button(control, "Fee Schedule Control")

    def enter_search_fee_schedule(self, fee_schedule):
        self.obj_wrapper.enter_text(self.txt_Search_Fee_Schedule, "Fee Schedule", fee_schedule)

    def enter_search_fee_schedule_alias(self, fee_schedule_alias):
        self.obj_wrapper.enter_text(self.txt_Search_Fee_Schedule_Alias, "Fee Schedule Alias", fee_schedule_alias)

    def enter_search_version(self, version):
        self.obj_wrapper.enter_text(self.txt_Search_Version, "Version", version)

    def enter_search_effective_date(self, effective_date):
        self.obj_wrapper.enter_text(self.txt_Search_Effective_Date, "Effective Date", effective_date)