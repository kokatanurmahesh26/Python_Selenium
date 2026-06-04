from selenium import webdriver #importing the webdriver
from selenium.webdriver.common.keys import Keys #keys class provide keys into the keyboard
from selenium.webdriver.common.by import By #By class to locate element
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest

driver = webdriver.Chrome()

def launch_browser() :
    print("launch_browser")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(3)

launch_browser()



