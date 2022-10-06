from Common.Wrapper import Wrappers
from selenium.webdriver.common.by import By


class FeeObjects:

    # All common objects of Fee portlet
    frm1 = (By.CSS_SELECTOR, "div.space-v360-page.angular-header>iframe#iframe-page-container")
    btn_add = (By.ID, "add")
    btn_delete = (By.ID, "delete")
    btn_invoice = (By.ID, "invoice")
    btn_void = (By.ID, "void")
    btn_invoice_and_pay = (By.ID, "invoiceWithAutoPay")
    btn_recalculate = (By.ID, "reCalc")
    btn_submit = (By.ID, "acsubmit")
    cbo_fee_schedule = (By.ID, "FeeSched")
    txt_quantity = (By.ID, "value(Quantity)")
    txt_notes = (By.ID, "value(feeNotes)")
    cbo_fee_factor = (By.ID, "FeeFactor")
    lbl_total_fee = (By.XPATH, "//td[text()='Fee Total']//following-sibling::td[1]")
    lbl_message = (By.CLASS_NAME, "portlet-msg-alert")


    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_add(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_add, "Add")
        self.obj_wrapper.switch_to_default()

    def click_delete(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_delete, "Delete")
        self.obj_wrapper.switch_to_default()

    def click_invoice(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_invoice, "Invoice")
        self.obj_wrapper.switch_to_default()

    def click_void(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_void, "Void")
        self.obj_wrapper.switch_to_default()

    def click_invoice_and_pay(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_invoice_and_pay, "Invoice and Pay")
        self.obj_wrapper.switch_to_default()

    def click_recalculate(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_recalculate, "Recalculate")
        self.obj_wrapper.switch_to_default()

    def click_submit(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        self.obj_wrapper.click_button(self.btn_submit, "Submit")
        self.obj_wrapper.switch_to_default()

    # for fee_item parameter we can either pass fee item name or fee code
    def verify_fee_code(self, fee_item):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        fee = (By.XPATH, "//table[@id='AccelaMainTable']//td[contains(.,'" + fee_item + "')]")
        exists = self.obj_wrapper.object_exists(fee, "Fee Item")
        self.obj_wrapper.switch_to_default()
        if exists == 1:
            return True
        else:
            return False

    def click_fee_checkbox(self, fee_code):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//table[@id='AccelaMainTable']//tr/td[contains(.,'" + fee_code + "')]//..//td//input")
        self.obj_wrapper.click_checkbox(control)
        self.obj_wrapper.switch_to_default()

    # in all Accela the configuration changes. as fee column_index we have to pass in which column it exists
    # From UI we can determine this.ex. 5th column(Pass 5) or 6th column (Pass 6)
    def verify_fee_amount(self, fee_code, fee_amount, column_index):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        fee_amt_control = (By.XPATH, "//table[@id='AccelaMainTable']//tr/td[contains(.,'" + fee_code + "')]//..//td[" + column_index + "]")
        fee_amt = self.obj_wrapper.get_text_for_webelement(fee_amt_control, "Fee amount control")
        self.obj_wrapper.switch_to_default()
        if fee_amt == fee_amount:
            return True
        else:
            return False

    def verify_fee_status(self, fee_code, fee_status, column_index):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        fee_status_control = (By.XPATH, "//table[@id='AccelaMainTable']//tr/td[contains(.,'" + fee_code + "')]//..//td[" + column_index + "]")
        fee_sts = self.obj_wrapper.get_text_for_webelement(fee_status_control, "Fee status control")
        self.obj_wrapper.switch_to_default()
        if fee_status == fee_sts.strip():
            return True
        else:
            return False

    def verify_no_fee(self):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        no_record = self.obj_wrapper.get_text_for_webelement(self.lbl_message, "No Record")
        self.obj_wrapper.switch_to_default()
        if no_record == "0 record(s) found.":
            return True
        else:
            return False

    def verify_total_fee(self, total_fee):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        exists = self.obj_wrapper.object_exists(self.lbl_total_fee, "Total Fees")
        total_fees = self.obj_wrapper.get_text_for_webelement(self.lbl_total_fee, "Total Fees")
        self.obj_wrapper.switch_to_default()
        if total_fees == total_fee:
            return True
        else:
            return False

    def enter_fee_quantity(self, fee_item, quantity, column_index):
        self.obj_wrapper.switch_to_frame(self.frm1, "")
        control = (By.XPATH, "//table[@id='AccelaMainTable']//td[contains(.,'" + fee_item + "')]//..//td[" + column_index + "]/input")
        self.obj_wrapper.enter_text(control, "Fee Add", quantity)
        self.obj_wrapper.switch_to_default()