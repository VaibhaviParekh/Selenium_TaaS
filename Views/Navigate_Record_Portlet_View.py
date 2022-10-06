from PageObjects.Record_Portlet_Link import RecordPortletObjects


class RecordPortletView:

    def __init__(self, drv):
        # Create instance of the Login Page Objects
        self.obj_driver = drv
        self.obj_portlet = RecordPortletObjects(drv)

    # Navigate to Portlets under record in AA
    def navigate_to_record_portlet(self, portlet):
        try:
            self.obj_portlet.click_record_portlet(portlet)

        except Exception as e:
            print("Error : {}".format(e))


