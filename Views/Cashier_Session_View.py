from PageObjects.Cashier_Session import CashierSessionObjects


class CashierSessionView:

    def __init__(self, drv):
        # Create instance of the Cashier Session Page Objects
        self.obj_driver = drv
        self.obj_cash = CashierSessionObjects(drv)

    def continue_cashier_session(self):
        try:
            self.obj_cash.click_continue_session()
            self.obj_cash.click_cancel()

        except Exception as e:
            print("Error : {}".format(e))