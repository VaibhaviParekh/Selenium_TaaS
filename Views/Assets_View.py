from PageObjects.Assets import AssetsObjects
from Views.Navigate_Record_Portlet_View import RecordPortletView

class AssetsView:

    def __init__(self, drv):
        # Create instance of the Assets Look up Page Objects
        self.obj_driver = drv
        self.obj_asset = AssetsObjects(drv)
        self.obj_portlet = RecordPortletView(drv)

    def asset_lookup (self, asset_group, asset_type, asset_id):
        try:
            self.obj_portlet.navigate_to_record_portlet("Assets")
            self.obj_asset.click_lookup()
            self.obj_asset.enter_asset_group(asset_group)
            self.obj_asset.enter_asset_type(asset_type)
            self.obj_asset.enter_asset_id(asset_id)
            self.obj_asset.click_submit()
            self.obj_asset.asset_exists(asset_id)
            self.obj_asset.select_asset(asset_id)
            self.obj_asset.verify_asset_added(asset_id)

        except Exception as e:
            print("Error : {}".format(e))