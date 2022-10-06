from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class FeeItemObjects:

    # Page Objects related to Fee Item
    btn_Add = (By.XPATH, "//img[@alt='Add New Fee Item']")

    txt_Fee_Item_Code = (By.ID, "id_txtR1GfCod")
    txt_Fee_Schedule = (By.ID, "id_txtR1FeeCode")
    txt_Payment_Period = (By.ID, "id_txtR1GfFeePeriod")
    txt_Sub_Group = (By.ID, "id_R1_SUB_GROUP")
    txt_Fee_Description = (By.ID, "id_txtR1GfDes")
    rdo_Status_All = (By.ID, "id_txtRecStatus_All")
    rdo_Status_Enable = (By.ID, "id_txtRecStatus_A")
    rdo_Status_Disable = (By.ID, "id_txtRecStatus_D")

    cbo_Version = (By.ID, "txtGFVersion")
    txt_Comment = (By.ID, "id_txtComment")
    cbo_Unit = (By.ID, "id_txtR1GFUDES")
    cbo_Calc_Formula = (By.ID, "id_txtR1GfCalProc")
    txt_Calc_Variable = (By.ID, "id_txtR1GfFormula")
    txt_Default_Value = (By.ID, "id_DefaultValue")
    txt_Fee_Indicator = (By.ID, "id_FeeIndicator")

    rdo_Round_Fee_Item_Yes = (By.ID, "id_txtRoundFeeFlag_Y")
    rdo_Round_Fee_Item_No = (By.ID, "id_txtRoundFeeFlag_N")
    rdo_Round_Up = (By.ID, "id_txtRoundFeeType_UP")
    rdo_Round_Down = (By.ID, "id_txtRoundFeeType_DOWN")
    rdo_Round_to_Nearest = (By.ID, "id_txtRoundFeeType_NEAREST")

    rdo_Coupen_Item_Yes = (By.ID, "id_couponFlag_Y")
    rdo_Coupen_Item_No = (By.ID, "id_couponFlag_N")
    txt_Effective_Date = (By.ID, "id_txtBeginEffDD")
    txt_Disabled_On = (By.ID, "id_txtEndEffDD")

    rdo_Required_Yes = (By.ID, "id_RequiredFlag_Y")
    rdo_Required_No = (By.ID, "id_RequiredFlag_N")
    rdo_Auto_Invoiced_Yes = (By.ID, "id_autoInvoicedFlag_Y")
    rdo_Auto_Invoiced_No = (By.ID, "id_autoInvoicedFlag_N")
    rdo_Auto_Access_Yes = (By.ID, "id_autoAssessFlag_Y")
    rdo_Auto_Access_No = (By.ID, "id_autoAssessFlag_N")

    txt_Quantity = (By.ID, "id_quantity")
    txt_Priority = (By.ID, "id_txtR1Priority")
    txt_Minimum = (By.ID, "id_txtR1GFMINFEE")
    txt_Maximum = (By.ID, "id_txtR1GFMAXFEE")
    txt_Seq_For_Calculation = (By.ID, "id_txtR1Display")
    txt_Display_Order = (By.ID, "id_txtR1DisplayOrder")

    rdo_Display_in_ACA_Yes = (By.ID, "id_txtR1GFDEFAULTFLAG_Y")
    rdo_Display_in_ACA_No = (By.ID, "disACA")
    rdo_Display_in_ReadOnly = (By.ID, "id_txtR1GFDEFAULTFLAG_R")
    rdo_Pay_Later_in_ACA_Yes = (By.ID, "partialPaymentInACAY")
    rdo_Pay_Later_in_ACA_No = (By.ID, "partialPaymentInACAN")
    rdo_Required_in_ACA_Yes = (By.ID, "reqACAY")
    rdo_Required_in_ACA_No = (By.ID, "reqACAN")
    rdo_Refundable_in_ACA_Yes = (By.ID, "id_refundFlag_Y")
    rdo_Refundable_in_ACA_No = (By.ID, "id_refundFlag_N")
    rdo_Assess_Adj_on_Recalc_Yes = (By.ID, "id_netFeeFlag_Y")
    rdo_Assess_Adj_on_Recalc_No = (By.ID, "id_netFeeFlag_N")
    rdo_Adj_Credits_Allowed_Yes = (By.ID, "id_negativeFeeFlag_Y")
    rdo_Adj_Credits_Allowed_No = (By.ID, "id_negativeFeeFlag_N")

    cbo_Payment_Period = (By.ID, "id_txtR1GFFEEPERIOD")
    rdo_Fee_Allocation_No_Allocation = (By.ID, "id_feeAllocationType_0")
    rdo_Fee_Allocation_Percentage = (By.ID, "id_feeAllocationType_1")
    rdo_Fee_Allocation_Fixed_Amount = (By.ID, "id_feeAllocationType_2")

    txt_Account_Code1 = (By.ID, "id_txtR1GFL1")
    txt_Account_Code2 = (By.ID, "id_txtR1GFL2")
    txt_Account_Code3 = (By.ID, "id_txtR1GFL3")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def click_add(self):
        self.obj_wrapper.click_button(self.btn_Add, "Add")

    def enter_fee_item_code(self, fee_item_code):
        self.obj_wrapper.enter_text(self.txt_Fee_Item_Code, "Fee Item Code", fee_item_code)

    def enter_fee_schedule(self, fee_schedule):
        self.obj_wrapper.enter_text(self.txt_Fee_Schedule, "Fee Schedule", fee_schedule)

    def select_fee_schedule(self, fee_schedule):
        self.obj_wrapper.select_value_from_dropdown(self.txt_Fee_Schedule, "Fee Schedule", fee_schedule)

    def select_version(self, version):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Version, "Version", version)

    def enter_fee_description(self, fee_description):
        self.obj_wrapper.enter_text(self.txt_Fee_Description, "Fee Description", fee_description)

    def enter_comment(self, comment):
        self.obj_wrapper.enter_text(self.txt_Comment, "Comment", comment)

    def select_unit(self, unit):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Unit, "Unit", unit)

    def select_calc_formula(self, calc_formula):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Calc_Formula, "Calc Formula", calc_formula)

    def enter_calc_variable(self, calc_variable):
        self.obj_wrapper.enter_text(self.txt_Calc_Variable, "Calc Variable", calc_variable)

    def enter_default_value(self, default_value):
        self.obj_wrapper.enter_text(self.txt_Default_Value, "Default Value", default_value)

    def enter_fee_indicator(self, fee_indicator):
        self.obj_wrapper.enter_text(self.txt_Fee_Indicator, "Fee Indicator", fee_indicator)

    def select_round_fee_item(self, round_fee_item, round_to):
        if round_fee_item == "Yes":
            self.obj_wrapper.click_button(self.rdo_Round_Fee_Item_Yes, "Round Fee Item")

            if round_to == "Nearest":
                self.obj_wrapper.click_button(self.rdo_Round_to_Nearest, "Round Nearest")
            elif round_to == "Up":
                self.obj_wrapper.click_button(self.rdo_Round_Up, "Round Up")
            elif round_to == "Down":
                self.obj_wrapper.click_button(self.rdo_Round_Down, "Down")

        elif round_fee_item == "No":
            self.obj_wrapper.click_button(self.rdo_Round_Fee_Item_No, "Round Fee Item")

    def select_coupen_item(self, coupen_item, effective_date, disable_on):
        if coupen_item == "Yes":
            self.obj_wrapper.click_button(self.rdo_Coupen_Item_Yes, "Coupen Item Yes")
            self.obj_wrapper.enter_text(self.txt_Effective_Date, "Effective Date", effective_date)
            self.obj_wrapper.enter_text(self.txt_Disabled_On, "Disable On", disable_on)
        elif coupen_item == "No":
            self.obj_wrapper.click_button(self.rdo_Coupen_Item_No, "Coupen Item No")

    def select_required(self, required):
        if required == "Yes":
            self.obj_wrapper.click_button(self.rdo_Required_Yes, "Required Yes")
        elif required == "No":
            self.obj_wrapper.click_button(self.rdo_Required_No, "Required No")

    def select_auto_invoiced(self, auto_invoiced):
        if auto_invoiced == "Yes":
            self.obj_wrapper.click_button(self.rdo_Auto_Invoiced_Yes, "Auto Invoiced Yes")
        elif auto_invoiced == "No":
            self.obj_wrapper.click_button(self.rdo_Auto_Invoiced_No, "Auto Invoiced No")

    def select_auto_assess(self, auto_assess):
        if auto_assess == "Yes":
            self.obj_wrapper.click_button(self.rdo_Auto_Access_Yes, "Auto Access Yes")
        elif auto_assess == "No":
            self.obj_wrapper.click_button(self.rdo_Auto_Access_Yes, "Auto Access No")

    def enter_quantity(self, quantity):
        self.obj_wrapper.enter_text(self.txt_Quantity, "Quantity", quantity)

    def enter_priority(self, priority):
        self.obj_wrapper.enter_text(self.txt_Priority, "Priority", priority)

    def enter_minimum(self, minimum):
        self.obj_wrapper.enter_text(self.txt_Minimum, "Minimum", minimum)

    def enter_maximum(self, maximum):
        self.obj_wrapper.enter_text(self.txt_Maximum, "Maximum", maximum)

    def enter_seq_for_calculation(self, seq_for_calculation):
        self.obj_wrapper.enter_text(self.txt_Seq_For_Calculation, "Seq for calc", seq_for_calculation)

    def enter_display_order(self, display_order):
        self.obj_wrapper.enter_text(self.txt_Display_Order, "Display Order", display_order)

    def select_display_in_ACA(self, display_in_ACA, pay_later_in_ACA, required_in_ACA, refundable_in_ACA):
        if display_in_ACA == "Yes":
            self.obj_wrapper.click_button(self.rdo_Display_in_ACA_Yes, "Display in ACA Yes")
        elif display_in_ACA == "No":
            self.obj_wrapper.click_button(self.rdo_Display_in_ACA_No, "Display in ACA No")
        elif display_in_ACA == "Read-Only":
            self.obj_wrapper.click_button(self.rdo_Display_in_ReadOnly, "Display in ACA Read Only")

        if display_in_ACA != "No":
            self.select_pay_later_in_ACA(pay_later_in_ACA)
            self.select_required_in_ACA(required_in_ACA)
            self.select_refundable_in_ACA(refundable_in_ACA)

    def select_pay_later_in_ACA(self, pay_later_in_ACA):
        if pay_later_in_ACA == "Yes":
            self.obj_wrapper.click_button(self.rdo_Pay_Later_in_ACA_Yes, "Pay Later in ACA Yes")
        elif pay_later_in_ACA == "No":
            self.obj_wrapper.click_button(self.rdo_Pay_Later_in_ACA_No, "Pay Later in ACA No")

    def select_required_in_ACA(self, required_in_ACA):
        if required_in_ACA == "Yes":
            self.obj_wrapper.click_button(self.rdo_Required_in_ACA_Yes, "Required in ACA Yes")
        elif required_in_ACA == "No":
            self.obj_wrapper.click_button(self.rdo_Required_in_ACA_No, "Required in ACA No")

    def select_refundable_in_ACA(self, refundable_in_ACA):
        if refundable_in_ACA == "Yes":
            self.obj_wrapper.click_button(self.rdo_Refundable_in_ACA_Yes, "Refundable in ACA Yes")
        elif refundable_in_ACA == "No":
            self.obj_wrapper.click_button(self.rdo_Refundable_in_ACA_No, "Refundable in ACA No")

    def select_assess_adjustment_on_recalculation(self, assess_adj_on_recalc):
        if assess_adj_on_recalc == "Yes":
            self.obj_wrapper.click_button(self.rdo_Assess_Adj_on_Recalc_Yes, "Assess Adj on Recalc Yes")
        elif assess_adj_on_recalc == "No":
            self.obj_wrapper.click_button(self.rdo_Assess_Adj_on_Recalc_No, "Assess Adj on Recalc No")

    def select_adjustment_credit_allowed(self, adj_credit_allowed):
        if adj_credit_allowed == "Yes":
            self.obj_wrapper.click_button(self.rdo_Adj_Credits_Allowed_Yes, "Adj Credits Allowed Yes")
        elif adj_credit_allowed == "No":
            self.obj_wrapper.click_button(self.rdo_Adj_Credits_Allowed_No, "Adj Credits Allowed No")

    def select_status(self, status):
        if status == "Enable":
            self.obj_wrapper.click_button(self.rdo_Status_Enable, "Enable")
        elif status == "Disable":
            self.obj_wrapper.click_button(self.rdo_Status_Disable, "Disable")

    def select_payment_period(self, payment_period):
        self.obj_wrapper.select_value_from_dropdown(self.cbo_Payment_Period, "Payment Period", payment_period)

    def enter_subgroup(self, subgroup):
        self.obj_wrapper.enter_text(self.txt_Sub_Group, "Sub Group", subgroup)

    def select_fee_allocation(self, fee_allocation):
        if fee_allocation == "No Allocation":
            self.obj_wrapper.click_button(self.rdo_Fee_Allocation_No_Allocation, "No Allocation")
        elif fee_allocation == "Percentage":
            self.obj_wrapper.click_button(self.rdo_Fee_Allocation_Percentage, "Percentage")
        elif fee_allocation == "Fixed Amounts":
            self.obj_wrapper.click_button(self.rdo_Fee_Allocation_Fixed_Amount, "Fixed Amount")

    def enter_account_code1(self, account_code1):
        self.obj_wrapper.enter_text(self.txt_Account_Code1, "Account Code 1", account_code1)

    def enter_account_code2(self, account_code2):
        self.obj_wrapper.enter_text(self.txt_Account_Code2, "Account Code 2", account_code2)

    def enter_account_code3(self, account_code3):
        self.obj_wrapper.enter_text(self.txt_Account_Code3, "Account Code 3", account_code3)

    def verify_fee_item_exists(self, fee_item, fee_schedule):
        control = (By.XPATH, "//table[@summary='Fee Item']//td[contains(.,'" + fee_item + "')]"
                             "//following-sibling::td[contains(.,'" + fee_schedule + "')]/..//td[1]//img")
        exists = self.obj_wrapper.object_exists(control, "Fee Item")
        if exists == 1:
            return True
        else:
            return False

    def select_fee_item(self, fee_item, fee_schedule):
        control = (By.XPATH, "//table[@summary='Fee Item']//td[contains(.,'" + fee_item + "')]"
                                            "//following-sibling::td[contains(.,'" + fee_schedule + "')]/..//td[1]//img")
        self.obj_wrapper.click_button(control, "Fee Item Control")