from Pages.BasePage import BasePage


class NewCarsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def goto_hyundai(self):
        self.do_click("hyundai_XPATH")

    def goto_bmw(self):
        self.do_click("bmw_XPATH")

    def goto_kia(self):
        self.do_click("kia_XPATH")

    def goto_toyota(self):
        self.do_click("toyota_XPATH")
