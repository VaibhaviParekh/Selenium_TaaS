from PageObjects.Communication import CommunicationObjects
from PageObjects.Record_Portlet_Link import RecordPortletObjects


class CommunicationView:

    def __init__(self, drv):
        # Create instance of the Communication Page Objects
        self.obj_driver = drv
        self.obj_communication = CommunicationObjects(drv)
        self.obj_portlet = RecordPortletObjects(drv)

    # Verify email instance in the portlet
    def verify_email(self, event, email_title):
        try:
            self.obj_communication.click_on_email_instance(event)
            email_instance = self.obj_communication.verify_email_content(email_title)
            if email_instance == 1:
                print("Email successfully verified")
            else:
                print("Email not successfully verified")
            self.obj_communication.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))

    # Verify no email instance in the portlet
    def verify_no_email(self):
        try:
            self.obj_portlet.click_record_portlet("Communication")
            no_email = self.obj_communication.verify_no_email_instance_exists()
            if no_email == 1:
                print("Successfully verified. There is no email instance present")
            else:
                print("Not verified successfully- Email instance is present")


        except Exception as e:
            print("Error : {}".format(e))