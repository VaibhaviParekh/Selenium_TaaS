from selenium.webdriver.common.by import By
from Common.Wrapper import Wrappers


class ACAPaymentObjects:

    Select_Contact = (By.ID, "ctl00_PlaceHolderMain_Payment_TrustAccount_ddlAssociatedType")
    Trust_Account_Number = (By.ID, "ctl00_PlaceHolderMain_Payment_TrustAccount_ddlTrustAccount")
    Security_Code = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_txtCCV")
    Card_Number = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_txtCardNumber")
    Card_Type = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_ddlCardType")
    Name_On_Card = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_txtCardName")
    Expiration_Month = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_ddlExpMonth")
    Expiration_Year = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_ddlExpYear")
    Street_Address = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_txtCCStreetAdd1")
    Country = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_ddlCCCountry")
    City = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_txtCCCity")
    State = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_ddlCCState_State1")
    Zip = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_txtCCZip")
    Phone = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_txtCCPhone")
    Email = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_txtCCEmail")
    Defer_Payment = (By.ID, "ctl00_PlaceHolderMain_lnkPayAtCounter")
    Auto_Fill_With = (By.ID, "ctl00_PlaceHolderMain_Payment_CreditCard_chkAutoFill")
    Check_Out_Fees = (By.ID, "ctl00_PlaceHolderMain_lnkAddToShoppingCart")
    Check_Out_Cart = (By.ID, "ctl00_PlaceHolderMain_btnCheckOut")
    Submit_Payment = (By.ID, "ctl00_PlaceHolderMain_Payment_lnkSubmitPaymentPage")

    def __init__(self, drv):
        # Create an instance of a Wrappers class
        self.obj_wrapper = Wrappers(drv)

    def select_card_type(self, card_type):
        self.obj_wrapper.select_value_from_dropdown(self.Card_Type, "Card Type", card_type)

    def enter_card_number(self, card_number):
        self.obj_wrapper.enter_text(self.Card_Number, "Card Number", card_number)

    def enter_security_code(self, security_code):
        self.obj_wrapper.enter_text(self.Security_Code, "Security Code", security_code)

    def select_expiration_month(self, expiration_month):
        self.obj_wrapper.select_value_from_dropdown(self.Expiration_Month, "Expiration Month", expiration_month)

    def select_expiration_year(self, expiration_year):
        self.obj_wrapper.select_value_from_dropdown(self.Expiration_Year, "Expiration Year", expiration_year)

    def enter_name_on_card(self, name_on_card):
        self.obj_wrapper.enter_text(self.Name_On_Card, "Name on Card", name_on_card)

    def check_auto_fill_with(self):
        self.obj_wrapper.click_checkbox(self.Auto_Fill_With)

    def enter_street_address(self, street_address):
        self.obj_wrapper.enter_text(self.Street_Address, "Street Address", street_address)

    def enter_city(self, city):
        self.obj_wrapper.enter_text(self.City, "City", city)

    def select_state(self, state):
        self.obj_wrapper.select_value_from_dropdown(self.State, "State", state)

    def enter_zip(self, zip):
        self.obj_wrapper.enter_text(self.Zip, "Zip", zip)

    def select_country(self, country):
        self.obj_wrapper.select_value_from_dropdown(self.Country, "Country", country)

    def enter_email(self, email):
        self.obj_wrapper.enter_text(self.Email, "E-mail", email)

    def enter_phone(self, phone):
        self.obj_wrapper.enter_text(self.Phone, "Phone", phone)

    def click_submit_payment(self):
        self.obj_wrapper.click_button(self.Submit_Payment, "Submit Payment")

    def click_checkout_fees(self):
        self.obj_wrapper.click_button(self.Check_Out_Fees, "Checkout Fees")

    def click_checkout_cart(self):
        self.obj_wrapper.click_button(self.Check_Out_Cart, "Checkout Cart")