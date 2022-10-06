from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Home import ClassicAdminHomePageObjects


class ClassicAdminHomeView:

    def __init__(self, drv):
        # Create instance of the Fees Page Objects
        self.obj_driver = drv
        self.obj_classic_home = ClassicAdminHomePageObjects(drv)

    # Navigate to Menu
    def select_menu_option(self, menu, menu_option):
        try:
            self.obj_classic_home.select_menu(menu)
            self.obj_classic_home.select_menu_option(menu_option)

        except Exception as e:
            print("Error : {}".format(e))

    # Logout from classic admin
    def logout_class_admin(self):
        try:
            self.obj_classic_home.click_logout()
        except Exception as e:
            print("Error : {}".format(e))

