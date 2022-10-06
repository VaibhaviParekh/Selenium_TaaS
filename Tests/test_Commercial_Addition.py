from Common.Base import Base
from Views.Login_View import LoginView
from Views.Landing_View import LandingView
from Views.Record_Search_View import RecordSearchView
from Views.Record_Type_Selection_View import RecordTypeSelectionView
from Views.Intake_Record_Details_View import IntakeRecordDetailsView
from Views.Navigate_Record_Portlet_View import RecordPortletView
from Views.Intake_Address_View import IntakeAddressView
from Views.Intake_ApplicantContact_View import IntakeApplicantContactView
from Views.Intake_Professional_View import IntakeProfessionalView
from Views.Intake_Document_View import IntakeDocumentsView
from Views.Fees_View import FeesView
from Views.Inspection_View import InspectionView
from Views.Workflow_View import WorkflowView
from Views.EMSE_Window_View import EMSEWindowView
from Views.Payment_View import PaymentView
from Views.Document_View import DocumentView
from Views.Record_Details_View import RecordDetailsView
from Views.Summary_View import SummaryView
from Views.Logout_View import LogoutView
from Views.Application_Submission_View import ApplicationSubmissionView
from Views.Communication_View import CommunicationView
from Views.Status_View import StatusView
from Views.Renewal_Info_View import RenewalInfoView
from Views.Window_View import WindowView

import pytest
import time
from Common.delayedAssert import expect, assert_expectations
from datetime import date


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

    obj_arr['acaUser'] = obj_base.obj_config.aca_user
    obj_arr['acaPassword'] = obj_base.obj_config.aca_pwd
    return obj_arr

'''
# Successful login with correct login/password
'''

def test_comercial_addition(setUp):

    try:
        obj_login = LoginView(setUp['Base'].obj_driver)
        obj_landing = LandingView(setUp['Base'].obj_driver)
        obj_record_select = RecordTypeSelectionView(setUp['Base'].obj_driver)
        obj_intake_record_details = IntakeRecordDetailsView(setUp['Base'].obj_driver)
        obj_intake_doc = IntakeDocumentsView(setUp['Base'].obj_driver)
        obj_app = IntakeApplicantContactView(setUp['Base'].obj_driver)
        obj_address = IntakeAddressView(setUp['Base'].obj_driver)
        obj_porf = IntakeProfessionalView(setUp['Base'].obj_driver)
        obj_app_submission = ApplicationSubmissionView(setUp['Base'].obj_driver)
        obj_search = RecordSearchView(setUp['Base'].obj_driver)
        obj_portlet = RecordPortletView(setUp['Base'].obj_driver)
        obj_summary = SummaryView(setUp['Base'].obj_driver)
        obj_record_details = RecordDetailsView(setUp['Base'].obj_driver)
        obj_fee = FeesView(setUp['Base'].obj_driver)
        obj_ins = InspectionView(setUp['Base'].obj_driver)
        obj_workflow = WorkflowView(setUp['Base'].obj_driver)
        obj_emse = EMSEWindowView(setUp['Base'].obj_driver)
        obj_payment = PaymentView(setUp['Base'].obj_driver)
        obj_doc = DocumentView(setUp['Base'].obj_driver)
        obj_communication = CommunicationView(setUp['Base'].obj_driver)
        obj_logout = LogoutView(setUp['Base'].obj_driver)
        obj_status = StatusView(setUp['Base'].obj_driver)
        obj_renewal = RenewalInfoView(setUp['Base'].obj_driver)
        obj_win = WindowView(setUp['Base'].obj_driver)

        today = date.today()
        date_today = today.strftime("%m/%d/%Y")

        # Login to accela AA
        obj_login.login(setUp["sAgency"], setUp['sLogin'], setUp['sPassword'])

        # Create a new record of type Commercial Addition.
        obj_landing.create_new_record()
        obj_record_select.new_record_create("Commercial Addition")
        obj_intake_record_details.enter_record_details("Commercial Addition Record", "Create record for testing")
        obj_address.address_search("2115", "39TH", "ST", "S", "Louisville", "KY", "40211")
        time.sleep(5)
        obj_address.verify_address_owner_parcel_added("yes", "yes")
        obj_app.search_applicant("Vaibhavi", "Parekh", "")
        time.sleep(5)
        obj_porf.search_license_professional("Commercial Building Contractor", "14CONT1073-BUS")
        time.sleep(5)
        obj_intake_doc.new_record_upload_document("TestDoc.txt", "BLD", "Construction Plans", "New Document Upload", "1")
        obj_intake_doc.new_record_upload_document("TestDoc.txt", "BLD", "Site Plans", "New Document Upload", "2")
        obj_app_submission.submit_application()
        obj_app_submission.verify_successful_application_submission()
        obj_summary.verify_summary_details("Submitted", "Commercial Addition")

        # Navigate to Record portlet and read the permit id
        obj_portlet.navigate_to_record_portlet("Record")
        PERMIT_ID = obj_record_details.get_record_id()
        print("Created permit id is: " + PERMIT_ID)

        # Verify no fee is invoiced and on communication portlet application submission email
        obj_portlet.navigate_to_record_portlet("Fees")
        obj_fee.verify_no_fee_invoiced()
        obj_portlet.navigate_to_record_portlet("Communication")
        obj_communication.verify_email("BLD_FIRE_DISTRICT", "Permit Application Submitted")

        # Navigate to workflow and update workflow task
        obj_portlet.navigate_to_record_portlet("Workflow")
        obj_workflow.update_workflow_task("Application Submittal", "Accepted – Plan Review Not Required", date_today, "New Comment", "current", "current", "", "", "", "", "", "yes")
        time.sleep(4)
        obj_portlet.navigate_to_record_portlet("Workflow")
        obj_workflow.verify_workflow_status("Permit Issuance", "in progress", "")
        obj_workflow.verify_workflow_status("Application Submittal", "Accepted –  Plan Review Not Required", "Completed Task")

        obj_portlet.navigate_to_record_portlet("Inspection")
        obj_ins.inspection_schedule("Building Commercial Addition", "Com Remodeling Final Inspection", date_today, "current", "current", "", "no")
        obj_ins.verify_inspection_in_list("Com Remodeling Final Inspection", "Scheduled")

        # Add and verify some fees
        obj_portlet.navigate_to_record_portlet("Fees")
        obj_fee.fee_add_new("Construction Permit Fee", "1", "2")
        obj_fee.verify_fee("Construction Permit Fee", "$75.00", "NEW", "4", "5")
        obj_fee.fee_invoice("Construction Permit Fee")
        obj_fee.verify_fee("Construction Permit Fee", "$75.00", "INVOICED", "4", "5")

        # Update workflow task to Issued and verify fee not paid error appears
        obj_portlet.navigate_to_record_portlet("Workflow")
        obj_workflow.update_workflow_task("Permit Issuance", "Issued", date_today, "New Comment", "current", "current", "", "", "", "", "", "yes")
        time.sleep(5)
        obj_emse.verify_emse_message("Fees have not been fully paid.")

        # Navigate to Payment and make the payment
        obj_portlet.navigate_to_record_portlet("Payment")
        obj_payment.aa_payment("", "Vaibhavi Parekh")
        time.sleep(5)

        # Update workflow task to Issued
        obj_portlet.navigate_to_record_portlet("Workflow")
        obj_workflow.update_workflow_task("Permit Issuance", "Issued", date_today, "New Comment", "current", "current", "", "", "", "", "", "yes")
        time.sleep(5)
        obj_win.verify_window_exists("reportShow.do", "")
        obj_win.close_window("reportShow.do", "")

        # Navigate to Inspection. Schedule and Result the inspection to Passed
        obj_portlet.navigate_to_record_portlet("Inspection")
        obj_ins.inspection_result("Com Remodeling Final Inspection", "Scheduled", "Passed", date_today, "current", "current", "New Comment")
        obj_ins.verify_inspection_in_list("Com Remodeling Final Inspection", "Passed")

        # Update workflow task to Final Inspection
        obj_portlet.navigate_to_record_portlet("Workflow")
        obj_workflow.verify_workflow_status("Inspections", "in progress", "")
        obj_workflow.update_workflow_task("Inspections", "Final Inspection", date_today, "New Comment", "current", "current", "", "", "", "", "", "yes")
        time.sleep(5)

        # Verify application status and issued document is updated
        obj_portlet.navigate_to_record_portlet("Summary")
        obj_summary.verify_summary_details("Finaled", "Commercial Addition")
        obj_portlet.navigate_to_record_portlet("Document")
        obj_doc.aa_upload_documents("TestDoc.txt", "BLD", "Plans", "New Document")
        obj_doc.verify_document_in_list("Buildingpermit", "Permit")

        # Verify and Update Status and Renewal Info
        obj_portlet.navigate_to_record_portlet("Status")
        obj_status.verify_status_values("Finaled", "")
        obj_status.update_status("Issued", date_today)

        obj_portlet.navigate_to_record_portlet("Renewal Info")
        obj_renewal.verify_renewal_info("Pending", "")
        obj_renewal.update_renewal_info("About to Expire", date_today)

        # Logout from AA
        obj_logout.logout()

    finally:
        setUp['Base'].obj_driver.close()
        setUp['Base'].obj_driver.quit()
        assert_expectations()