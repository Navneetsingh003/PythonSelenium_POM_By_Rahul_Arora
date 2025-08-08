from selenium.webdriver.common.by import By

from Utilities import config_reader


class CarBase:

    def __init__(self, driver):
        self.driver = driver

    def get_car_title(self):
        return self.driver.find_element(By.XPATH,
                                        config_reader.read_config("locators", "car_title_XPATH")).text

    def get_car_name_and_prices(self):
        car_names = self.driver.find_elements(By.XPATH,
                                              config_reader.read_config("locators", "car_names_XPATH"))

        car_prices = self.driver.find_elements(By.XPATH,
                                               config_reader.read_config("locators", "car_prices_XPATH"))

        for i in range(1, len(car_prices)):
            print(car_names[i].text+" ----------------- "+car_prices[i].text)
