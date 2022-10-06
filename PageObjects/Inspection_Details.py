from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By

class InspectionDetailsObjects():

    # Objects on Inspection Checklist, Inspection Details
    frm1 = (By.XPATH, "//iframe[@data-entity='inspection']")

    # Links on the left side to select for further inspection options
    lnk_Inspection_Detail = (By.PARTIAL_LINK_TEXT, "Inspection Detail")
    lnk_Checklist = (By.XPATH, "//li[@id='Guide Sheets']")
    lnk_Conditions = (By.PARTIAL_LINK_TEXT, "Conditions")
    lnk_Documents = (By.PARTIAL_LINK_TEXT, "Documents")
    lnk_Related_Inspections = (By.PARTIAL_LINK_TEXT, "Related Inspections")
    lnk_Random_Audit_History = (By.PARTIAL_LINK_TEXT, "Random Audit History")
    cbo_group = (By.ID, "value(rGuideSheetGroupCode)")
    btn_Search_Checklist = (By.ID, "addFromRef")
    btn_Save = (By.ID, "editSave")
    btn_Cancel = (By.ID, "cancel")
    btn_Submit = (By.ID, "addFromRefSave")
    lbl_message = (By.ID, "err_msg")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_checklist_menu(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.lnk_Checklist, "Checklist")
        self.obj_wrapper.switch_to_default()

    def click_inspection_detail_menu(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.lnk_Inspection_Detail, "Inspection Detail")
        self.obj_wrapper.switch_to_default()

    def click_condition_menu(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.lnk_Conditions, "Conditions")
        self.obj_wrapper.switch_to_default()

    def click_documents_menu(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.lnk_Documents, "Documents")
        self.obj_wrapper.switch_to_default()

    def click_search_checklist(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Search_Checklist, "Search")
        self.obj_wrapper.switch_to_default()

    def click_submit(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Submit, "Submit")
        self.obj_wrapper.switch_to_default()

    def click_cancel(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Cancel, "Cancel")
        self.obj_wrapper.switch_to_default()

    def click_save(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Save, "Save")
        self.obj_wrapper.switch_to_default()

    def select_checklist_group(self, group):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_group, "Group", group)
        self.obj_wrapper.switch_to_default()

    def verify_checklist_item_exists(self, checklist):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//a[.='" + checklist + "']")
        exists = self.obj_wrapper.object_exists(control, "Checklist item")
        self.obj_wrapper.switch_to_default()
        if exists == 1:
            return True
        else:
            return False

    def check_checklist_item_checkbox(self, checklist):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//table[@id='AccelaMainTable']//td[contains(.,'" + checklist + "')]//..//input")
        self.obj_wrapper.click_checkbox(control)
        self.obj_wrapper.switch_to_default()

    def click_checklist_item_link(self, checklist):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//a[.='" + checklist + "']")
        self.obj_wrapper.click_button(control, "Checklist Item Link")
        self.obj_wrapper.switch_to_default()

    def verify_checklist_sub_item_exists(self, checklist_sub_item):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//table[@id='displayBody']//div[contains(.,'" + checklist_sub_item + "')]")
        self.obj_wrapper.switch_to_default()

    def select_checklist_sub_item_status(self,checklist_sub_item, status):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//table[@id='displayBody']//div[contains(.,'"+ checklist_sub_item +"')]//ancestor::tr[2]//select")
        self.obj_wrapper.select_value_from_dropdown(control, "Checklist status select", status)
        self.obj_wrapper.switch_to_default()

    def verify_success_message(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        message = self.obj_wrapper.get_text_for_webelement(self.lbl_message, "Success")
        self.obj_wrapper.switch_to_default()
        if message == "Updated successfully.":
            return True
        else:
            return False