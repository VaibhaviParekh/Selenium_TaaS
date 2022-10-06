from AutoConfig.AutoConfigPageObjects.FeeItem import FeeItemObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Common import ClassicAdminCommonPageObjects
from AutoConfig.AutoConfigPageObjects.ClassicAdmin_Home import ClassicAdminHomePageObjects
import time
import math

class FeeItemView:

    def __init__(self, drv):
        # Create instance of the Fees Page Objects
        self.obj_driver = drv
        self.obj_fee = FeeItemObjects(drv)
        self.obj_common = ClassicAdminCommonPageObjects(drv)
        self.obj_home = ClassicAdminHomePageObjects(drv)

    RETURN_VALUE = 0

    # Select Fee Schedule from Menu
    def navigate_to_fee_item(self):
        try:
            self.obj_home.select_menu("Fee")
            self.obj_home.select_menu_option("Fee Item")
        except Exception as e:
            print("Error : {}".format(e))

    # Search for fee Item. If exists select it, if not then mark failure
    def search_fee_item(self, i, action, fee_item, fee_schedule):
        try:
            self.obj_fee.enter_fee_item_code(fee_item)
            self.obj_fee.enter_fee_schedule(fee_schedule)
            self.obj_common.click_submit()

            record_found = self.obj_fee.verify_fee_item_exists(fee_item, fee_schedule)
            if record_found == 1:
                self.obj_fee.select_fee_item(fee_item, fee_schedule)
                self.RETURN_VALUE = 1
            else:
                no_rec = self.obj_common.no_record_found()
                if no_rec == 1:
                    print(str(i) + ", " + action + ", FAIL, " + fee_item + " unable to find")
                    self.obj_common.click_search_new()
                    self.RETURN_VALUE = 0

        except Exception as e:
            print("Error : {}".format(e))

    # Add new Fee Item
    # If any error appears on execution report the error and continue with next iteration
    def add_new_fee_item(self, i, fee_item, fee_schedule, version, fee_description, comment, unit, calc_formula, calc_variable, default_value
                         ,fee_indicator_qty, round_fee_item, round_fee, coupen_item, effective_date, disabled_on ,required, auto_invoiced,
                         auto_assess, quantity, priority, minimum, maximum ,seq_for_calc, display_order, display_in_ACA, pay_later_in_aca,
                         required_in_ACA, refundable_in_ACA, assess_adj_on_recalc, adj_credits_allowed ,status, payment_period
                         ,sub_group, fee_allocation, account_code1, account_code2, account_code3):
        try:
            time.sleep(5)
            self.obj_fee.click_add()
            self.obj_fee.enter_fee_item_code(fee_item)
            self.obj_fee.select_fee_schedule(fee_schedule)
            self.obj_fee.select_version(version)
            self.obj_fee.enter_fee_description(fee_description)
            self.obj_fee.enter_comment(comment)
            self.obj_fee.select_unit(unit)
            self.obj_fee.select_calc_formula(calc_formula)
            self.obj_fee.enter_calc_variable(calc_variable)
            self.obj_fee.enter_default_value(default_value)
            self.obj_fee.enter_fee_indicator(fee_indicator_qty)
            self.obj_fee.select_round_fee_item(round_fee_item, round_fee)
            self.obj_fee.select_coupen_item(coupen_item, effective_date, disabled_on)
            self.obj_fee.select_required(required)
            self.obj_fee.select_auto_invoiced(auto_invoiced)
            self.obj_fee.select_auto_assess(auto_assess)
            self.obj_fee.enter_quantity(quantity)
            self.obj_fee.enter_priority(priority)
            self.obj_fee.enter_minimum(minimum)
            self.obj_fee.enter_maximum(maximum)
            self.obj_fee.enter_seq_for_calculation(seq_for_calc)
            self.obj_fee.enter_display_order(display_order)
            self.obj_fee.select_display_in_ACA(display_in_ACA, pay_later_in_aca, required_in_ACA, refundable_in_ACA)
            self.obj_fee.select_assess_adjustment_on_recalculation(assess_adj_on_recalc)
            self.obj_fee.select_adjustment_credit_allowed(adj_credits_allowed)
            self.obj_fee.select_status(status)
            self.obj_fee.select_payment_period(payment_period)
            self.obj_fee.enter_subgroup(sub_group)
            self.obj_fee.select_fee_allocation(fee_allocation)
            self.obj_fee.enter_account_code1(account_code1)
            self.obj_fee.enter_account_code2(account_code2)
            self.obj_fee.enter_account_code3(account_code3)
            self.obj_common.click_save()

            alert = self.obj_common.does_alert_exists()
            if alert == 1:
                error = self.obj_common.read_alert_text()
                print(str(i) + ", CREATE, FAIL, " + fee_item + ", Error:" + error)
                self.obj_common.handle_alert()
                self.obj_common.click_cancel()
            else:
                print(str(i) + ", CREATE, PASS, " + fee_item + ", Fee Item Added successfully")
                self.RETURN_VALUE = 1

        except Exception as e:
            print("Error : {}".format(e))

    # Update existing fee item.
    # Search the fee item and if no record found report it and go for the next iteration if not that update the record
    # If any error appears on execution, report the error and continue with the next iteration
    def update_fee_item(self, i, fee_item, fee_schedule, fee_description, comment, unit, calc_formula,
                        calc_variable, default_value, fee_indicator_qty, round_fee_item, round_fee, coupen_item,
                        effective_date, disabled_on, required, auto_invoiced, auto_assess, quantity, priority,
                        minimum, maximum, seq_for_calc, display_order, display_in_ACA, pay_later_in_aca,required_in_ACA,
                        refundable_in_ACA, assess_adj_on_recalc, adj_credits_allowed, status, sub_group,
                        fee_allocation, account_code1, account_code2, account_code3):
        try:
            self.search_fee_item(i, "UPDATE", fee_item, fee_schedule)
            if self.RETURN_VALUE == 1:
                self.obj_fee.enter_fee_description(fee_description)
                self.obj_fee.enter_comment(comment)
                self.obj_fee.select_unit(unit)
                self.obj_fee.select_calc_formula(calc_formula)
                self.obj_fee.enter_calc_variable(calc_variable)
                self.obj_fee.enter_default_value(default_value)
                self.obj_fee.enter_fee_indicator(fee_indicator_qty)
                self.obj_fee.select_round_fee_item(round_fee_item, round_fee)
                self.obj_fee.select_coupen_item(coupen_item, effective_date, disabled_on)
                self.obj_fee.select_required(required)
                self.obj_fee.select_auto_invoiced(auto_invoiced)
                self.obj_fee.select_auto_assess(auto_assess)
                self.obj_fee.enter_quantity(quantity)
                self.obj_fee.enter_priority(priority)
                self.obj_fee.enter_minimum(minimum)
                self.obj_fee.enter_maximum(maximum)
                self.obj_fee.enter_seq_for_calculation(seq_for_calc)
                self.obj_fee.enter_display_order(display_order)
                self.obj_fee.select_display_in_ACA(display_in_ACA, pay_later_in_aca, required_in_ACA, refundable_in_ACA)
                self.obj_fee.select_assess_adjustment_on_recalculation(assess_adj_on_recalc)
                self.obj_fee.select_adjustment_credit_allowed(adj_credits_allowed)
                self.obj_fee.select_status(status)
                self.obj_fee.enter_subgroup(sub_group)
                self.obj_fee.select_fee_allocation(fee_allocation)
                self.obj_fee.enter_account_code1(account_code1)
                self.obj_fee.enter_account_code2(account_code2)
                self.obj_fee.enter_account_code3(account_code3)
                self.obj_common.click_save()

                alert = self.obj_common.does_alert_exists()
                if alert == 1:
                    error = self.obj_common.read_alert_text()
                    print(str(i) + ", UPDATE, FAIL, " + fee_item + ", Error:" + error)
                    self.obj_common.handle_alert()
                    self.obj_common.click_cancel()
                else:
                    print(str(i) + ", UPDATE, PASS, " + fee_item + ", Fee Item Updated successfully")
                self.obj_common.click_search_new()

        except Exception as e:
            print("Error : {}".format(e))