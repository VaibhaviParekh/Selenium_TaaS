from PageObjects.Inspection import InspectionObjects
from PageObjects.Inspection_Result import InspectionResultObjects
from PageObjects.Inspection_Details import InspectionDetailsObjects
from Views.EMSE_Window_View import EMSEWindowView
import time


class InspectionView:

    def __init__(self, drv):
        # Create instance of the Fees Page Objects
        self.obj_driver = drv
        self.obj_EMSE = EMSEWindowView(drv)
        self.obj_ins = InspectionObjects(drv)
        self.obj_res_ins = InspectionResultObjects(drv)
        self.obj_ins_det = InspectionDetailsObjects(drv)

    # Verify Inspection in the list
    def verify_inspection_in_list(self, inspection_name, inspection_status):
        try:
            exists = self.obj_ins.verify_inspection(inspection_name, inspection_status)
            if exists == 1:
                print("Inspection name " + inspection_name + " verified successfully to " + inspection_status)
            else:
                print("Inspection name " + inspection_name + " not verified to " + inspection_status)

        except Exception as e:
            print("Error : {}".format(e))

    # Verify Inspection Details in the list
    def verify_inspection_details(self, inspection_name, inspection_status, inspection_date, department, user):
        try:
            exists = self.obj_ins.verify_inspection(inspection_name, inspection_status)
            if exists == 1:

                # Verify Inspection Date
                date = self.obj_ins.verify_inspection_date(inspection_name, inspection_status, inspection_date)
                if date == 1:
                    print("Inspection date verified successfully to " + inspection_date)
                else:
                    print("Inspection date not verified to " + inspection_date)

                # Verify Inspection Department
                dept = self.obj_ins.verify_inspection_department(inspection_name, inspection_status, department)
                if dept == 1:
                    print("Inspection department verified successfully to " + department)
                else:
                    print("Inspection department not verified to " + department)

                # Verify Inspection Department
                dept_user = self.obj_ins.verify_inspection_user(inspection_name, inspection_status, user)
                if dept_user == 1:
                    print("Inspection User verified successfully to " + user)
                else:
                    print("Inspection User not verified to " + user)

            else:
                print("Inspection name " + inspection_name + " not verified to " + inspection_status)

        except Exception as e:
            print("Error : {}".format(e))

    # Click on Inspection Link
    def inspection_select(self, inspection_name, inspection_status):
        try:
            ins_exist = self.obj_ins.verify_inspection(inspection_name, inspection_status)
            if ins_exist == 1:
                self.obj_ins.click_inspection_link(inspection_name, inspection_status)
            else:
                print("Inspection doesn't exists in link")

        except Exception as e:
            print("Error : {}".format(e))

    # Schedule new Inspection
    def inspection_schedule(self, inspection_group, inspection_name, date, user, department, error_message, verify_error='no'):
        try:
            self.obj_ins.click_schedule_inspection_from_menu()
            self.obj_ins.select_inspection_group(inspection_group)
            self.obj_ins.select_inspection_from_list(inspection_group, inspection_name)
            self.obj_ins.move_inspection_to_right()
            self.obj_ins.click_schedule_inspection()
            self.obj_ins.enter_schedule_inspection_date(date)

            if department.lower() == 'current':
                self.obj_ins.click_current_department()
            else:
                self.obj_ins.select_department_value(department)

            if user.lower() == 'current':
                self.obj_ins.click_current_user()
            else:
                # after selection current department it quickly clicks the user link so giving it a sleep
                time.sleep(2)
                self.obj_ins.select_user_value(user)

            # The execution is too much fast so it can't click on button. So giving it a wait
            time.sleep(3)
            self.obj_ins.click_submit()

            if verify_error.lower() == "yes":
                self.obj_EMSE.verify_emse_message(error_message)
            else:
                self.obj_ins.message_from_webpage_click_OK()

                #if Config.Config.browser_type == "Chrome":
                    # Takes a little time for the chrome alert to appear. So we wait to handle the pop up
                time.sleep(5)
                self.obj_ins.handle_alert()

        except Exception as e:
            print("Error : {}".format(e))

    # Result the Inspection
    def inspection_result(self, inspection_name, inspection_status, ins_status_to_update, inspection_date, department, user, result_comment):
        try:
            self.obj_ins.click_inspection_checkbox(inspection_name, inspection_status)
            self.obj_ins.click_result_inspection_from_menu()
            self.obj_res_ins.select_inspection_status(ins_status_to_update)
            self.obj_res_ins.enter_inspection_date(inspection_date)
            self.obj_res_ins.enter_result_comment(result_comment)

            if department.lower() == "current":
                self.obj_res_ins.click_current_department()
            else:
                self.obj_res_ins.select_department_value(department)

            if user.lower() == "current":
                self.obj_res_ins.click_current_user()
            else:
                # after selection current department it quickly clicks the user link so giving it a sleep
                time.sleep(2)
                self.obj_res_ins.select_user_value(user)

            self.obj_res_ins.click_save()
            self.obj_res_ins.enter_applicant_email("a@b.com")
            self.obj_res_ins.click_send_email()

        except Exception as e:
            print("Error : {}".format(e))

    # Search for an existing checklist
    def inspection_search_checklist_item(self, group, checklist_item):
        try:
            self.obj_ins_det.click_search_checklist()
            self.obj_ins_det.select_checklist_group(group)
            self.obj_ins_det.check_checklist_item_checkbox(checklist_item)
            self.obj_ins_det.click_submit()
            item_exists = self.obj_ins_det.verify_checklist_item_exists(checklist_item)
            if item_exists == 1:
                print("Checklist Item " + checklist_item + " added successfully")
            else:
                print("Checklist Item " + checklist_item + " unable to add")

        except Exception as e:
            print("Error : {}".format(e))

    # Select a checklist item. Click on the link
    def inspection_click_checklist_item(self, checklist_item):
        try:
            exists = self.obj_ins_det.verify_checklist_item_exists(checklist_item)
            if exists == 1:
                self.obj_ins_det.click_checklist_item_link(checklist_item)
            else:
                print("Unable to find the checklist item " + checklist_item)
        except Exception as e:
            print("Error : {}".format(e))

    # This click is common between all inspection details
    def inspection_click_cancel_on_inspection_detail(self):
        self.obj_ins_det.click_cancel()

    # Update checklist item status
    def inspection_update_checklist_item_status(self, checklist_sub_item, status, click_submit='no', click_cancel = 'no'):
        try:
            control_exits = self.obj_ins_det.verify_checklist_sub_item_exists(checklist_sub_item)
            if control_exits == 1:
                self.obj_ins_det.select_checklist_sub_item_status(checklist_sub_item, status)

                if click_submit.lower() == "yes":
                    self.obj_ins_det.click_submit()

                if click_cancel == "yes":
                    self.inspection_click_cancel_on_inspection_detail()

        except Exception as e:
            print("Error : {}".format(e))

    # Navigate to Inspection Detail Menu
    def navigate_to_inspection_menu(self, menu):
        if menu.lower() == "checklist":
            self.obj_ins_det.click_checklist_menu()
        elif menu.lower() == "documents":
            self.obj_ins_det.click_documents_menu()
        elif menu.lower == "inspection details":
            self.obj_ins_det.click_inspection_detail_menu()
        elif menu.lower == "conditions":
            self.obj_ins_det.click_condition_menu()