from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class IntakeDocumentObjects:
    # Document Upload on new record
    btn_add = (By.ID, "Add")

    def __init__(self, drv):
        # Create instance of Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_add_document(self):
        self.obj_wrapper.click_button(self.btn_add, "Add Document")

    def enter_document_name(self, document_name, i):
        self.obj_wrapper.switch_to_window("New Record By Single")
        control = (By.ID, "value(documentName" + i + ")")
        self.obj_wrapper.enter_text(control, "Document Name", document_name)

    def select_document_group(self, document_group, i):
        control = (By.ID, "value(docGroup" + i + ")")
        self.obj_wrapper.select_value_from_dropdown(control, "Document Group", document_group)

    def select_document_category(self, document_category, i):
        control = (By.ID, "value(docCategory" + i + ")")
        self.obj_wrapper.select_value_from_dropdown(control, "Document Category", document_category)

    def enter_document_description(self, document_description, i):
        control = (By.ID, "value(docDescription" + i + ")")
        self.obj_wrapper.enter_text(control, "Document Description", document_description)