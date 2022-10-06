from PageObjects.ACA_Payment import ACAPaymentObjects
from PageObjects.ACA_Common import ACACommonObject


class ACAPaymentView:

    def __init__(self, drv):
        # Create instance of the ACA Record Details Objects
        self.obj_driver = drv
        self.obj_payment = ACAPaymentObjects(drv)
        self.obj_common = ACACommonObject(drv)

    def aca_fee_checkout(self):
        try:
            self.obj_payment.click_checkout_fees()
            self.obj_common.aca_wait_for_spinner()
            self.obj_payment.click_checkout_cart()
            self.obj_common.aca_wait_for_spinner()

        except Exception as e:
            print("Error : {}".format(e))

    def aca_payment(self, card_type, card_number, security_code, name_on_card, expiration_month, expiration_year, street_address, city, state, country, zip, phone, email, autofill='yes'):
        try:
            self.obj_payment.select_card_type(card_type)
            self.obj_payment.enter_card_number(card_number)
            self.obj_payment.enter_security_code(security_code)
            self.obj_payment.enter_name_on_card(name_on_card)
            self.obj_payment.select_expiration_month(expiration_month)
            self.obj_payment.select_expiration_year(expiration_year)

            if autofill == "yes":
                self.obj_payment.check_auto_fill_with()

            else:
                self.obj_payment.enter_street_address(street_address)
                self.obj_payment.enter_city(city)
                self.obj_payment.select_state(state)
                self.obj_payment.select_country(country)
                self.obj_payment.enter_zip(zip)
                self.obj_payment.enter_phone(phone)
                self.obj_payment.enter_email(email)

            self.obj_payment.click_submit_payment()
            self.obj_common.aca_wait_for_spinner()

        except Exception as e:
            print("Error : {}".format(e))