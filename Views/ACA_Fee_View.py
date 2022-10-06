
from PageObjects.ACA_Fees import ACAFeeObjects

class ACAFeesView:

    def __init__(self, drv):
        # Create instance of the ACA Fees Page Objects
        self.obj_driver = drv
        self.obj_fees = ACAFeeObjects(drv)

    def aca_verify_fees(self, fee_item, amount):
        try:
            fee_exists = self.obj_fees.verify_fees(fee_item, amount)
            if fee_exists == 1:
                print("Fee item " + fee_item + " verified to amount " + amount)
            else:
                print("Fee item " + fee_item + " not verified to amount " + amount)
        except Exception as e:
            print("Error : {}".format(e))

    def aca_edit_fee_quantity_and_recalculate(self, fee_item, quantity):
        self.obj_fees.edit_fee_quantity(fee_item, quantity)
        self.obj_fees.btn_recalculate()

    def aca_verify_total_fees(self,total_fees):
        total_fee = self.obj_fees.verify_total_fees(total_fees)
        if total_fee == 1:
            print("Total Fees verified to " + total_fee)
        else:
            print("Total Fees not verified to " + total_fee)
