from Common.Base import Base
from Common.TestData import TestData
from Common.delayedAssert import expect, assert_expectations
import pytest

from AutoConfig.AutoConfigView.CustomFields_View import CustomFieldsView
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
        obj_custom_field = CustomFieldsView(setUp['Base'].obj_driver)

        # Custom Fields can be added, updated, add field, delete field, delete sub group
        # Navigate to custom fields Item
        obj_login.login(setUp["sAgency"], setUp['sLogin'], setUp['sPassword'])
        obj_logout.navigate_to_classic_admin()
        obj_custom_field.navigate_to_custom_field()

        df = obj_testdata.read_testdata("AutoConfig.xlsx", "CustomFields")
        for i, row in df.iterrows():
            if row['ACTION'] == "Create":
                obj_custom_field.create_new_custom_field(i + 1, row['GROUP_CODE'], row['SUBGROUP'], row['CUSTOM_LIST_GROUP'], row['GROUP_DISPLAY_ORDER'],
                                                         row['FIRST_FIELD_LABEL'], row['FIELD_LABEL_ALIAS'], row['FIELD_TYPE'], row['DISPLAY_ORDER'],
                                                         row['DEFAULT_VALUE'], row['UNIT'], row['NEW_UNIT'], row['FEE_INDICATOR'], row['REQUIRED_FLAG'],
                                                         row['REQ_FOR_FEE_CALC'], row['SUPERVISOR_EDIT_ONLY'], row['SEARCHABLE_FLAG'], row['MAX_LEN'],
                                                         row['DISPLAY_LEN'], row['ACA_DISPLAYABLE'], row['ACA_SEARCHABLE'], row['JUSTIFICATION'],
                                                         row['DEFAULT_APO_GIS_LAYER'], row['LOCATION_QUERY'], row['STATUS'])
            elif row['ACTION'] == "Update":
                obj_custom_field.update_custom_field(i+1, row['GROUP_CODE'], row['SUBGROUP'],row['FIRST_FIELD_LABEL'],row['FIELD_LABEL_ALIAS'],
                                                    row['DEFAULT_APO_GIS_LAYER'], row['LOCATION_QUERY'],row['FIELD_TYPE'], row['DISPLAY_ORDER'],
                                                    row['DEFAULT_VALUE'], row['UNIT'], row['FEE_INDICATOR'], row['REQUIRED_FLAG'],
                                                    row['REQ_FOR_FEE_CALC'], row['SUPERVISOR_EDIT_ONLY'], row['SEARCHABLE_FLAG'], row['MAX_LEN'],
                                                    row['DISPLAY_LEN'], row['ACA_DISPLAYABLE'], row['ACA_SEARCHABLE'], row['JUSTIFICATION'], row['STATUS'])
            elif row['ACTION'] == "Add Field":
                obj_custom_field.add_new_field(i+1, row['GROUP_CODE'], row['SUBGROUP'], row['APPLY_CHANGE_TO'], row['FIRST_FIELD_LABEL'],
                                               row['FIELD_LABEL_ALIAS'], row['FIELD_TYPE'], row['DISPLAY_ORDER'], row['DEFAULT_VALUE'],
                                               row['UNIT'], row['NEW_UNIT'], row['FEE_INDICATOR'], row['REQUIRED_FLAG'], row['REQ_FOR_FEE_CALC'],
                                               row['SUPERVISOR_EDIT_ONLY'], row['SEARCHABLE_FLAG'], row['MAX_LEN'], row['DISPLAY_LEN'],
                                               row['ACA_DISPLAYABLE'], row['ACA_SEARCHABLE'], row['JUSTIFICATION'], row['STATUS'],
                                               row['DISPLAY_FIELD_EXISTING_RECORD'], row['DISPLAY_FIELD_EXISTING_CONTACT'], row['DISPLAY_FIELD_EXISTING_MEETING'],
                                               row['DISPLAY_FIELD_EXISTING_EDUCATION'], row['ALTERNATE_ACA_LABEL'])
            elif row['ACTION'] == "Delete Field":
                obj_custom_field.delete_field(i+1, row['GROUP_CODE'], row['SUBGROUP'],row['FIRST_FIELD_LABEL'], row['DELETE_CAP_DATA'],
                                               row['DELETE_CHECKLIST'], row['DELETE_CONTACT'], row['DELETE_MEETING'], row['DELETE_EDUCATION'])
            elif row['ACTION'] == "Delete Group":
                obj_custom_field.delete_subgroup(i+1, row['GROUP_CODE'], row['SUBGROUP'], row['DELETE_CAP_DATA'], row['DELETE_CHECKLIST'], row['DELETE_CONTACT'], row['DELETE_MEETING'], row['DELETE_EDUCATION'])
            else:
                print("-----Blank row skipped-----")
            i = i+1

        obj_classic_logout.logout_classic_admin()

    finally:
        setUp['Base'].obj_driver.close()
        setUp['Base'].obj_driver.quit()
        assert_expectations()