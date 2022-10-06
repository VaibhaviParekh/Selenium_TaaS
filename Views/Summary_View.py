from PageObjects.Summary import SummaryObjects
from PageObjects.Record_Portlet_Link import RecordPortletObjects


class SummaryView:

    def __init__(self,drv):

        # Initialize the instance of a class
        self.obj_driver = drv
        self.obj_summary = SummaryObjects(drv)
        self.obj_portlet = RecordPortletObjects(drv)

    def verify_summary_details(self, application_status, application_type):
        try:
            # Verify Application Status
            if self.obj_summary.verify_application_status_value(application_status):
                print("Application status successfully verified to " + application_status)
            else:
                print("Application status not verified to " + application_status)

            # Verify Application Type
            if self.obj_summary.verify_application_type_value(application_type):
                print("Application type successfully verified to " + application_type)
            else:
                print("Application type not verified to " + application_type)

        except Exception as e:
            print("Error : {}".format(e))
