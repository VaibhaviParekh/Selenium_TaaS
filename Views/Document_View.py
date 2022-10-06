from PageObjects.Documents import DocumentObjects
from Views.Upload_File_View import DocumentUploadView


class DocumentView:

    def __init__(self, drv):
        # Create instance of the Communication Page Objects
        self.obj_driver = drv
        self.obj_documents = DocumentObjects(drv)
        self.obj_upload_file = DocumentUploadView(drv)

    def aa_upload_documents(self, document_name, document_group, document_category, document_description):
        try:
            self.obj_documents.click_new()
            self.obj_documents.select_document_group(document_group)
            self.obj_documents.select_document_category(document_category)
            self.obj_documents.enter_document_name(document_category)
            self.obj_documents.enter_document_description(document_description)
            self.obj_documents.click_add()
            self.obj_upload_file.upload_document_file(document_name, "record")
            self.obj_documents.click_save()
            document_added = self.obj_documents.verify_document_exists_in_list(document_name, document_category)
            if document_added == 1:
                print("Document added successfully")
            else:
                print("Document not added successfully")

        except Exception as e:
            print("Error : {}".format(e))

    def verify_document_in_list(self, document_name, document_category):
        try:
            document_added = self.obj_documents.verify_document_exists_in_list(document_name, document_category)
            if document_added == 1:
                print("Document " + document_name + " found in the list")
            else:
                print("Document " + document_name + " not found in the list")

        except Exception as e:
            print("Error : {}".format(e))