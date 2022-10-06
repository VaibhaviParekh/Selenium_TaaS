from Common.Base import Base
from Common.TestData import TestData
from Common.delayedAssert import expect, assert_expectations
import pytest

from AutoConfig.AutoConfigView.FeeItem_View import FeeItemView
from AutoConfig.AutoConfigView.ClassicAdmin_LoginLogout_View import ClassicAdminLoginLogoutView
from Views.Login_View import LoginView
from Views.Logout_View import LogoutView


@pytest.fixture
def setUp(cmdopt):
    obj_base = Base()
    obj_base.obj_config.set_config_values(cmdopt)
    obj_base.open_url()
    obj_arr = {}
    obj_arr['Base'] = obj_base
    obj_arr['sAgency'] = obj_base.obj_config.agency
    obj_arr['sLogin'] = obj_base.obj_config.aa_user
    obj_arr['sPassword'] = obj_base.obj_config.aa_pwd
    return obj_arr

'''
# Successful login with correct login/password
'''


def test_fee_schedule(setUp):
    try:
        obj_testdata = TestData()
        obj_login = LoginView(setUp['Base'].obj_driver)
        obj_logout = LogoutView(setUp['Base'].obj_driver)
        obj_classic_logout = ClassicAdminLoginLogoutView(setUp['Base'].obj_driver)
        obj_fee_item = FeeItemView(setUp['Base'].obj_driver)

        # Fee Item can be added new, update existing
        # Navigate to Fee Item
        obj_login.login(setUp["sAgency"], setUp['sLogin'], setUp['sPassword'])
        obj_logout.navigate_to_classic_admin()
        obj_fee_item.navigate_to_fee_item()

        df = obj_testdata.read_testdata("AutoConfig.xlsx", "FeeItem")
        for i, row in df.iterrows():
            if row['ACTION'] == "Create":
                obj_fee_item.add_new_fee_item(i+1, row['FEE_ITEM'], row['FEE_SCHEDULE'], row['VERSION'], row['FEE_DESCRIPTION'], row['COMMENT'],
                                              row['UNIT'], row['CALC_FORMULA'] ,row['CALC_VARIABLE'], row['DEFAULT_VALUE'], row['FEE_INDICATOR'],
                                              row['ROUND_FEE_ITEM'], row['ROUND_TO'], row['COUPON_ITEM'], row['EFFECTIVE_DATE'], row['DISABLED_ON'],
                                              row['REQUIRED'], row['AUTO_INVOICED'], row['AUTO_ASSESS'], row['QUANTITY'], row['PRIORITY'], row['MINIMUM'],
                                              row['MAXIMUM'], row['SEQ_FOR_CALC'], row['DISPLAY_ORDER'],row['DISPLAY_IN_ACA'], row['PAY_LATER_IN_ACA'],
                                              row['REQUIRED_IN_ACA'], row['REFUNDABLE_IN_ACA'], row['ASSESS_ADJUSTMENT_ON_RECALC'],
                                              row['ADJUSTMENT_CREDITS_ALLOWED'], row['STATUS'], row['PAYMENT_PERIOD'], row['SUB_GROUP'],
                                              row['FEE_ALLOCATION'], row['ACCOUNT_CODE_1'], row['ACCOUNT_CODE_2'], row['ACCOUNT_CODE_3'])
            elif row['ACTION'] == "Update":
                obj_fee_item.update_fee_item(i+1, row['FEE_ITEM'], row['FEE_SCHEDULE'], row['FEE_DESCRIPTION'], row['COMMENT'],
                                              row['UNIT'], row['CALC_FORMULA'] ,row['CALC_VARIABLE'], row['DEFAULT_VALUE'], row['FEE_INDICATOR'],
                                              row['ROUND_FEE_ITEM'], row['ROUND_TO'], row['COUPON_ITEM'], row['EFFECTIVE_DATE'], row['DISABLED_ON'],
                                              row['REQUIRED'], row['AUTO_INVOICED'], row['AUTO_ASSESS'], row['QUANTITY'], row['PRIORITY'], row['MINIMUM'],
                                              row['MAXIMUM'], row['SEQ_FOR_CALC'], row['DISPLAY_ORDER'],row['DISPLAY_IN_ACA'], row['PAY_LATER_IN_ACA'],
                                              row['REQUIRED_IN_ACA'], row['REFUNDABLE_IN_ACA'], row['ASSESS_ADJUSTMENT_ON_RECALC'],
                                              row['ADJUSTMENT_CREDITS_ALLOWED'], row['STATUS'], row['SUB_GROUP'],
                                              row['FEE_ALLOCATION'], row['ACCOUNT_CODE_1'], row['ACCOUNT_CODE_2'], row['ACCOUNT_CODE_3'])
            else:
                print("-----Blank row skipped-----")
            i = i+1

        obj_classic_logout.logout_classic_admin()

    finally:
        setUp['Base'].obj_driver.close()
        setUp['Base'].obj_driver.quit()
        assert_expectations()