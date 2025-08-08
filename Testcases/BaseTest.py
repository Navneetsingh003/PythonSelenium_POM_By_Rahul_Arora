import pytest


@pytest.mark.usefixtures("log_on_failure", "browser_init")
class BaseTest:
    pass

    # def __int__(self, driver, browser_init):
    #     self.driver = browser_init

# Either we can use pass statement with two fixtures defined at class level or to initialize driver with browser_init
# fixture, we can also make use of __init__() method to initialize it.