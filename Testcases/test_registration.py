import logging

import pytest

from Pages.RegistrationPage import RegistrationPage
from Testcases.BaseTest import BaseTest
from Utilities import excel_data_provider
from Utilities import config_reader
from Utilities.logging_utility import Logger

log = Logger(__name__, logging.INFO)


class TestRegistration(BaseTest):
    @pytest.mark.parametrize("name, phone_num, email, country, city, username, password", excel_data_provider.get_data("Registration"))
    def test_registration_form(self, name, phone_num, email, country, city, username, password):

        log.logger.info("Registration test started")
        reg_page = RegistrationPage(self.driver)
        reg_page.fill_form(name, phone_num, email, country, city, username, password)
        log.logger.info("Registration test successfully executed.")



