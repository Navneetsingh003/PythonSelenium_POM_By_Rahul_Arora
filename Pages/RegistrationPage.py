from Pages.BasePage import BasePage


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_form(self, name, phone_num, email, country, city, username, password):
        self.input("name_CSS", name)
        self.input("phone_CSS", phone_num)
        self.input("email_XPATH", email)
        self.select_dropdown_by_text("country_XPATH", country)
        self.input("city_XPATH", city)
        self.input("username_XPATH", username)
        self.input("password_XPATH", password)
        self.do_click("submit_button_XPATH")

