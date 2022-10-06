from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class WindowView:

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def close_window(self, partial_window_url, window_name):
        try:
            exists = self.obj_wrapper.window_exists(partial_window_url, window_name)
            if exists == 1:
                self.obj_wrapper.close_open_window(partial_window_url, window_name)
            else:
                print("Window " + window_name + " doesn't exists. Unable to close given instance")
        except Exception as e:
            print("Error : {}".format(e))

    def verify_window_exists(self,partial_window_url, window_name):
        try:
            exists = self.obj_wrapper.window_exists(partial_window_url, window_name)
            if exists == 1:
                print("Window Verified successfully.")
                return True
            else:
                print("Window doesn't exists.")
        except Exception as e:
            print("Error : {}".format(e))