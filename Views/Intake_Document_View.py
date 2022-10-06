from PageObjects.Intake_Documents import IntakeDocumentObjects
from Views.Upload_File_View import DocumentUploadView


class IntakeDocumentsView:

    def __init__(self, drv):
        # Create instance of the Comments Page Objects
        self.obj_driver = drv
        self.obj_documents = IntakeDocumentObjects(drv)
        self.obj_upload_file = DocumentUploadView(drv)

    def new_record_upload_document(self, document_name, document_group, document_category, document_description, i):
        try:
            self.obj_documents.click_add_document()
            self.obj_upload_file.upload_document_file(document_name, "New Record")
            self.obj_documents.enter_document_name(document_category, i)
            self.obj_documents.select_document_group(document_group, i)
            self.obj_documents.select_document_category(document_category, i)
            self.obj_documents.enter_document_description(document_description, i)

        except Exception as e:
            print("Error : {}".format(e))


