from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class Spinner:
    # A page object for spinner control

    spinner = (By.ID, "PBO_IMG_ID_KEY_0000000000")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def wait_for_spinner(self):
        spinner_exists = self.obj_wrapper.object_exists(self.spinner, "Loading icon")
        if spinner_exists == 1:
            self.obj_wrapper.is_not_visible(self.spinner, "Loading icon")




