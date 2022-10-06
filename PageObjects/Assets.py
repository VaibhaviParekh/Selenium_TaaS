from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class AssetsObjects:

    # All common objects of Assets portlet
    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")

    btn_Save = (By.ID, "Save")
    btn_Look_Up = (By.ID, "lookup")
    btn_Submit = (By.ID, "submit4WO")
    btn_Select = (By.ID, "select")
    lbl_msg = (By.ID, "err_msg")

    cbo_Asset_Group = (By.ID, "value(g1AssetGroup)")
    cbo_Asset_Type = (By.ID, "value(g1AssetType)")

    txt_Asset_ID = (By.ID, "value(g1AssetID)")
    txt_Asset_Name = (By.ID, "value(g1AssetName)")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    # Click on Look Up button
    def click_lookup(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Look_Up, "Look Up")
        self.obj_wrapper.switch_to_default()

    # Save the asset value
    def click_save(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Save, "Save")
        self.obj_wrapper.switch_to_default()

    # Search the asset and then Select option appears to select the asset
    def click_select(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Select, "Select")
        self.obj_wrapper.switch_to_default()

    # Click on Submit button while looking up for the asset
    def click_submit(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Submit, "Submit")
        self.obj_wrapper.switch_to_default()

    def enter_asset_group(self, asset_group):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Asset_Group, "Asset Group", asset_group)
        self.obj_wrapper.switch_to_default()

    def enter_asset_type(self, asset_type):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Asset_Type, "Asset Type", asset_type)
        self.obj_wrapper.switch_to_default()

    def enter_asset_id(self, asset_id):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_Asset_ID, "Asset ID", asset_id)
        self.obj_wrapper.switch_to_default()

    def enter_asset_name(self, asset_name):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_Asset_Name, "Asset Name", asset_name)
        self.obj_wrapper.switch_to_default()

    def asset_exists(self, asset_id):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        label_asset = (By.xpath, "//table[@id='AccelaMainTable']//td[contains(.,'" + asset_id + "')]")
        if self.obj_wrapper.object_exists(label_asset,"Asset id" + asset_id):
            return True
        else:
            return False

    # Click on a checkbox against Asset ID and select it
    def select_asset(self, asset_id):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        checkbox_asset = (By.xpath, "//table[@id='AccelaMainTable']//td[contains(.,'" + asset_id + "')]//..//input")
        self.obj_wrapper.click_button(checkbox_asset," Asset selection checkbox ")
        self.obj_wrapper.switch_to_default()

    def verify_asset_added(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        msg = self.obj_wrapper.get_attribute(self.lbl_msg, "Message", "innertext")
        self.obj_wrapper.switch_to_default()
        if "1 record(s) added successfully." in msg:
            return True
        else:
            return False
