from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import logging

from Utilities import config_reader
from Utilities.logging_utility import Logger

log = Logger(__name__, logging.INFO) # __name__ will give the current file name. Suppose we are executing
# test_registration.py file, it will give the current file name. Now, wherever we want to generate logs, we can call the method.



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, config_reader.read_config("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, config_reader.read_config("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, config_reader.read_config("locators", locator)).click()
        log.logger.info("Clicking on element: "+str(locator))

    def input(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, config_reader.read_config("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, config_reader.read_config("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, config_reader.read_config("locators", locator)).send_keys(value)
        log.logger.info("Input in an element: " + str(locator)+" and value entered is: "+str(value))

    def select_dropdown_by_text(self, locator, visible_text):
        dropdown = None
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element(By.XPATH, config_reader.read_config("locators", locator))

        elif str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element(By.CSS_SELECTOR, config_reader.read_config("locators", locator))

        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element(By.ID, config_reader.read_config("locators", locator))

        select = Select(dropdown)
        select.select_by_visible_text(visible_text)

        log.logger.info("Selecting from an element: " + str(locator) + " and value selected is: " + str(visible_text))

    def mouse_hover(self, locator):

        element = None
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, config_reader.read_config("locators", locator))

        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element(By.CSS_SELECTOR, config_reader.read_config("locators", locator))

        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(By.ID, config_reader.read_config("locators", locator))

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

        log.logger.info("Moving to an element: " + str(locator))


