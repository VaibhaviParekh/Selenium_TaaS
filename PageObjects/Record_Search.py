from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class RecordSearchPageObjects:
    frm1 = (By.ID, "iframe-page-container")
    frm2 = (By.ID, "capList")
    btnSearch = (By.ID, "search")
    txtRecordID = (By.XPATH, "//table[@id='elementTableContainer(capModel*altID)']//input[@id='value(capModel*altID)']")
    btnSubmit = (By.ID, "acsubmit")
    lnkRecord = (By.ID, "linkrow1")
    lblRecOpen = (By.CSS_SELECTOR, "div.r-id.text-ellipsis")

    def __init__(self, drv):
        # Create instance of Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_search(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.click_button(self.btnSearch, "Search")
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    def enter_record_no(self, rec_no):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        self.obj_wrapper.enter_text(self.txtRecordID, "Record #", rec_no)

    def click_submit(self):
        self.obj_wrapper.click_button(self.btnSubmit, "Submit")
        self.obj_wrapper.switch_to_default()
        self.obj_wrapper.switch_to_default()

    def verify_record_found(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.switch_to_frame(self.frm2, "")
        if self.obj_wrapper.object_exists(self.lnkRecord, "Record"):
            return True
        else:
            return False

    def click_record_row(self, record):
        if self.obj_wrapper.check_page_loaded():
            self.obj_wrapper.force_click(self.lnkRecord, "Record")
            self.obj_wrapper.switch_to_default()
            self.obj_wrapper.switch_to_default()

    def verify_record_open(self):
        if self.obj_wrapper.check_page_loaded():
            if self.obj_wrapper.object_exists(self.lblRecOpen, "Record Page"):
                return True
            else:
                return False