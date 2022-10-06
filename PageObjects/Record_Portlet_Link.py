from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class RecordPortletObjects:
    # After submission of record. Page objects from Record Portlet
    frm1 = (By.CSS_SELECTOR, "div.angular-header>iframe#iframe-page-container")
    Summary = (By.CSS_SELECTOR, "li#CapTabSummary>a")
    Record = (By.CSS_SELECTOR, "li#CapDetail>a")
    Workflow = (By.ID, "Workflow")
    Status = (By.CSS_SELECTOR, "li#Status>a")
    Communication = (By.CSS_SELECTOR, "li#Communications>a")
    Comments = (By.CSS_SELECTOR, "li#Comments>a")
    Renewal_Info = (By.CSS_SELECTOR, "li#RenewalInfo>a")
    Fees = (By.CSS_SELECTOR, "li#Fees>a")
    Inspection = (By.CSS_SELECTOR, "li#Inspections>a")
    Payment = (By.CSS_SELECTOR, "li#Payments>a")
    Documents = (By.CSS_SELECTOR, "li#Document>a")

    def __init__(self, drv):
        # Create instance of Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_record_portlet(self, portlet):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        ele = None
        if portlet == "Workflow":
            ele = self.Workflow
        elif portlet == "Summary":
            ele = self.Summary
        elif portlet == "Record":
            ele = self.Record
        elif portlet == "Status":
            ele = self.Status
        elif portlet == "Communication":
            ele = self.Communication
        elif portlet == "Comments":
            ele = self.Comments
        elif portlet == "Renewal Info":
            ele = self.Renewal_Info
        elif portlet == "Fees":
            ele = self.Fees
        elif portlet == "Inspection":
            ele = self.Inspection
        elif portlet == "Payment":
            ele = self.Payment
        elif portlet == "Document":
            ele = self.Documents

        if self.obj_wrapper.object_exists(ele, portlet):
            self.obj_wrapper.click_button(ele, portlet)
        self.obj_wrapper.switch_to_default()