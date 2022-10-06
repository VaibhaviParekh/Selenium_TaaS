
from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class LandingPageObjects:

    btnMenu = (By.CSS_SELECTOR, "div.aa-nav-launch>a.button")
    btnAllPages = (By.ID, "ui-tabpanel-1-label")
    txtFilterPage = (By.CSS_SELECTOR, "div.search-input>input[placeholder='Filter pages']")
    btn_create_new = (By.CLASS_NAME, "new-record")
    link_global_search = (By.CSS_SELECTOR, "div.aa-nav-search")  # Not implementing it for now as it may not be required.
    txt_global_search = (By.NAME, "searchText")
    btn_global_search = (By.CLASS_NAME, "ui-button-text ui-clickable")

    def __init__(self, drv):
        # Create instance of Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_menu(self):
        self.obj_wrapper.click_button(self.btnMenu, "Open Menu")

    def click_all_pages(self):
        self.obj_wrapper.click_button(self.btnAllPages, "All Pages")

    def select_menu_option(self, menu_name):
        self.obj_wrapper.enter_text(self.txtFilterPage, "Filter Pages", menu_name)
        btn_menu = (By.CSS_SELECTOR, "a[title='" + menu_name + "']>span.list-text")
        self.obj_wrapper.click_button(btn_menu, menu_name)

    def click_create_record(self):
        self.obj_wrapper.click_button(self.btn_create_new, "Create New Record")

    def click_global_search_link(self):
        self.obj_wrapper.click_button(self.link_global_search, "Global Search Link")

    def enter_record_global_search(self, record_id):
        self.obj_wrapper.enter_text(self.txt_global_search, "Global Search Text", record_id)

    def click_global_search_button(self):
        self.obj_wrapper.click_button(self.btn_global_search, "Global Search")

