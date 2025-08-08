from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage


class CarWaleHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def find_new_cars(self):
        self.mouse_hover("new_car_XPATH")
        self.do_click("find_new_cars_XPATH")

        # If we know the next page after performing an action, we can create the object of that class.
        # This will avoid creating object of each page classes separately everytime in all tests.
        # This is the whole purpose of POM design pattern.
        return NewCarsPage(self.driver)


