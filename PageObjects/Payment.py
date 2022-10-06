from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class PaymentObjects:

    # Payment on AA
    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")

    lbl_Total_Invoice_Payment = (By.XPATH, "//td[text()='Total Inspection Amount: ']/following-sibling::td[1]")
    lbl_Total_Payment = (By.XPATH, "//table[@id='displayBody']//td//td[contains(.,'Total Payment:')]/following-sibling::td[1]")
    lbl_Balance = (By.XPATH, "//table[@id='displayBody']//td//td[contains(.,'Total Balance:')]/following-sibling::td[1]")
    lbl_Amount_Not_Applied = (By.XPATH, "//td[text()='Amount Not Applied: ']/following-sibling::td[1]")
    lbl_Terminal = (By.XPATH, "//label[text()='Terminal #']/ancestor::td[1]/following-sibling::td[1]")
    lbl_Cashier_ID = (By.XPATH, "//label[text()='Cashier ID']/ancestor::td[1]/following-sibling::td[1]")
    lbl_Date = (By.XPATH, "//label[text()='Date']/ancestor::td[1]/following-sibling::td[1]")

    btn_Pay = (By.ID, "pay")
    btn_Fullpay = (By.ID, "fullpay")
    btn_Fullpay_Submit = (By.ID, "acsubmit")
    btn_Save = (By.ID, "save")
    btn_Cancel = (By.ID, "cancel")
    btn_Refund = (By.ID, "Refund")
    btn_Generate_Receipt = (By.ID, "generate")

    cbo_method = (By.ID, "value(method)")
    cbo_check_type = (By.ID, "value(checkType)")
    txt_amount = (By.ID, "value(amount)")
    txt_reference = (By.ID, "value(reference)")
    txt_cc_authentication_code = (By.ID, "value(ccAuthCode)")
    txt_check_number = (By.ID, "value(checkNbr)")
    txt_driver_license = (By.ID, "value(licenseNbr)")
    txt_payor = (By.ID, "value(payee)")
    img_select_payor = (By.NAME, "pageImage")
    txt_comment = (By.ID, "value(comment)")

    def __init__(self, drv):
        # Create instance of Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_pay(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Pay, "Pay")
        self.obj_wrapper.switch_to_default()

    def click_fullpay(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Fullpay, "Full Pay")
        self.obj_wrapper.switch_to_default()

    def click_fullpay_submit(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Fullpay_Submit, "Full Payment Submit")
        self.obj_wrapper.switch_to_default()

    def click_save(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Save, "Save")
        self.obj_wrapper.switch_to_default()

    def click_cancel(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Cancel, "Cancel")
        self.obj_wrapper.switch_to_default()

    def click_refund(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Refund, "Refund")
        self.obj_wrapper.switch_to_default()

    def click_generate_receipt(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_Generate_Receipt, "Generate Receipt")
        self.obj_wrapper.switch_to_default()

    def select_method(self, method):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.obj_wrapper, "Select Method", method)
        self.obj_wrapper.switch_to_default()

    def select_check_type(self, check_type):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.select_value_from_dropdown(self.cbo_check_type, "Check Type", check_type)
        self.obj_wrapper.switch_to_default()

    def enter_amount(self, amount):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_amount, "Amount", amount)
        self.obj_wrapper.switch_to_default()

    def enter_reference(self, reference):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_reference, "Reference", reference)
        self.obj_wrapper.switch_to_default()

    def enter_cc_authentication(self, cc_authentication):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_cc_authentication_code, "CC Authentication Code", cc_authentication)
        self.obj_wrapper.switch_to_default()

    def enter_check_number(self, check_number):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_check_number, "Check Number", check_number)
        self.obj_wrapper.switch_to_default()

    def enter_driver_license(self, driver_license):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_driver_license, "Dirver License", driver_license)
        self.obj_wrapper.switch_to_default()

    def enter_payor(self, payor):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_payor, "Payor", payor)
        self.obj_wrapper.switch_to_default()

    def enter_comment(self, comment):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.enter_text(self.txt_comment, "Comment", comment)
        self.obj_wrapper.switch_to_default()

    def click_select_payor(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.img_select_payor, "Select Payor")
        self.obj_wrapper.switch_to_default()


    def get_total_invoiced_payment(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        total_invoice_payment = self.obj_wrapper.get_text_for_webelement(self.lbl_Total_Invoice_Payment, "Total Invoice Payment")
        self.obj_wrapper.switch_to_default()
        return total_invoice_payment

    def get_balance_due(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        total_payment_due = self.obj_wrapper.get_text_for_webelement(self.lbl_Balance, "Due Balance")
        self.obj_wrapper.switch_to_default()
        return total_payment_due

    def get_total_paid_payment(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        total_payment_paid = self.obj_wrapper.get_text_for_webelement(self.lbl_Total_Payment, "Total Payment")
        self.obj_wrapper.switch_to_default()
        return total_payment_paid