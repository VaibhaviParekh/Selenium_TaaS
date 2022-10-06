from Common.Base import Base
from Views.LoginView import LoginView
from Views.RecordSearchView import RecordSearchPageObjects
from Views.LandingView import LandingView
from Views.RecordSearchView import RecordSearchView
from Views.Navigate_Record_Portlet_View import RecordPortletView
from Views.Summary_View import SummaryView
from Views.Status_View import StatusView
from Views.Workflow_View import WorkflowView
from Views.EMSE_Window_View import EMSEWindowView
from Views.Record_Details_View import RecordDetailsView
from Views.Communication_View import CommunicationView
from Views.Comments_View import CommentsView
from Views.Assets_View import AssetsView
from Views.Logout_View import LogoutView
from Views.Renewal_Info_View import RenewalInfoView

import pytest
import time

from Common.delayedAssert import expect, assert_expectations


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


def test_111(setUp):
    try:
        obj_login = LoginView(setUp['Base'].obj_driver)
        obj_landing = LandingView(setUp['Base'].obj_driver)
        obj_search = RecordSearchView(setUp['Base'].obj_driver)
        obj_portlet = RecordPortletView(setUp['Base'].obj_driver)
        obj_summary = SummaryView(setUp['Base'].obj_driver)
        obj_status = StatusView(setUp['Base'].obj_driver)
        obj_workflow = WorkflowView(setUp['Base'].obj_driver)
        obj_emse = EMSEWindowView(setUp['Base'].obj_driver)
        obj_record = RecordDetailsView(setUp['Base'].obj_driver)
        obj_communication = CommunicationView(setUp['Base'].obj_driver)
        obj_comments = CommentsView(setUp['Base'].obj_driver)
        obj_assets = AssetsView(setUp['Base'].obj_driver)
        obj_logout = LogoutView(setUp['Base'].obj_driver)
        obj_renewal = RenewalInfoView(setUp['Base'].obj_driver)

        obj_login.login(setUp["sAgency"], setUp['sLogin'], setUp['sPassword'])
        #obj_login.verify_login()
        obj_landing.open_page()
        obj_search.search_record_by_id("COM-ALT-20-00288")

        obj_portlet.navigate_to_record_portlet("Renewal Info")
        #obj_renewal.verify_renewal_info("Pending", "11/17/2020")
        obj_renewal.update_renewal_info("Active", "12/12/2020")
        #obj_assets.asset_lookup()

        time.sleep(10)
        #obj_portlet.navigate_to_record_portlet("Status")
        #obj_status.verify_status_values("Issued", "11/25/2020")
        #obj_status.update_status("Void", "12/28/2020", "", "")

        #obj_portlet.navigate_to_record_portlet("Communication")
        #obj_communication.verify_email("BLD_PMT_ISSUED", "Permit Issued")
        #obj_communication.verify_email("BLD_FIRE_DISTRICT", "Permit Application Submitted")
        #obj_communication.verify_no_email()

        #obj_portlet.navigate_to_record_portlet("Comments")
        #obj_comments.verify_comment_added("Any person who shall attempt to erect. construct, alter, repair", "11/25/2020")
        #obj_comments.verify_no_comment()

        #obj_portlet.navigate_to_record_portlet("Record")
        #obj_record.verify_record_id("COM-ALT-20-00289")

        #obj_portlet.navigate_to_record_portlet("Summary")
        #obj_summary.verify_summary_details("Issued", "Commercial Alteration")

        #obj_portlet.navigate_to_record_portlet("Workflow")
        #obj_workflow.verify_workflow_status("Application Submittal", "Accepted –  Plan Review Not Required", "Completed Task")
        #obj_portlet.navigate_to_record_portlet("Workflow")
        #obj_workflow.verify_workflow_status("Permit Issuance", "in progress","")
        #obj_workflow.update_workflow_task("Permit Issuance", "Issued", "11/25/2020","New Comment","current","current","","","","","","yes")
        #obj_emse.verify_emse_message("Fees have not been fully paid.")





    finally:
        setUp['Base'].obj_driver.close()
        setUp['Base'].obj_driver.quit()
        assert_expectations()

