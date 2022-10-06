# from PageObjects.LoginPage import LoginPageObjects
# from PageObjects.LandingPage import LandingPageObjects
from PageObjects.Record_Search import RecordSearchPageObjects


class RecordSearchView:

    def __init__(self, drv):
        # Create instance of the Login Page Objects
        self.obj_driver = drv
        # self.objLoginPage = LoginPageObjects(drv)
        # self.objLandingPage = LandingPageObjects(drv)
        self.obj_record_page = RecordSearchPageObjects(drv)

    def search_record_by_id(self, rec_id):
        try:
            self.obj_record_page.click_search()
            self.obj_record_page.enter_record_no(rec_id)
            self.obj_record_page.click_submit()
            record_found = self.obj_record_page.verify_record_found()
            if record_found == 1:
                self.obj_record_page.click_record_row(rec_id)

                record_open = self.obj_record_page.verify_record_open()
                if record_open == 1:
                    print("Record searched and selected.")
                else:
                    print("Unable to select the record.")

            else:
                print("Record not found")

        except Exception as e:
            print("Error : {}".format(e))