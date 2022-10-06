# This class contains the wrapper methods for selenium basic operations handling exceptions and timeouts.

from Common.Base import Base
import selenium.webdriver.support.ui
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import math

# from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
# from selenium.webdriver.remote import webelement
# from selenium.webdriver.remote.webelement import WebElement


class BasePage(object):
    def __init__(self, drv):
        # Create the wait object
        self.obj_driver = drv
        self.obj_driver_wait = selenium.webdriver.support.ui.WebDriverWait(self.obj_driver,
                                                                           int(Base.obj_config.mid_timeout))

class Wrappers(BasePage):

    def key_press(self, obj_ele, key_name):
        element = self.obj_driver.find_element(*obj_ele)
        if key_name == "TAB":
            element.send_keys(Keys.TAB)
        elif key_name == "ENTER":
            element.send_keys(Keys.ENTER)
        else:
            element.send_keys(key_name)

    # Click the given button if it exists and is displayed on the page
    def click_button(self, obj_ele, obj_name):
        if self.is_clickable(obj_ele, obj_name):
            element = self.obj_driver_wait.until(EC.presence_of_all_elements_located(obj_ele))
            element[0].click()
            print(obj_name + " clicked successfully.") if Base.obj_config.log_level == 1 else ""
        else:
            raise Exception("Element " + obj_name + " not click-able.")

    def force_click(self, obj_ele, obj_name):
        if self.is_clickable(obj_ele, obj_name):
            element = self.obj_driver.find_element(*obj_ele)
            self.obj_driver.execute_script("arguments[0].click();", element)

    # Enter the given text in the input box if it exists and is displayed on the page
    def enter_text(self, obj_ele, obj_name, text_to_enter):
        try:
            if math.isnan(text_to_enter):
                text_to_enter = ""
        except:
            pass
        if text_to_enter != "":
            element = self.obj_driver.find_element(*obj_ele)
            if self.is_visible(obj_ele, obj_name):
                element.clear()
                element.send_keys(str(text_to_enter))
                print("Value: " + text_to_enter + " entered for " + obj_name + " successfully.") \
                    if Base.obj_config.log_level == 1 else ""
            else:
                raise Exception("Element " + obj_name + " not visible.")

    # Wait for the object to become visible. If it becomes visible in the given time, return true. Else return false.
    def is_visible(self, obj_ele, obj_name):
        try:
            if self.obj_driver_wait.until(EC.visibility_of_element_located(obj_ele),
                                          'Timeout while checking the visibility of the element') is not None:
                print(obj_name + " is visible.") if Base.obj_config.log_level == 1 else ""
                return True
            else:
                print("Element " + obj_name + " is not visible.")
                return False

        except Exception as e:
            # print "ERROR: while checking visibility of the element " + obj_name, "Error: {}".format(e)
            print("Element " + obj_name + " is not visible." + " Error: {}".format(e))
            return False

    # This function will return checkbox selected state
    def get_checkbox_selection(self, obj_ele):
        element = self.obj_driver.find_element(*obj_ele)
        return element.is_selected()

    # This function will click on checkbox in order to select or deselect
    def click_checkbox(self, obj_ele):
        element = self.obj_driver.find_element(*obj_ele)

        # Weird but click didn't work in case of Type drop down on Users page in ManaJS.
        element.send_keys(Keys.SPACE)

    # Wait for the object to get rendered. If it is rendered in the given time, return true. Else return false.
    def object_exists(self, obj_ele, obj_name):
        try:
            if self.obj_driver_wait.until(EC.presence_of_element_located(obj_ele)) is not None:
                print(obj_name + " exists on page") if Base.obj_config.log_level == 1 else ""
                return True
            else:
                print(obj_name + " does not exist on page")
                return False
        except Exception as e:
            print(obj_name + " does not exist on page. Error: {}".format(e))
            # print "ERROR: while checking existence of the element " + obj_name, "Error: {}".format(e)
            return False

    # Wait for the object to be rendered and become clickable.
    # If it becomes clickable in the given time, return true. Else return false.
    def is_clickable(self, obj_ele, obj_name):
        try:
            if self.is_visible(obj_ele, obj_name):
                if self.obj_driver_wait.until(EC.element_to_be_clickable(obj_ele), 'Timeout Exception') is not None:
                    print(obj_name + " is click-able.") if Base.obj_config.log_level == 1 else ""
                    return True
                else:
                    print(obj_name + " is not click-able.")
                    return False
            else:
                return False
        except Exception as e:
            print("ERROR: while checking click-ability of the element " + obj_name + " Error: {}".format(e))
            return False

    def is_enabled(self, obj_ele, obj_name):
        try:
            if self.object_exists(obj_ele, obj_name):
                element = self.obj_driver.find_element(*obj_ele)
                return element.is_enabled()
            else:
                return False
        except Exception as e:
            print("ERROR: while checking if the element " + obj_name + " is enabled. Error: {}".format(e))
            return False

    # Check if the given string exists on the entire page. Return true if found.
    # If object is provided, wait till the object is visible and then check for the string in the page source.
    def text_exists_on_page(self, str_check, obj_ele=None, obj_name=""):
        if obj_ele is not None:
            if self.is_visible(obj_ele, obj_name):
                return str_check in self.obj_driver.page_source
        else:
            return str_check in self.obj_driver.page_source

    # Check if the given string exists in the text of the given control.
    # Check if the control is present on the page, get it's text
    # and then check if the text contains the given string. Return true if found.
    def text_exists_in_control(self, obj_ele, obj_name, text_to_check):
        try:
            if self.is_visible(obj_ele, obj_name):
                if self.obj_driver_wait.until(EC.text_to_be_present_in_element(obj_ele, text_to_check)):
                    element = self.obj_driver.find_element(*obj_ele)
                    if element is not None:
                        print(text_to_check + " found in " + obj_name) if Base.obj_config.log_level == 1 else ""
                        return text_to_check.lower() in element.text.lower()
                    else:
                        print(text_to_check + " not found in " + obj_name)
                        return False
                else:
                    print(text_to_check + " ")
                    return False
        except Exception as e:
            print("ERROR: while checking if text '" + text_to_check + "' exists in element " +
                  obj_name + " Error: {}".format(e))
            return ""

    # Return the text of the control if it exists.
    # obj_ele is the sequence, not the webelement
    def get_text(self, obj_ele, obj_name):
        try:
            if self.object_exists(obj_ele, obj_name):
                element = self.obj_driver.find_element(*obj_ele)

                return element.text.encode("utf-8")
            else:
                raise Exception(obj_name + " not found on the page.")

        except Exception as e:
            print("ERROR: while getting text of element " + obj_name + " Error: {}".format(e))
            return ""

    # Return the text of the control if it exists.
    # objObject is the webelement
    def get_text_for_webelement(self, obj_ele, obj_name):
        try:
            element = self.obj_driver.find_element(*obj_ele)
            return element.text
        except Exception as e:
            print("ERROR: while getting text of element " + obj_name + " Error: {}".format(e))
            return ""

    def get_value(self, obj_ele, obj_name):
        if self.object_exists(obj_ele, obj_name):
            element = self.obj_driver.find_element(*obj_ele)

            return element.get_attribute("value")
        else:
            raise Exception(obj_name + " not found on the page.")

    def get_attribute(self, obj_ele, obj_name, attr_name):
        if self.object_exists(obj_ele, obj_name):
            element = self.obj_driver.find_element(*obj_ele)

            return element.get_attribute(attr_name)
        else:
            raise Exception(obj_name + " not found on the page.")

    # Select the given value from the dropdown
    def select_value_from_dropdown(self, obj_ele, obj_name, value_to_select):
        try:
            if math.isnan(value_to_select):
                value_to_select = ""
        except:
            pass
        if value_to_select != "":
            try:
                obj_select = self.obj_driver.find_element(*obj_ele)
                cbo_select = Select(obj_select)
                cbo_select.select_by_visible_text(str(value_to_select))
            except Exception as e:
                print("ERROR: while selecting value from dropdown: " + obj_name + " Error : {}".format(e))

    # Switch to the child window of the given window title
    def switch_to_window(self, win_name):
        # try:
            # self.parent_window = self.obj_driver.current_window_handle
            # self.obj_driver.switch_to.window(self.parent_window)
            # print("Parent Window:" + self.obj_driver.title)
            child = self.obj_driver.window_handles

            for i in range(len(child)):
                # if child[i] != self.parent_window:
                self.obj_driver.switch_to.window(child[i])
                #print(self.obj_driver.title)
                if win_name in self.obj_driver.title:
                    break

        # except NoSuchWindowException:
        #     continue

    # Verify if given window exists or no
    def window_exists(self, win_name_partial_url, win_name_title):
        try:
            child = self.obj_driver.window_handles
            for i in range(len(child)):
                self.obj_driver.switch_to.window(child[i])

                # We can either check window by partial URL text or by Title
                if win_name_partial_url != "":
                    curr_win_url = self.obj_driver.current_url
                    pos = curr_win_url.find(win_name_partial_url)
                    if pos > 0:
                        # Switching back to main window
                        self.obj_driver.switch_to.window(child[0])
                        return True
                    else:
                        if i+1 == len(child):
                            self.obj_driver.switch_to.window(child[0])
                            return False

                elif win_name_title != "":
                    curr_win_name = self.obj_driver.title
                    if win_name_title in self.obj_driver.title:
                        self.obj_driver.switch_to.window(child[0])
                        return True
                    else:
                        if i + 1 == len(child):
                            self.obj_driver.switch_to.window(child[0])
                            return False
        except Exception as e:
            print("While looking for window Error : {}".format(e))

    # Close any open window
    # Pass the partial unique part of URL. Ex for EMSE pass - EMSEMessage, Report - reportShow.do etc
    def close_open_window(self, win_name_partial_url, win_name_title):
        try:
            child = self.obj_driver.window_handles
            for i in range(len(child)):
                self.obj_driver.switch_to.window(child[i])

                if win_name_partial_url != "":
                    curr_win_url = self.obj_driver.current_url
                    pos = curr_win_url.find(win_name_partial_url)
                    if pos > 0:
                        self.obj_driver.close()
                        self.obj_driver.switch_to.window(child[0])

                elif win_name_title != "":
                    curr_win_name = self.obj_driver.title
                    if win_name_title in self.obj_driver.title:
                        self.obj_driver.close()
                        self.obj_driver.switch_to.window(child[0])
        except Exception as e:
            print("While closing the window Error : {}".format(e))

    # Switch to the given iFrame
    def switch_to_frame(self, obj_ele, obj_name):
        try:
            obj_frame = self.obj_driver.find_element(*obj_ele)
            self.obj_driver.switch_to.frame(obj_frame)
            print("Switched successfully to frame: " + obj_name) if Base.obj_config.log_level == 1 else ""
        except Exception as e:
            print("ERROR: while switching to iFrame: " + "Error: {}".format(e))

    # Switch back from the iFrame to default content
    def switch_to_default(self):
        self.obj_driver.switch_to.default_content()

    def refresh_page(self):
        try:
            self.obj_driver.refresh()
        except Exception as e:
            print("Error: while refreshing page: Error : {}".format(e))

    # Close any browser alert that is displayed. It may not be possible to check the text that is displayed in the alert
    # We are just pressing the Ok button and closing the alert. We are only checking that alert was displayed.
    def close_browser_alert(self):
        self.obj_driver.switch_to.alert.accept()

    def get_text_alert(self):
        alert_text = self.obj_driver.switch_to.alert.text
        return alert_text

    def alert_exists(self):
        try:
            self.obj_finite_wait = selenium.webdriver.support.ui.WebDriverWait(self.obj_driver,5)
            if self.obj_finite_wait.until(EC.alert_is_present()):
                return True
            else:
                return False
        except Exception:
            return False

    # Get the URL of the current page
    def get_current_url(self):
        return self.obj_driver.current_url

    def check_page_loaded(self):
        for ind in range(0, 6):
            page_state = self.obj_driver.execute_script('return document.readyState;')
            if page_state == 'complete':
                print(page_state)
                return True
            else:
                sleep(3)
        else:
            return False

    def scroll_element(self, obj_ele):
        element = self.obj_driver.find_element(*obj_ele)
        self.obj_driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_dropdown_value(self, obj_ele, obj_name):
        try:
            cbo_select = Select(self.obj_driver.find_element(*obj_ele))
            cbo_option = cbo_select.options
            opt_values = []
            for iOptions in range(len(cbo_option)):
                opt_values.append(self.get_text_for_webelement(cbo_option[iOptions], "DropDown Options"))
            return opt_values
        except Exception as e:
            print("ERROR: while reading value from dropdown: " + obj_name + " Error: {}".format(e))

    def mouse_hover(self, obj_ele):
        element = self.obj_driver_wait.until(EC.visibility_of_element_located(obj_ele))

        act_hover = ActionChains(self.obj_driver).move_to_element(element)
        act_hover.perform()

    # Get all elements for the given object
    def get_elements(self, obj_ele):
        try:
            elements = self.obj_driver.find_elements(*obj_ele)
            return elements
        except Exception as exp:
            print("Error : {}".format(exp))
            return None

    def drag_drop(self, source_ele, dest_ele, source_name, dest_name):
        try:
            if self.object_exists(source_ele, source_name):
                if self.object_exists(dest_ele, dest_name):
                    source = self.obj_driver.find_element(*source_ele)
                    destination = self.obj_driver.find_element(*dest_ele)
                    ActionChains(self.obj_driver).drag_and_drop(source, destination).perform()
        except Exception as exp:
            print("Error: while drag and drop: Error : {}".format(exp))

    def set_option_button_value(self, obj_ele, obj_name, value):
        if self.object_exists(obj_ele, obj_name):
            element = self.obj_driver.find_elements(*obj_ele)
            for ele in element:
                if ele.get_attribute("value") == value:
                    ele.click()
                    break
            else:
                raise Exception(value + " option button not found " + obj_name)
        else:
            raise Exception(obj_name + " not found on the page.")

    # Wait unitl element is visible.
    def is_not_visible(self, obj_ele, obj_name):
        try:
            if self.obj_driver_wait.until(EC.invisibility_of_element_located(obj_ele),
                                          'TimeOut while checking the invisibility of the element') is not None:
                return True
            else:
                print(obj_name + " is visible.")
                return False
        except Exception as e:
            print("ERROR: while checking invisibility of the element " + "{}".format(e))
            return False

    def change_control_visibility(self, obj_ele, visible=True):
        element = self.obj_driver.find_element(*obj_ele)
        if visible:
            self.obj_driver.execute_script("arguments[0].style.height='auto'; arguments[0].style.visibility='visible';", element)
        else:
            self.obj_driver.execute_script("arguments[0].style.height='1px'; arguments[0].style.visibility='hidden';", element)
