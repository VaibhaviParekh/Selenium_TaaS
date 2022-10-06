from PageObjects.ACA_Review_Page import ACAReviewPageObjects
from PageObjects.ACA_Common import ACACommonObject

class ACAReviewView:

    def __init__(self, drv):
        # Create instance of the ACA Login Page Objects
        self.obj_driver = drv
        self.obj_aca_review = ACAReviewPageObjects(drv)
        self.obj_common = ACACommonObject(drv)

    def review_I_agree(self):
        self.obj_aca_review.chk_review_I_agree()

    def edit_document(self):
        self.obj_aca_review.click_edit_document()

    def edit_attachment(self):
        self.obj_aca_review.click_edit_attachment()

    def verify_review_date(self, date):
        self.obj_aca_review.verify_review_date(date)
