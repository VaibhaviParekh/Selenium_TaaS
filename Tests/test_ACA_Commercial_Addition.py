from Common.Base import Base
from Views.ACA_Common_View import ACACommonView
from Views.ACA_Login_View import ACALoginView
from Views.ACA_Logout_View import ACALogoutView
from Views.ACA_Record_Details_View import ACARecordDetailsView
from Views.ACA_Address_View import ACAAddressView
from Views.ACA_Contact_Information_View import ACAContactInformationView
from Views.ACA_License_Professional_View import ACALicenseProfessionalView
from Views.ACA_Detail_Description_View import ACADetailDescriptionView
from Views.ACA_Record_Type_Selection_View import ACARecordTypeSelectionView
from Views.ACA_Documents_View import ACADocumentView
from Views.ACA_Record_Submission_View import ACARecordSubmissionView
from Views.Login_View import LoginView
from Views.Landing_View import LandingView
from Views.Record_Search_View import RecordSearchView
from Views.Window_View import WindowView
from Views.Navigate_Record_Portlet_View import RecordPortletView
from Views.Fees_View import FeesView
from Views.Inspection_View import InspectionView
from Views.Workflow_View import WorkflowView
from Views.EMSE_Window_View import EMSEWindowView
from Views.Payment_View import PaymentView
from Views.Document_View import DocumentView
from Views.Record_Details_View import RecordDetailsView
from Views.Summary_View import SummaryView
from Views.Logout_View import LogoutView
from Views.Communication_View import CommunicationView
from Views.Status_View import StatusView
from Views.Renewal_Info_View import RenewalInfoView
from Common.TestData import TestData
from Common.delayedAssert import expect, assert_expectations

import pytest
from datetime import date
import time


@pytest.fixture
def setUp(cmdopt):
    obj_base = Base()
    obj_base.obj_config.set_config_values(cmdopt)

    obj_base.open_url()
    obj_base.open_url_aca()

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


def test_aca_commercial_addition(setUp):
    try:
        obj_aca_login = ACALoginView(setUp['Base'].obj_driver_aca)
        obj_aca_logout = ACALogoutView(setUp['Base'].obj_driver_aca)
        obj_aca_rec = ACARecordTypeSelectionView(setUp['Base'].obj_driver_aca)
        obj_aca_record_details = ACARecordDetailsView(setUp['Base'].obj_driver_aca)
        obj_aca_common = ACACommonView(setUp['Base'].obj_driver_aca)
        obj_aca_address = ACAAddressView(setUp['Base'].obj_driver_aca)
        obj_aca_contact = ACAContactInformationView(setUp['Base'].obj_driver_aca)
        obj_aca_prof = ACALicenseProfessionalView(setUp['Base'].obj_driver_aca)
        obj_aca_dd = ACADetailDescriptionView(setUp['Base'].obj_driver_aca)
        obj_aca_doc = ACADocumentView(setUp['Base'].obj_driver_aca)
        obj_aca_submit = ACARecordSubmissionView(setUp['Base'].obj_driver_aca)

        obj_testdata = TestData()
        obj_login = LoginView(setUp['Base'].obj_driver)
        obj_search = RecordSearchView(setUp['Base'].obj_driver)
        obj_portlet = RecordPortletView(setUp['Base'].obj_driver)
        obj_summary = SummaryView(setUp['Base'].obj_driver)
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
        obj_landing = LandingView(setUp['Base'].obj_driver)
        obj_win = WindowView(setUp['Base'].obj_driver)

        today = date.today()
        date_today = today.strftime("%m/%d/%Y")

        df = obj_testdata.read_testdata("TestData_Sample.xlsx", "ACA")
        for i, row in df.iterrows():
            if row['Action'] == "Create":
                obj_aca_login.aca_login(setUp['acaUser'], setUp['acaPassword'])
                obj_aca_common.select_module("Building", "Apply for a Permit")
                obj_aca_common.aca_license_disclaimer()
                obj_aca_common.aca_continue_application()
                obj_aca_common.aca_select_license("None Applicable")
                obj_aca_common.aca_continue_application()
                obj_aca_rec.aca_select_record_type("Commercial", "Commercial Addition")
                obj_aca_address.aca_search_address(row['Street_Num'], row['Street_Name'], row['Street_Type'], row['Direction'], row['Zip'])
                obj_aca_contact.applicant_select_from_account_with_address_or_contact_type("Mailing Address", "")
                obj_aca_contact.verify_applicant_added()
                obj_aca_prof.license_professional_look_up(row['Lic_Type'], row['Lic_Num'])
                obj_aca_common.aca_continue_application()
                obj_aca_dd.enter_detail_description(row['Application_Name'], row['Detail_Desc'], "")
                obj_aca_common.aca_continue_application()
                obj_aca_common.aca_continue_application()

                obj_aca_doc.aca_document_upload(row['Document_1'], row['Doc_Category_1'], row['Doc_Desc'])
                obj_aca_doc.aca_document_upload(row['Document_2'], row['Doc_Category_2'], row['Doc_Desc'])
                obj_aca_common.aca_continue_application()
                obj_aca_common.aca_continue_application()
                PERMIT_ID = obj_aca_submit.aca_verify_record_submitted()
                print("Permit ID: " + PERMIT_ID)
                obj_aca_logout.aca_logout()

                obj_login.login(setUp["sAgency"], setUp['sLogin'], setUp['sPassword'])
                time.sleep(2)
                obj_landing.open_page()
                obj_search.search_record_by_id(PERMIT_ID)

                # Verify no fee is invoiced and on communication portlet application submission email
                obj_portlet.navigate_to_record_portlet("Fees")
                obj_fee.verify_no_fee_invoiced()
                obj_portlet.navigate_to_record_portlet("Communication")
                obj_communication.verify_email("BLD_APP_RECEIVED", "Application Received")

                # Navigate to workflow and update workflow task
                obj_portlet.navigate_to_record_portlet("Workflow")
                obj_workflow.update_workflow_task("Application Submittal", "Accepted – Plan Review Not Required",
                                                  date_today, "New Comment", "current", "current", "", "", "", "", "",
                                                  "yes")
                time.sleep(4)
                obj_portlet.navigate_to_record_portlet("Workflow")
                obj_workflow.verify_workflow_status("Permit Issuance", "in progress", "")
                obj_workflow.verify_workflow_status("Application Submittal", "Accepted –  Plan Review Not Required",
                                                    "Completed Task")

                obj_portlet.navigate_to_record_portlet("Inspection")
                obj_ins.inspection_schedule("Building Commercial Addition", "Com Remodeling Final Inspection",
                                            date_today, "current", "current", "", "no")
                obj_ins.verify_inspection_in_list("Com Remodeling Final Inspection", "Scheduled")

                # Add and verify some fees
                obj_portlet.navigate_to_record_portlet("Fees")
                obj_fee.fee_add_new("Construction Permit Fee", "1", "2")
                obj_fee.verify_fee("Construction Permit Fee", "$75.00", "NEW", "4", "5")
                obj_fee.fee_invoice("Construction Permit Fee")
                obj_fee.verify_fee("Construction Permit Fee", "$75.00", "INVOICED", "4", "5")

                # Update workflow task to Issued and verify fee not paid error appears
                obj_portlet.navigate_to_record_portlet("Workflow")
                obj_workflow.update_workflow_task("Permit Issuance", "Issued", date_today, "New Comment", "current",
                                                  "current", "", "", "", "", "", "yes")
                time.sleep(5)
                obj_emse.verify_emse_message("Fees have not been fully paid.")

                # Navigate to Payment and make the payment
                obj_portlet.navigate_to_record_portlet("Payment")
                obj_payment.aa_payment("", "Vaibhavi Parekh")
                time.sleep(5)

                # Update workflow task to Issued
                obj_portlet.navigate_to_record_portlet("Workflow")
                obj_workflow.update_workflow_task("Permit Issuance", "Issued", date_today, "New Comment", "current",
                                                  "current", "", "", "", "", "", "yes")
                time.sleep(5)
                obj_win.verify_window_exists("reportShow.do", "")
                obj_win.close_window("reportShow.do", "")

                # Navigate to Inspection. Schedule and Result the inspection to Passed
                obj_portlet.navigate_to_record_portlet("Inspection")
                obj_ins.inspection_result("Com Remodeling Final Inspection", "Scheduled", "Passed", date_today,
                                          "current", "current", "New Comment")
                obj_ins.verify_inspection_in_list("Com Remodeling Final Inspection", "Passed")

                # Update workflow task to Final Inspection
                obj_portlet.navigate_to_record_portlet("Workflow")
                obj_workflow.verify_workflow_status("Inspections", "in progress", "")
                obj_workflow.update_workflow_task("Inspections", "Final Inspection", date_today, "New Comment",
                                                  "current", "current", "", "", "", "", "", "yes")
                time.sleep(5)
                obj_win.close_window("","EMSE Message List")

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
        setUp['Base'].obj_driver_aca.close()
        setUp['Base'].obj_driver_aca.quit()
        assert_expectations()

