from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ACAReviewPageObjects:

    chk_review_I_agree = (By.ID,"ctl00_PlaceHolderMain_capReviewCertification1_termReviewAccept")
    lbl_review_date = (By.ID, "ctl00_PlaceHolderMain_capReviewCertification1_lblDateValue")
    btn_edit_document = (By.XPATH,"//td[.='Documents']//..//td[contains(.,'Edit')]//a")
    btn_edit_attachment = (By.XPATH, "//td[.='Attachment]//..//td[contains(.,'Edit')]//a")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_review_I_agree(self):
        self.obj_wrapper.click_checkbox(self.chk_review_I_agree)

    def click_edit_document(self):
        self.obj_wrapper.click_button(self.btn_edit_document)

    def click_edit_attachment(self):
        self.obj_wrapper.click_button(self.btn_edit_attachment)

    def verify_review_date(self, date):
        review_date = self.obj_wrapper.get_text_for_webelement(self.lbl_review_date, "Review Date")
        if review_date == date:
            print("Review Date verified successfully")
        else:
            print("Review Date not verified")