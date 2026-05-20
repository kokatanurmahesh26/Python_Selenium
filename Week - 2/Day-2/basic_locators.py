from selenium import webdriver #importing the webdriver
from selenium.webdriver.common.keys import Keys #keys class provide keys into the keyboard
from selenium.webdriver.common.by import By #By class to locate element
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

try : 
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()

    user_field = driver.find_element(By.ID, "username")
    user_field.send_keys("student")
# WebDriverWait(driver,10)
    time.sleep(5)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Password123")
# WebDriverWait(driver,10)
    time.sleep(5)

    link = driver.find_element(By.LINK_TEXT, "Privacy Policy")
    print("Link Test discovered", link.get_attribute("href"))

    login_button = driver.find_element(By.CLASS_NAME, "btn")
    login_button.click()
    time.sleep(5)
finally :
    driver.quit()

