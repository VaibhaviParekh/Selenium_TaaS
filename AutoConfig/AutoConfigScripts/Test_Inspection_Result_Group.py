from Common.Base import Base
from Common.TestData import TestData
from Common.delayedAssert import expect, assert_expectations
import pytest

from AutoConfig.AutoConfigView.Inspection_Result_Group_View import InspectionResultGroupView
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


def test_inspection_result_group(setUp):
    try:
        obj_testdata = TestData()
        obj_login = LoginView(setUp['Base'].obj_driver)
        obj_logout = LogoutView(setUp['Base'].obj_driver)
        obj_classic_logout = ClassicAdminLoginLogoutView(setUp['Base'].obj_driver)
        obj_ins = InspectionResultGroupView(setUp['Base'].obj_driver)

        # Inspection Result Group can be added, updated, add type, delete type
        # Navigate to Inspection Result Group
        obj_login.login(setUp["sAgency"], setUp['sLogin'], setUp['sPassword'])
        obj_logout.navigate_to_classic_admin()
        obj_ins.navigate_to_inspection_result_group()

        df = obj_testdata.read_testdata("AutoConfig.xlsx", "InspectionResultGroup")
        for i, row in df.iterrows():
            if row['ACTION'] == "Create":
                obj_ins.create_new_result_group(i+1, row['RESULT_GROUP'], row['RESULT'], row['DISPLAY_ORDER'], row['RESULT_TYPE'],
                                                row['MINIMUM_SCORE'], row['MAXIMUM_SCORE'], row['MINIMUM_MAJOR_VIOLATION'], row['MAXIMUM_MAJOR_VIOLATION'] )
            elif row['ACTION'] == "Update":
                obj_ins.update_result_group(i+1, row['RESULT_GROUP'], row['RESULT'], row['RESULT_UPDATE'], row['DISPLAY_ORDER'], row['RESULT_TYPE'],
                                            row['MINIMUM_SCORE'], row['MAXIMUM_SCORE'], row['MINIMUM_MAJOR_VIOLATION'], row['MAXIMUM_MAJOR_VIOLATION'])
            elif row['ACTION'] == "Add Type":
                obj_ins.add_new_result(i+1, row['RESULT_GROUP'], row['RESULT'], row['DISPLAY_ORDER'], row['RESULT_TYPE'], row['MINIMUM_SCORE'],
                                       row['MAXIMUM_SCORE'], row['MINIMUM_MAJOR_VIOLATION'], row['MAXIMUM_MAJOR_VIOLATION'])
            elif row['ACTION'] == "Delete Type":
                obj_ins.delete_result(i+1, row['RESULT_GROUP'], row['RESULT'])
            else:
                print("-----Blank row skipped-----")

        obj_classic_logout.logout_classic_admin()

    finally:
        setUp['Base'].obj_driver.close()
        setUp['Base'].obj_driver.quit()
        assert_expectations()