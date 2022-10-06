from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ACADocumentsObject:

    # Page Objects Documents in ACA
    frm1 = (By.ID, "ACADialogFrame")
    btn_Add = (By.LINK_TEXT, "Add")
    file_dialog = (By.ID,"fileInput_divFileBrowser")
    btn_Continue_doc_upload = (By.ID, "ctl00_phPopup_btnFinish")
    cbo_Type = (By.XPATH, "//label[.='Type:']//ancestor::div[2]//select")
    txt_Description = (By.XPATH, "//label[.='Description:']//ancestor::div[2]//textarea")
    btn_Save = (By.LINK_TEXT, "Save")


    btn_add_document = (By.CSS_SELECTOR, "a.btnBrowser_html5.NotShowLoading")
    btn_add_another = (By.ID, "divFileBrowser")
    div_progress = (By.CSS_SELECTOR, "div.divProgressBar>font")


    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_document_add(self):
        self.obj_wrapper.click_button(self.btn_Add, "Add")

    def click_select_file(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.change_control_visibility(self.file_dialog)

    def wait_for_file_upload(self):
        self.obj_wrapper.object_exists(self.div_progress, "Progress")

    def click_continue(self):
        self.obj_wrapper.click_button(self.btn_Continue_doc_upload, "Continue")
        self.obj_wrapper.switch_to_default()

    def enter_file_name(self, file_name):
        self.obj_wrapper.key_press(self.file_dialog, file_name)

    def select_document_type(self, doc_type):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Type, "Type of document" ,doc_type)

    def enter_description(self, description):
        self.obj_wrapper.enter_text(self.txt_Description, "Description" , description)

    def click_save(self):
        self.obj_wrapper.click_button(self.btn_Save, "Save")