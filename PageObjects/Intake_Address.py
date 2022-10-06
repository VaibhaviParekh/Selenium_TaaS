from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class IntakeAddressObjects:

    # Address
    btn_ad_search = (By.ID, "searchAddress")
    txt_str_no = (By.ID, "value(addressesModel*houseNumberStart)")
    txt_str_name = (By.ID, "value(addressesModel*streetName)")
    txt_city = (By.ID, "value(addressesModel*city)")
    txt_state = (By.ID, "value(addressesModel*state)")
    cbo_str_type = (By.ID, "value(addressesModel*streetSuffix)")
    txt_zip = (By.ID, "value(addressesModel*zip_disp)")
    cbo_direction = (By.ID, "value(addressesModel*streetDirection)")
    txt_str_suffix = (By.ID, "value(addressesModel*streetSuffixdirection)")
    txt_str_prefix = (By.ID, "value(addressesModel*streetPrefix)")
    cbo_fraction_end = (By.ID, "value(addressesModel*houseFractionEnd)")
    txt_country = (By.ID, "value(addressesModel*county)")
    txt_distance = (By.ID, "value(addressesModel*distance)")
    txt_insp_dist_prefix = (By.ID, "value(addressesModel * inspectionDistrictPrefix)")
    txt_neighbour = (By.ID, "value(addressesModel * neighborhood)")
    txt_source_flag = (By.ID, "value(addressesModel * sourceFlag)")
    cbo_add_type1 = (By.ID, "value(addressesModel * refAddressType)")
    txt_level_end = (By.ID, "value(addressesModel * levelNumberEnd)")
    txt_str_name_end = (By.ID, "value(addressesModel * streetNameEnd)")
    cbo_unit_type = (By.ID, "value(addressesModel * unitType)")
    cbo_fraction_start = (By.ID, "value(addressesModel * houseFractionStart)")
    txt_unit_end = (By.ID, "value(addressesModel * unitEnd)")
    cbo_add_flag = (By.ID, "value(addressesModel * addressTypeFlag)")
    txt_second_road = (By.ID, "value(addressesModel * secondaryRoad)")
    txt_insp_dist = (By.ID, "value(addressesModel * inspectionDistrict)")
    txt_x_coordinate = (By.ID, "value(addressesModel * XCoordinator)")
    txt_y_coordinate = (By.ID, "value(addressesModel * YCoordinator)")
    txt_str_add = (By.ID, "value(addressesModel * fullAddress)")
    txt_level_prefix = (By.ID, "value(addressesModel * levelPrefix)")
    txt_hsg_alpha_start = (By.ID, "value(addressesModel * houseNumberAlphaStart)")
    cbo_location_type = (By.ID, "value(addressesModel * locationType)")
    txt_cross_str_name = (By.ID, "value(addressesModel * crossStreetNameStart)")
    cbo_add_status = (By.ID, "value(addressesModel * addressStatus)")
    txt_unit_start = (By.ID, "value(addressesModel * unitStart)")
    txt_str_no_end = (By.ID, "value(addressesModel * houseNumberEnd)")
    cbo_country = (By.ID, "value(addressesModel*countryCode)")
    txt_add_desc = (By.ID, "value(addressesModel * addressDescription)")
    txt_secondary_road_no = (By.ID, "value(addressesModel * secondaryRoadNumber)")
    txt_neighbour_prefix = (By.ID, "value(addressesModel * neighberhoodPrefix)")
    cbo_add_type2 = (By.ID, "value(addressesModel * addressType)")
    txt_level_start = (By.ID, "value(addressesModel * levelNumberStart)")
    txt_hsg_alpha_end = (By.ID, "value(addressesModel * houseNumberAlphaEnd)")
    txt_str_no_start = (By.ID, "value(addressesModel * streetNameStart)")
    txt_cross_str_name_end = (By.ID, "value(addressesModel * crossStreetNameEnd)")
    lbl_msg = (By.ID, "err_msg")
    frame_add = (By.ID, "addressListFrame")
    frame_owner = (By.ID, "ownerListFrame")
    frame_parcel = (By.ID, "parcelListFrame")

    def __init__(self, drv):
        # Create instance of Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def enter_street_number(self, str_no):
        self.obj_wrapper.enter_text(self.txt_str_no, "Street No", str_no)

    def enter_street_name(self, str_name):
        self.obj_wrapper.enter_text(self.txt_str_name, "Street Name", str_name)

    def select_direction(self, direction):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_direction, "Direction", direction)

    def select_street_type(self, str_type):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_str_type, "Street Type", str_type)

    def enter_city(self, city):
        self.obj_wrapper.enter_text(self.txt_city, "City", city)

    def enter_state(self, state):
        self.obj_wrapper.enter_text(self.txt_state, "State", state)

    def enter_zip(self, zip):
        self.obj_wrapper.enter_text(self.txt_zip, "ZIP", zip)

    def click_address_search(self):
        self.obj_wrapper.click_button(self.btn_ad_search, "Search Address")

    def verify_address_found(self):
        self.obj_wrapper.switch_to_frame(self.frame_add, "")
        msg = self.obj_wrapper.get_text_for_webelement(self.lbl_msg, "Message")
        self.obj_wrapper.switch_to_default()
        if msg == "1 record(s) added successfully.":
            return True
        else:
            return False

    def verify_owner_found(self):
        self.obj_wrapper.switch_to_frame(self.frame_owner, "")
        msg = self.obj_wrapper.get_text_for_webelement(self.lbl_msg, "Message")
        self.obj_wrapper.switch_to_default()
        if msg == "1 record(s) added successfully.":
            return True
        else:
            return False

    def verify_parcel_found(self):
        self.obj_wrapper.switch_to_frame(self.frame_parcel, "")
        msg = self.obj_wrapper.get_text_for_webelement(self.lbl_msg, "Message")
        self.obj_wrapper.switch_to_default()
        if msg == "1 record(s) added successfully.":
            return True
        else:
            return False
