from Common.Base import Base
from Common.TestData import TestData
from Common.delayedAssert import expect, assert_expectations
import pytest

from AutoConfig.AutoConfigView.CustomLists_View import CustomListsView
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
        obj_custom_lists = CustomListsView(setUp['Base'].obj_driver)

        # Custom Lists can be added, updated, add field, delete field, delete sub group
        # Navigate to custom fields Item
        obj_login.login(setUp["sAgency"], setUp['sLogin'], setUp['sPassword'])
        obj_logout.navigate_to_classic_admin()
        obj_custom_lists.navigate_to_custom_lists()

        df = obj_testdata.read_testdata("AutoConfig.xlsx", "CustomLists")
        for i, row in df.iterrows():
            if row['ACTION'] == "Create":
                obj_custom_lists.create_new_custom_lists(i + 1, row['CUSTOM_LIST_GROUP_CODE'], row['CUSTOM_LIST_SUBGROUP'], row['GROUP_DISPLAY_ORDER'], row['COLUMN_NAME'],
                                                         row['TYPE'], row['DISPLAY_ORDER'], row['DEFAULT_VALUE'], row['REQUIRED_FLAG'], row['REQ_FOR_FEE_CALC'],
                                                         row['SUPERVISOR_EDIT_ONLY'], row['SEARCHABLE_FLAG'], row['DISPLAY_LEN'], row['ACA_DISPLAYABLE'], row['ACA_SEARCHABLE'],
                                                         row['STATUS'])
            elif row['ACTION'] == "Update":
                obj_custom_lists.update_custom_lists(i+1, row['CUSTOM_LIST_GROUP_CODE'], row['CUSTOM_LIST_SUBGROUP'], row['COLUMN_NAME'], row['TYPE'], row['DISPLAY_ORDER'],
                                                     row['DEFAULT_VALUE'], row['REQUIRED_FLAG'], row['REQ_FOR_FEE_CALC'], row['SUPERVISOR_EDIT_ONLY'], row['SEARCHABLE_FLAG'],
                                                     row['DISPLAY_LEN'], row['ACA_DISPLAYABLE'], row['ACA_SEARCHABLE'], row['STATUS'])
            elif row['ACTION'] == "Add Field":
                obj_custom_lists.add_new_type(i+1, row['CUSTOM_LIST_GROUP_CODE'], row['CUSTOM_LIST_SUBGROUP'], row['COLUMN_NAME'],row['TYPE'], row['DISPLAY_ORDER'],
                                              row['DEFAULT_VALUE'], row['REQUIRED_FLAG'], row['REQ_FOR_FEE_CALC'], row['SUPERVISOR_EDIT_ONLY'], row['SEARCHABLE_FLAG'],
                                              row['DISPLAY_LEN'], row['ACA_DISPLAYABLE'], row['ACA_SEARCHABLE'], row['DISPLAY_ON_EXISTING_RECORD'],
                                              row['DISPLAY_ON_EXISTING_CONTACTS'], row['DISPLAY_ON_EXISTING_MEETING'], row['DISPLAY_ON_EXISTING_EDUCATION'], row['STATUS'])
            elif row['ACTION'] == "Delete Field":
                obj_custom_lists.delete_custom_lists_type(i+1, row['CUSTOM_LIST_GROUP_CODE'], row['CUSTOM_LIST_SUBGROUP'], row['COLUMN_NAME'] , row['DELETE_ASSOCIATED_CAP'],
                                                          row['DELETE_ASSOCIATED_GUIDE'], row['DELETE_ASSOCIATED_CONTACT'], row['DELETE_ASSOCIATED_MEETING'],
                                                          row['DELETE_ASSOCIATED_EDUCATION'])
            else:
                print("-----Blank row skipped-----")

        obj_classic_logout.logout_classic_admin()

    finally:
        setUp['Base'].obj_driver.close()
        setUp['Base'].obj_driver.quit()
        assert_expectations()