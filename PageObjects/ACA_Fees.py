from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers

class ACAFeeObjects:

    lbl_total_fees = (By.ID, "ctl00_PlaceHolderMain_capFeeList_lblFeeAmount")
    btn_recalculate = (By.ID, "ctl00_PlaceHolderMain_capFeeList_lnkRecalculate")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def verify_fees(self, fee_item, fee_amount):
        fees = (By.XPATH, "//table[contains(.,'Record fee list')]//td[contains(.,'" + fee_item + "\\')]/following-sibling::td[contains(.,\\'" + fee_amount + "\\')]")
        fees_exists = self.obj_wrapper.object_exists(fees, "ACA Fees")
        if fees_exists == 1:
           return True
        else:
            return False

    def verify_total_fees(self, total_fee):
        total_fees = self.obj_wrapper.get_text_for_webelement(self.lbl_total_fees, "Total Fees")
        if total_fees == total_fee:
            return True
        else:
            return False

    def edit_fee_quantity(self, fee_item, quantity):
        fee_control = self.obj_wrapper.object_exists(By.XPATH,"//table[@id='ctl00_PlaceHolderMain_capFeeList_agenceList_ctl00_feeItemList']"
                                                              "//td[contains(.,'" + fee_item + "')]//ancestor::tr[1]//input")
        self.obj_wrapper.enter_text(fee_control, "Edit fee quantity ",quantity)

    def click_recalculate(self):
        self.obj_wrapper.click_button(self.btn_recalculate, "Recalculate")