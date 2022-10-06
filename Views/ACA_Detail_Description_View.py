from PageObjects.ACA_Detail_Description import ACAApplicationDetailsObject


class ACADetailDescriptionView:

    def __init__(self, drv):
        # Create instance of the ACA Detail Description Page Objects
        self.obj_driver = drv
        self.obj_app_detail = ACAApplicationDetailsObject(drv)

    def enter_detail_description(self, application_name, detail_description, business_name):
        try:
            self.obj_app_detail.enter_application_name(application_name)
            self.obj_app_detail.enter_detailed_description(detail_description)
            self.obj_app_detail.enter_business_name(business_name)

        except Exception as e:
            print("Error : {}".format(e))