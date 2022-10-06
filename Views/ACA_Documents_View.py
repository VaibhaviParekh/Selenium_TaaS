from PageObjects.ACA_Document import ACADocumentsObject
from Views.ACA_Common_View import ACACommonView
import time
from Common.Config import Config


class ACADocumentView:

    def __init__(self, drv):
        # Create instance of the ACA Document Upload Page Objects
        self.obj_driver = drv
        self.obj_aca_doc = ACADocumentsObject(drv)
        self.obj_common = ACACommonView(drv)

    def aca_document_upload(self, document_name, document_type, document_description):
        # Any data file that we want to update will be in any folder.
        # From data file we just pass the file name ex. TestDoc.txt. So we concate the file name with file path to upload file
        datafile = Config.document_path + document_name

        self.obj_aca_doc.click_document_add()
        self.obj_aca_doc.click_select_file()
        self.obj_aca_doc.enter_file_name(datafile)
        # Once the document is uploaded the process on clicking on Continue is too fast. Need to slow down
        time.sleep(3)
        self.obj_aca_doc.click_continue()
        self.obj_aca_doc.select_document_type(document_type)
        self.obj_common.aca_wait_for_spinner()
        self.obj_aca_doc.enter_description(document_description)
        self.obj_aca_doc.click_save()
        self.obj_common.aca_wait_for_spinner()