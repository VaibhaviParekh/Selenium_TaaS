from Common.Base import Base
from Common.TestData import TestData
from Common.delayedAssert import expect, assert_expectations
import pytest

from AutoConfig.AutoConfigView.FeeSchedule_View import FeeScheduleView
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
        obj_fee_schedule = FeeScheduleView(setUp['Base'].obj_driver)

        # Fee schedule can be added new, update existing, add new version
        # Navigate to Fee Schedule
        obj_login.login(setUp["sAgency"], setUp['sLogin'], setUp['sPassword'])
        obj_logout.navigate_to_classic_admin()
        obj_fee_schedule.navigate_to_fee_schedule()

        df = obj_testdata.read_testdata("AutoConfig.xlsx", "FeeSchedule")
        for i, row in df.iterrows():
            if row['ACTION'] == "Create":
                obj_fee_schedule.add_new_fee_schedule(i+1, row['FEE_SCHEDULE'], row['FEE_SCHEDULE_ALIAS'], row['VERSION'],
                                                      row['EFFECTIVE_DATE'], row['COMMENT'], row['STATUS'], row['DISABLE_ON'])
            elif row['ACTION'] == "Update":
                obj_fee_schedule.edit_fee_schedule(i+1, row['FEE_SCHEDULE'], row['FEE_SCHEDULE_ALIAS'], row['VERSION'],
                                                      row['EFFECTIVE_DATE'], row['COMMENT'], row['STATUS'], row['DISABLE_ON'])
            elif row['ACTION'] == "Add New Version":
                obj_fee_schedule.add_new_version(i+1, row['FEE_SCHEDULE'], row['FEE_SCHEDULE_ALIAS'], row['VERSION'],
                                                      row['EFFECTIVE_DATE'], row['COMMENT'], row['STATUS'], row['DISABLE_ON'])
            else:
                print("-----Blank row skipped-----")
            i = i+1

        obj_classic_logout.logout_classic_admin()

    finally:
        setUp['Base'].obj_driver.close()
        setUp['Base'].obj_driver.quit()
        assert_expectations()