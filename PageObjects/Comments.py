from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers

class CommentObjects:

    # All page objects from Comment Portlet
    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")

    btn_New = (By.ID, "new")
    btn_submit = (By.ID, "addSave")
    btn_reset = (By.ID, "accelareset")
    btn_cancel = (By.ID, "cancel")
    chk_Apply_to_Inspections = (By.ID, "value(displayOnInsp)")
    txtarea_Comment = (By.ID, "value(text)")
    lbl_No_Record = (By.CLASS_NAME, "portlet-msg-alert")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    # Verify no comments are added.
    def verify_no_comments(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        no_record = self.obj_wrapper.is_visible(self.lbl_No_Record, "No Record")
        self.obj_wrapper.switch_to_default()
        if no_record == 1:
            return True
        else:
            return False

    # Verify comment value
    def verify_comment(self, comment):
        self.obj_wrapper.switch_to_frame(self.frm1,"")
        comment_control = (By.XPATH, "//a[contains(.,'" + comment + "')]")
        comment_value = self.obj_wrapper.object_exists(comment_control, "Comment")
        self.obj_wrapper.switch_to_default()
        if comment_value == 1:
            return True
        else:
            return False

    # Verify Comment Date
    def verify_comment_date(self, comment, date):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        comment_control = (By.XPATH,"//a[contains(.,'" + comment + "')]//ancestor::tr[1]//td[contains(.,'" + date + "')]")
        comment_date_value = self.obj_wrapper.object_exists(comment_control, "Comment with Date")
        self.obj_wrapper.switch_to_default()
        if comment_date_value == 1:
            return True
        else:
            return False
