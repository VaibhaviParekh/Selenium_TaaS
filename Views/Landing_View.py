from PageObjects.Landing_Page import LandingPageObjects


class LandingView:

    def __init__(self, drv):
        # Create instance of the Login Page Objects
        self.obj_driver = drv
        self.obj_landing_page = LandingPageObjects(drv)

    def open_page(self):
        self.obj_landing_page.click_menu()
        self.obj_landing_page.click_all_pages()
        self.obj_landing_page.select_menu_option("Record")

    def create_new_record(self):
        self.obj_landing_page.click_menu()
        self.obj_landing_page.click_create_record()
