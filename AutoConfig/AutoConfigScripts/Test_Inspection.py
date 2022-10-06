from Common.Base import Base
from Common.TestData import TestData
from Common.delayedAssert import expect, assert_expectations
import pytest

from AutoConfig.AutoConfigView.Inspection_View import InspectionView
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


def test_inspection(setUp):
    try:
        obj_testdata = TestData()
        obj_login = LoginView(setUp['Base'].obj_driver)
        obj_logout = LogoutView(setUp['Base'].obj_driver)
        obj_classic_logout = ClassicAdminLoginLogoutView(setUp['Base'].obj_driver)
        obj_ins = InspectionView(setUp['Base'].obj_driver)

        # Inspection can be added, updated, add type, delete type
        # Navigate to Inspection Item
        obj_login.login(setUp["sAgency"], setUp['sLogin'], setUp['sPassword'])
        obj_logout.navigate_to_classic_admin()
        obj_ins.navigate_to_inspection()

        df = obj_testdata.read_testdata("AutoConfig.xlsx", "Inspection")
        for i, row in df.iterrows():
            if row['ACTION'] == "Create":
               obj_ins.create_inspection_group(i+1 , row['INSPECTION_GROUP_CODE'], row['INSPECTION_GROUP_NAME'], row['CONFIGURED_BY'],
                                               row['INSPECTION_TYPE'],row['CHECKLIST_GROUP'], row['RESULT_GROUP'], row['GRADE_GROUP'],
                                               row['INSPECTION_SCORE'], row['TOTAL_SCORE'], row['REQUIRED_OPTIONAL'], row['ACA_INSPECTION_DISPLAY'],
                                               row['ACA_MULTI_INSPECTION_SCHEDULE'], row['AUTO_ASSIGN'], row['UNIT'], row['MAX_POINTS'],
                                               row['FLOW_ENABLED'], row['IVR_NUMBER'], row['DISPLAY_ORDER'], row['ALLOW_FAILED_CHECKLIST_ITEM'],
                                               row['CAPTURE_AND_CARRY_OVER_FAILED_CHECKLIST'], row['DEPARTMENT'], row['RESCHEDULE_RESTRICTION'],
                                               row['CANCEL_RESTRICTION'], row['EDIT_INSPECTION'], row['RESCHEDULE_HOURS_PRIOR_VALUE'],
                                               row['RESCHEDULE_DAYS_PRIOR_VALUE'], row['RESCHEDULE_DAYS_PRIOR_TIME'], row['RESCHEDULE_DAYS_PRIOR_AMPM'],
                                               row['CANCEL_HOURS_PRIOR_VALUE'], row['CANCEL_DAYS_PRIOR_VALUE'], row['CANCEL_DAYS_PRIOR_TIME'],
                                               row['CANCEL_DAYS_PRIOR_AMPM'])

            elif row['ACTION'] == "Update":
                obj_ins.update_inspection_type(i+1, row['INSPECTION_GROUP_CODE'], row['INSPECTION_GROUP_NAME'], row['INSPECTION_GROUP_NAME_UPDATE'],
                                               row['CONFIGURED_BY'], row['INSPECTION_TYPE'], row['INSPECTION_TYPE_NAME_UPDATE'], row['CHECKLIST_GROUP'],
                                               row['RESULT_GROUP'], row['GRADE_GROUP'], row['INSPECTION_SCORE'], row['TOTAL_SCORE'],
                                               row['REQUIRED_OPTIONAL'], row['ACA_INSPECTION_DISPLAY'], row['ACA_MULTI_INSPECTION_SCHEDULE'],
                                               row['AUTO_ASSIGN'], row['UNIT'], row['MAX_POINTS'], row['FLOW_ENABLED'], row['IVR_NUMBER'],
                                               row['DISPLAY_ORDER'], row['ALLOW_FAILED_CHECKLIST_ITEM'], row['CAPTURE_AND_CARRY_OVER_FAILED_CHECKLIST'],
                                               row['DEPARTMENT'], row['RESCHEDULE_RESTRICTION'], row['CANCEL_RESTRICTION'], row['EDIT_INSPECTION'],
                                               row['RESCHEDULE_HOURS_PRIOR_VALUE'], row['RESCHEDULE_DAYS_PRIOR_VALUE'], row['RESCHEDULE_DAYS_PRIOR_TIME'],
                                               row['RESCHEDULE_DAYS_PRIOR_AMPM'], row['CANCEL_HOURS_PRIOR_VALUE'], row['CANCEL_DAYS_PRIOR_VALUE'],
                                               row['CANCEL_DAYS_PRIOR_TIME'], row['CANCEL_DAYS_PRIOR_AMPM'])
            elif row['ACTION'] == "Add Type":
                obj_ins.add_inspection_type(i+1 , row['INSPECTION_GROUP_CODE'], row['INSPECTION_GROUP_NAME'],
                                               row['INSPECTION_TYPE'],row['CHECKLIST_GROUP'], row['RESULT_GROUP'], row['GRADE_GROUP'],
                                               row['INSPECTION_SCORE'], row['TOTAL_SCORE'], row['REQUIRED_OPTIONAL'], row['ACA_INSPECTION_DISPLAY'],
                                               row['ACA_MULTI_INSPECTION_SCHEDULE'], row['AUTO_ASSIGN'], row['UNIT'], row['MAX_POINTS'],
                                               row['FLOW_ENABLED'], row['IVR_NUMBER'], row['DISPLAY_ORDER'], row['ALLOW_FAILED_CHECKLIST_ITEM'],
                                               row['CAPTURE_AND_CARRY_OVER_FAILED_CHECKLIST'], row['DEPARTMENT'], row['RESCHEDULE_RESTRICTION'],
                                               row['CANCEL_RESTRICTION'], row['EDIT_INSPECTION'], row['RESCHEDULE_HOURS_PRIOR_VALUE'],
                                               row['RESCHEDULE_DAYS_PRIOR_VALUE'], row['RESCHEDULE_DAYS_PRIOR_TIME'], row['RESCHEDULE_DAYS_PRIOR_AMPM'],
                                               row['CANCEL_HOURS_PRIOR_VALUE'], row['CANCEL_DAYS_PRIOR_VALUE'], row['CANCEL_DAYS_PRIOR_TIME'],
                                               row['CANCEL_DAYS_PRIOR_AMPM'])
            elif row['ACTION'] == "Delete Type":
                obj_ins.inspection_type_delete(i+1, row['INSPECTION_GROUP_CODE'], row['INSPECTION_GROUP_NAME'], row['INSPECTION_TYPE'] )
            else:
                print("-----Blank row skipped-----")

        obj_classic_logout.logout_classic_admin()

    finally:
        setUp['Base'].obj_driver.close()
        setUp['Base'].obj_driver.quit()
        assert_expectations()