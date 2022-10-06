from PageObjects.ACA_License_Professional import ACALicenseProfessional
from Views.ACA_Common_View import ACACommonView


class ACALicenseProfessionalView:

    def __init__(self, drv):
        # Create instance of the ACA License Professional Page Objects
        self.obj_driver = drv
        self.obj_aca_lp = ACALicenseProfessional(drv)
        self.obj_aca_common = ACACommonView(drv)

    def license_professional_look_up(self, license_type, license_number):
        try:
            self.obj_aca_lp.click_look_up()
            self.obj_aca_lp.select_license_type(license_type)
            self.obj_aca_lp.enter_license_number(license_number)
            self.obj_aca_lp.click_license_search()
            self.verify_license_professional_added()
        except Exception as e:
            print("Error : {}".format(e))

    def verify_license_professional_added(self):
        lp_added = self.obj_aca_lp.verify_license_professional_added()
        if lp_added == 1:
            print("License Professional Added successfully")
        else:
            print("License Professional not added successfully")
