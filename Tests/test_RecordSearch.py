from Common.Base import Base
from Views.LoginView import LoginView
from Views.LandingView import LandingView
from Views.RecordSearchView import RecordSearchView

import pytest
from Common.delayedAssert import assert_expectations


@pytest.fixture
def setup(cmdopt):
    obj_base = Base()

    obj_base.obj_config.set_config_values(cmdopt)
    obj_base.open_url()

    obj_arr = {}
    obj_arr['Base'] = obj_base
    obj_arr['sAgency'] = obj_base.obj_config.agency
    obj_arr['sLogin'] = obj_base.obj_config.user
    obj_arr['sPassword'] = obj_base.obj_config.pwd

    return obj_arr


# Search for a record by ID
def test_search_record(setup):
    try:
        obj_login = LoginView(setup['Base'].obj_driver)
        obj_landing = LandingView(setup['Base'].obj_driver)
        obj_search = RecordSearchView(setup['Base'].obj_driver)

        obj_login.login(setup['sLogin'], setup['sPassword'])
        obj_landing.open_page()
        obj_search.search_record_by_id("AUTOMATE")

    finally:
        setup['Base'].obj_driver.close()
        setup['Base'].obj_driver.quit()

        assert_expectations()
