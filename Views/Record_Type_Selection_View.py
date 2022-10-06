import time

from PageObjects.Landing_Page import LandingPageObjects
from PageObjects.Record_Type_Selection import RecordTypeSelectionPageObjects
from Views.Landing_View import LandingView


class RecordTypeSelectionView:

    def __init__(self, drv):
        # Create instance of the Record Type Selectiion Page Objects
        self.obj_driver = drv
        self.obj_record_page = RecordTypeSelectionPageObjects(drv)

    def new_record_create(self, record_type):
        try:
            self.obj_record_page.select_record_type(record_type)
            self.obj_record_page.click_create()

        except Exception as e:
            print("Error : {}".format(e))