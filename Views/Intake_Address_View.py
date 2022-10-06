from PageObjects.Intake_Address import IntakeAddressObjects


class IntakeAddressView:

    def __init__(self, drv):
        # Create instance of the Address Page Objects
        self.obj_driver = drv
        self.obj_address = IntakeAddressObjects(drv)

    def address_search(self, street_num, street_name, street_type, direction, city, state, zip):
        try:
            self.obj_address.enter_street_number(street_num)
            self.obj_address.enter_street_name(street_name)
            self.obj_address.select_street_type(street_type)
            self.obj_address.select_direction(direction)
            self.obj_address.enter_city(city)
            self.obj_address.enter_state(state)
            self.obj_address.enter_zip(zip)
            self.obj_address.click_address_search()
        except Exception as e:
            print("Error : {}".format(e))

    def verify_address_owner_parcel_added(self, verify_owner_added, verify_parcel_added):
        try:
            add_found = self.obj_address.verify_address_found()
            if add_found == 1:
                print("Address found and added successfully")
            else:
                print("Address not found")

            if verify_owner_added == "yes":
                owner_found = self.obj_address.verify_owner_found()
                if owner_found == 1:
                    print("Owner added successfully")
                else:
                    print("Owner not added successfully")

            if verify_parcel_added == "yes":
                parcel_found = self.obj_address.verify_parcel_found()
                if parcel_found == 1:
                    print("Parcel added successfully")
                else:
                    print("Parcel not added successfully")

        except Exception as e:
            print("Error : {}".format(e))

