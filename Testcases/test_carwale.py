import logging
import time

import pytest

from Pages.CarBase import CarBase
from Pages.CarWaleHomePage import CarWaleHomePage
from Testcases.BaseTest import BaseTest
from Utilities import excel_data_provider
from Utilities import config_reader
from Utilities.logging_utility import Logger

log = Logger(__name__, logging.INFO)


class TestCarwale(BaseTest):

    @pytest.mark.skip
    def test_goto_new_car(self):
        log.logger.info("new car test started")
        car_home = CarWaleHomePage(self.driver)
        car_home.find_new_cars()
        time.sleep(3)

    @pytest.mark.skip
    @pytest.mark.parametrize("car_brand, brand_title",
                             excel_data_provider.get_data("NewCars"))
    def test_select_cars(self, car_brand, brand_title):
        log.logger.info("Test select cars started")

        car_home = CarWaleHomePage(self.driver)
        car_base = CarBase(self.driver)

        if car_brand == "BMW":
            car_home.find_new_cars().goto_bmw() # Since the HomePage class find_new_cars() method is returning
            # object of NewCarsPage class, we can directly call NewCarsPage methods by creating object of HomePage
            # class and calling it's method.

            car_title = car_base.get_car_title()
            assert car_title == brand_title, "Car title does not match for "+car_brand+" car."

        elif car_brand == "Hyundai":
            car_home.find_new_cars().goto_hyundai()

            car_title = car_base.get_car_title()
            assert car_title == brand_title, "Car title does not match for " + car_brand + " car."

        elif car_brand == "KIA":
            car_home.find_new_cars().goto_kia()

            car_title = car_base.get_car_title()
            assert car_title == brand_title, "Car title does not match for " + car_brand + " car."

        elif car_brand == "Toyota":
            car_home.find_new_cars().goto_toyota()

            car_title = car_base.get_car_title()
            assert car_title == brand_title, "Car title does not match for " + car_brand + " car."

    @pytest.mark.parametrize("car_brand, brand_title",
                             excel_data_provider.get_data("NewCars"))
    def test_get_car_names_and_prices(self, car_brand, brand_title):
        log.logger.info("Test select cars started")

        car_home = CarWaleHomePage(self.driver)
        car_base = CarBase(self.driver)

        if car_brand == "BMW":
            car_home.find_new_cars().goto_bmw()  # Since the HomePage class find_new_cars() method is returning
            # object of NewCarsPage class, we can directly call NewCarsPage methods by creating object of HomePage
            # class and calling it's method.

            car_title = car_base.get_car_title()
            assert car_title == brand_title, "Car title does not match for " + car_brand + " car."

            car_base.get_car_name_and_prices()

        elif car_brand == "Hyundai":
            car_home.find_new_cars().goto_hyundai()

            car_title = car_base.get_car_title()
            assert car_title == brand_title, "Car title does not match for " + car_brand + " car."

            car_base.get_car_name_and_prices()

        elif car_brand == "KIA":
            car_home.find_new_cars().goto_kia()

            car_title = car_base.get_car_title()
            assert car_title == brand_title, "Car title does not match for " + car_brand + " car."

            car_base.get_car_name_and_prices()

        elif car_brand == "Toyota":
            car_home.find_new_cars().goto_toyota()

            car_title = car_base.get_car_title()
            assert car_title == brand_title, "Car title does not match for " + car_brand + " car."

            car_base.get_car_name_and_prices()


