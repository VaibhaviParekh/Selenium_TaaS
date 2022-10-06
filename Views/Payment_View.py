from PageObjects.Payment import PaymentObjects
from Views.Cashier_Session_View import CashierSessionView
from Views.Window_View import WindowView
from Common import Config


class PaymentView:

    def __init__(self, drv):
        # Create an instance of the class
        self.obj_driver=drv
        self.obj_payment = PaymentObjects(drv)
        self.obj_cashier_session = CashierSessionView(drv)
        self.obj_win = WindowView(drv)

    def aa_payment(self, payment_method, payor):
        total_pending_balance = self.obj_payment.get_balance_due()
        if total_pending_balance.strip() == "$0.00":
            print("No Balance due to make the payment")
        else:
            self.obj_payment.click_pay()
            self.obj_payment.select_method(payment_method)
            self.obj_payment.enter_payor(payor)
            self.obj_payment.click_save()
            self.obj_cashier_session.continue_cashier_session()
            self.obj_payment.click_save()
            self.verify_no_payment_due()

            if Config.Config.browser_type.lower() == "chrome":
                self.obj_win.verify_window_exists("receiptView.do", "")
                self.obj_win.close_window("receiptView.do", "")

    def verify_no_payment_due(self):
        due_balance = self.obj_payment.get_balance_due()
        if due_balance.strip() == "$0.00":
            print("Passed - No balance due")
        else:
            print("Failed - Balance is due")