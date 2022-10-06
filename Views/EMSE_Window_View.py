from PageObjects.EMSE_Window import EMSEObjects
import time

class EMSEWindowView:

    def __init__(self, drv):
        # Create instance of the EMSE Window Page Objects
        self.obj_driver = drv
        self.obj_emse = EMSEObjects(drv)

    def verify_emse_message(self, message):
        try:
            # It takes a while to open an EMSE window
            if self.obj_emse.verify_emse_message(message):
                print("EMSE message: " + message + " verified successfully.")
            else:
                print("EMSE message: " + message + " not verified successfully.")
            self.obj_emse.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))