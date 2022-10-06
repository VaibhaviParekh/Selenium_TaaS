from AutoConfig.AutoConfigPageObjects.FeeSchedule import FeeScheduleObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Common import ClassicAdminCommonPageObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Home import ClassicAdminHomePageObjects
import time


class FeeScheduleView:

    def __init__(self, drv):
        # Create instance of the Fees Page Objects
        self.obj_driver = drv
        self.obj_fee = FeeScheduleObjects(drv)
        self.obj_common = ClassicAdminCommonPageObjects(drv)
        self.obj_home = ClassicAdminHomePageObjects(drv)

    RETURN_VALUE = 0

    # Select Fee Schedule from Menu
    def navigate_to_fee_schedule(self):
        try:
            self.obj_home.select_menu("Fee")
            self.obj_home.select_menu_option("Fee Schedule")
        except Exception as e:
            print("Error : {}".format(e))

    # Search for given fee schedule
    def search_fee_schedule(self, i, action, fee_schedule, version):
        try:
            time.sleep(5)
            self.obj_fee.enter_search_fee_schedule(fee_schedule)
            self.obj_fee.enter_search_version(version)
            self.obj_common.click_submit()

            rec_found = self.obj_fee.verify_fee_schedule_exists(fee_schedule, version)
            if rec_found == 1:
                self.select_fee_schedule(i, action, fee_schedule, version)
                self.RETURN_VALUE = 1
            else:
                no_rec = self.obj_common.no_record_found()
                if no_rec == 1:
                    print(str(i) + ", " + action + ", FAIL, " + fee_schedule + " unable to find")
                    self.obj_common.click_search()
                    self.RETURN_VALUE = 0

        except Exception as e:
            print("Error : {}".format(e))

    # Add new Fee Schedule
    def add_new_fee_schedule(self, i, fee_schedule, fee_schedule_alias, version, effective_date, comment, status, disable_date):
        try:
            time.sleep(3)
            self.obj_fee.click_add()
            self.obj_fee.enter_fee_schedule(fee_schedule)
            self.obj_fee.enter_fee_schedule_alias(fee_schedule_alias)
            self.obj_fee.enter_version(version)
            self.obj_fee.enter_effective_date(effective_date)
            self.obj_fee.enter_comment(comment)
            self.obj_fee.select_status(status)
            self.obj_fee.enter_disable_date(disable_date)
            self.obj_common.click_save()

            alert = self.obj_common.does_alert_exists()
            if alert == 1:
                error = self.obj_common.read_alert_text()
                print(str(i) + ", CREATE, FAIL, " + fee_schedule + ", Error:" + error)
                self.obj_common.handle_alert()
            else:
                print(str(i) + ", CREATE, PASS, " + fee_schedule + " added successfully.")

            self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Edit existing Fee Schedule
    def edit_fee_schedule(self, i, fee_schedule, fee_schedule_alias, version, effective_date, comment, status, disable_on ):
        try:
            self.search_fee_schedule(i, "UPDATE", fee_schedule, version)
            if self.RETURN_VALUE == 1:
                self.obj_fee.enter_fee_schedule_alias(fee_schedule_alias)
                self.obj_fee.enter_effective_date(effective_date)
                self.obj_fee.enter_comment(comment)
                self.obj_fee.select_status(status)
                self.obj_fee.enter_disable_date(disable_on)
                self.obj_common.click_save()

                alert = self.obj_common.does_alert_exists()
                if alert == 1:
                    error = self.obj_common.read_alert_text()
                    print(str(i) + ", UPDATE, FAIL, " + fee_schedule + ", Error:" + error)
                    self.obj_common.handle_alert()
                else:
                    print(str(i) + ", UPDATE, PASS, " + fee_schedule + " added successfully")

                self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Select the Fee schedule
    def select_fee_schedule(self, i, action, fee_schedule, version):
        try:
            exists = self.obj_fee.verify_fee_schedule_exists(fee_schedule, version)
            if exists == 1:
                self.obj_fee.select_fee_schedule(fee_schedule, version)
            else:
                print(i + ", " + action + ", FAIL, " + fee_schedule + " not found.")
                self.obj_common.click_search()
                self.RETURN_VALUE = 0

        except Exception as e:
            print("Error : {}".format(e))

    # Add a new version into existing fee schedule
    def add_new_version(self, i, fee_schedule, fee_schedule_alias, version, version_add, effective_date, comment, status, disable_on ):
        try:
            self.search_fee_schedule(i, "ADD NEW VERSION", fee_schedule, version)
            if self.RETURN_VALUE == 1:
                self.obj_fee.click_create_new_version()
                self.obj_fee.enter_fee_schedule_alias(fee_schedule_alias)
                self.obj_fee.enter_version(version_add)
                self.obj_fee.enter_effective_date(effective_date)
                self.obj_fee.enter_comment(comment)
                self.obj_fee.select_status(status)
                self.obj_fee.enter_disable_date(disable_on)
                self.obj_common.click_save()

                message = self.obj_common.does_alert_exists()
                if message == 1:
                    error = self.obj_common.read_alert_text()
                    self.obj_common.handle_alert()
                    print(str(i) + ", ADD NEW VERSION, FAIL, " + fee_schedule + ", Error:" + error)
                else:
                    print(str(i) + ", ADD NEW VERSION, PASS, " + fee_schedule + " added successfully")

            self.obj_common.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))