from PageObjects.Addtl_Info import AddtlInfoObjects


class AddtlInfoView:

    def __init__(self, drv):
        # Create instance of the Login Page Objects
        self.obj_driver = drv
        self.obj_addtl_info_page = AddtlInfoObjects(drv)

    # Enter Additional Information Detail
    def fill_addtl_info_detail(self, application_job_value, number_of_buildings, housing_unit, consruction_type, public_owned, addtl_info_date):
        try:
            self.obj_addtl_info_page.enter_application_job_value(application_job_value)
            self.obj_addtl_info_page.enter_number_of_buildings(number_of_buildings)
            self.obj_addtl_info_page.enter_housing_unit(housing_unit)
            self.obj_addtl_info_page.select_construction_type(consruction_type)
            self.obj_addtl_info_page.select_public_owned(public_owned)
            self.obj_addtl_info_page.save_addtl_info_data()
        except Exception as e:
            print("Error : {}".format(e))