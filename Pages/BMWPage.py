from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Utilities import config_reader


class BMWPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    # This get_car_title() method will be used for each car brand to get title, it would not be good to repeat the
    # same thing all the Car Brand Pages. Instead, we can create a base class for each page if required and move all
    # common functionalities to that base class.
    
    # def get_car_title(self):
    #     return self.driver.find_element(By.XPATH, config_reader.read_config("locators", "car_title_XPATH")).text
