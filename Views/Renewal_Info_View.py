from PageObjects.Renewal_Info import RenewalInfoObject


class RenewalInfoView:

    # Create an instance of class
    def __init__(self, drv):
        self.obj_driver=drv
        self.obj_renewal_info = RenewalInfoObject(drv)

    def update_renewal_info(self, renewal_status, renewal_date):
        try:
            self.obj_renewal_info.select_expiration_status(renewal_status)
            self.obj_renewal_info.enter_expiration_date(renewal_date)
            self.obj_renewal_info.save_renewal_info()
            success = self.obj_renewal_info.verify_renewal_info_updated()
            if success == 1:
                print("Renewal Information updated successfully.")
            else:
                print("Renewal Information not updated successfully")

        except Exception as e:
            print("Error : {}".format(e))

    def verify_renewal_info(self, renewal_status, renewal_date):
        try:
            if renewal_status != "":
                status = self.obj_renewal_info.verify_expiration_status_value(renewal_status)
                if status == 1:
                    print("Renewal Information status successfully verified to: " + renewal_status)
                else:
                    print("Renewal Information status not successfully verified to: " + renewal_status)

            if renewal_date != "":
                date = self.obj_renewal_info.verify_expiration_date_value(renewal_date)
                if date == 1:
                    print("Renewal Information date successfully verified to: " + renewal_date)
                else:
                    print("Renewal Information date not successfully verified to: " + renewal_date)

        except Exception as e:
            print("Error : {}".format(e))