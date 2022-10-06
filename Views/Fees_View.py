from PageObjects.Fees import FeeObjects
from Views.Cashier_Session_View import CashierSessionView


class FeesView:

    def __init__(self, drv):
        # Create instance of the Fees Page Objects
        self.obj_driver = drv
        self.obj_fee = FeeObjects(drv)
        self.obj_cash = CashierSessionView(drv)

    # Add New Fee
    def fee_add_new(self, fee_item, quantity, column_index):
        try:
            self.obj_fee.click_add()
            fee_item_exists = self.obj_fee.verify_fee_code(fee_item)
            if fee_item_exists == 1:
                self.obj_fee.enter_fee_quantity(fee_item, quantity, column_index)
                self.obj_fee.click_submit()
            else:
                print("Unable to add quantity. Fee Item doesn't exists")
        except Exception as e:
            print("Error : {}".format(e))

    # Invoice a fee
    def fee_invoice(self, fee_item):
        try:
            fee_item_exists = self.obj_fee.verify_fee_code(fee_item)
            if fee_item_exists == 1:
                self.obj_fee.click_fee_checkbox(fee_item)
                self.obj_fee.click_invoice()
            else:
                print("Unable to add Fee. Fee Item doesn't exists")
        except Exception as e:
            print("Error : {}".format(e))

    # Delete a fee
    def fee_delete(self, fee_item):
        try:
            fee_item_exists = self.obj_fee.verify_fee_code(fee_item)
            if fee_item_exists == 1:
                self.obj_fee.click_fee_checkbox(fee_item)
                self.obj_fee.click_delete()
            else:
                print("Unable to delete Fee. Fee Item doesn't exists")
        except Exception as e:
            print("Error : {}".format(e))

    # Void a fee
    def fee_void(self, fee_item):
        try:
            fee_item_exists = self.obj_fee.verify_fee_code(fee_item)
            if fee_item_exists == 1:
                self.obj_fee.click_fee_checkbox(fee_item)
                self.obj_fee.click_void()
                self.obj_cash.continue_cashier_session()
            else:
                print("Unable to void Fee. Fee Item doesn't exists")
        except Exception as e:
            print("Error : {}".format(e))

    # Verify no fee is invoiced
    def verify_no_fee_invoiced(self):
        try:
            no_fee = self.obj_fee.verify_no_fee()
            if no_fee == 1:
                print("No fee item is present in the list")
            else:
                print("Fee item present in the list")
        except Exception as e:
            print("Error : {}".format(e))

    # Verify fee in the list
    def verify_fee(self, fee_item, fee_amount, fee_status, fee_amount_column_index, fee_status_column_index):
        try:
            fee_item_exists = self.obj_fee.verify_fee_code(fee_item)
            if fee_item_exists == 1:
                # If fee amount is not null verify
                if fee_amount != "":
                    fee_amount_exists = self.obj_fee.verify_fee_amount(fee_item, fee_amount, fee_amount_column_index)
                    if fee_item_exists == 1:
                        print("Fee amount verified successfully to " + fee_amount)
                    else:
                        print("Fee amount not verified to " + fee_amount)

                # If fee status is not null verify
                if fee_status != "":
                    fee_status_exists = self.obj_fee.verify_fee_status(fee_item, fee_status, fee_status_column_index)
                    if fee_status_exists == 1:
                        print("Fee status verified successfully to " + fee_status)
                    else:
                        print("Fee status not verified to " + fee_status)

            else:
                print("Unable to find fee item")

        except Exception as e:
            print("Error : {}".format(e))

    # Verify total fee
    def verify_total_fee(self, total_fee):
        try:
            fee_total = self.obj_fee.verify_total_fee(total_fee)
            if fee_total == 1:
                print("Total fee verified successfully to " + total_fee)
            else:
                print("Unable to verify total fee to " + total_fee)

        except Exception as e:
            print("Error : {}".format(e))