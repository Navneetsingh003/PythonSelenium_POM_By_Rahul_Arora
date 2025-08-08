import pytest
from selenium import webdriver

import allure
from allure_commons.types import AttachmentType

from Utilities import config_reader

driver = None


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request, browser_init):
    yield
    item = request.node
    driver = browser_init
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)


@pytest.fixture(params=["chrome"], scope="function")
def browser_init(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()

    request.cls.driver = driver  # Scope of fixture is updated to class level. Using this statement, We have defined
    # driver at class level, so that we get the driver ref in all our test classes.

    driver.implicitly_wait(7)
    driver.maximize_window()

    driver.get(config_reader.read_config("basic info", "URL"))

    yield driver
    driver.close()
