from PageObjects.ACA_Address import ACAAddressObject
from Views.ACA_Common_View import ACACommonView


class ACAAddressView:

    def __init__(self, drv):
        # Create instance of the ACA Address Page Objects
        self.obj_driver = drv
        self.obj_aca_address = ACAAddressObject(drv)
        self.obj_aca_common = ACACommonView(drv)

    def aca_search_address(self, street_number, street_name, street_type, street_dir, zip):
        try:
            self.obj_aca_address.enter_street_number(street_number)
            self.obj_aca_address.enter_street_name(street_name)
            self.obj_aca_address.select_street_type(street_type)
            self.obj_aca_address.select_direction(street_dir)
            self.obj_aca_address.enter_zip(zip)
            self.obj_aca_address.click_search()
            self.obj_aca_common.aca_wait_for_spinner()
            self.obj_aca_common.aca_continue_application()

        except Exception as e:
            print("Error : {}".format(e))