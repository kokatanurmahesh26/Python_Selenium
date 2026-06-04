#Why conftest.py?

#PyTest automatically loads fixtures from:
#no need to write -from conftest import browser
import pytest
from config.config import URL
from utilities.browser_utils import BrowserUtils
from selenium import webdriver

@pytest.fixture
def browser():

    driver = BrowserUtils.get_driver()
    driver.get(URL)

    yield driver

    driver.quit()
