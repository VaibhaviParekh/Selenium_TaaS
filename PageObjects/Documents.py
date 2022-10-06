from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class DocumentObjects:

    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")
    btn_New = (By.ID, "add")
    cbo_Document_Group = (By.ID, "value(docGroup)")
    cbo_Document_Category = (By.ID, "value(type)")
    txt_Document_Name = (By.ID, "value(documentName)")
    txt_Document_Description = (By.ID, "value(documentDescription)")
    cbo_EDMS_Name = (By.ID, "value(source)")
    btn_Save = (By.ID, "saveRecords")
    btn_Add = (By.ID, "addOneRecord")
    btn_Cancel = (By.ID, "cancel")
    btn_Delete = (By.ID, "deleteRecord")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_new(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_New, "New")
        self.obj_wrapper.switch_to_default()

    def select_document_group(self, document_group):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Document_Group, "Document Group", document_group)
        self.obj_wrapper.switch_to_default()

    def select_document_category(self, document_category):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Document_Category, "Document Category", document_category)
        self.obj_wrapper.switch_to_default()

    def enter_document_name(self, document_name):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_Document_Name, "Document Name", document_name)
        self.obj_wrapper.switch_to_default()

    def enter_document_description(self, document_description):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_Document_Description, "Document Description", document_description)
        self.obj_wrapper.switch_to_default()

    def click_add(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Add, "Add")
        self.obj_wrapper.switch_to_default()

    def click_save(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Save, "Save")
        self.obj_wrapper.switch_to_default()

    def click_delete(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Delete, "Delete")
        self.obj_wrapper.switch_to_default()

    def click_cancel(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Cancel, "Cancel")
        self.obj_wrapper.switch_to_default()

    def verify_document_exists_in_list(self, document_name, document_category):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH,
                   "//table[@id='AccelaMainTable']//td[contains(.,'" + document_name + "')]//..//td[contains(.,'" + document_category + "')]")
        document_exists = self.obj_wrapper.object_exists(control, "Document in List")
        self.obj_wrapper.switch_to_default()
        if document_exists == 1:
            return True
        else:
            return False