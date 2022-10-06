from PageObjects.Status import StatusObjects
import time

class StatusView:

    def __init__(self, drv):
        # Create an instance of the class
        self.obj_driver = drv
        self.obj_status = StatusObjects(drv)

    def update_status(self, status, date, department='current', user='current'):
        try:
            self.obj_status.enter_status_date(date)
            self.obj_status.select_status(status)

            if department.lower() == 'current':
                self.obj_status.click_current_department()
            else:
                self.obj_status.select_department_value(department)

            if user.lower() == 'current':
                self.obj_status.click_current_user()
            else:
                time.sleep(2)
                self.obj_status.select_user_value(user)
            self.obj_status.click_save()

            if self.obj_status.verify_status_updated():
                print("Status successfully updated")
            else:
                print("Status not successfully updated")

        except Exception as e:
            print("Error : {}".format(e))

    def verify_status_values(self, status, date):
        try:
            if status != "":
                if self.obj_status.verify_status_value(status):
                    print("Status successfully verified to: " + status)
                else:
                    print("Status not successfully verified to: " + status)

            if date != "":
                if self.obj_status.verify_date_value(date):
                    print("Status date successfully verified to: " + date)
                else:
                    print("Status date not successfully verified to: " + date)

        except Exception as e:
            print("Error : {}".format(e))