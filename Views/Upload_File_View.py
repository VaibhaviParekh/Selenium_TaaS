from PageObjects.Upload_File import DocumentUploadObjects
from Common.Config import Config

class DocumentUploadView:

    def __init__(self, drv):
        # Create instance of the Upload File Page Objects
        self.obj_driver = drv
        self.obj_upload_file = DocumentUploadObjects(drv)

    def upload_document_file(self, file_name, section):
        try:
            # Any data file that we want to update will be in any folder.
            # From data file we just pass the file name ex. TestDoc.txt. So we concate the file name with file path to upload file
            datafile = Config.document_path + file_name
            self.obj_upload_file.click_select_file(section)
            self.obj_upload_file.enter_file_name(datafile)
            self.obj_upload_file.click_continue(section)

        except Exception as e:
            print("Error : {}".format(e))
