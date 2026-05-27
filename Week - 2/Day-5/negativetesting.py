from selenium import webdriver #importing the webdriver
from selenium.webdriver.common.keys import Keys #keys class provide keys into the keyboard
from selenium.webdriver.common.by import By #By class to locate element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try : 
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(5)

    user_field = driver.find_element(By.ID, "username")
    user_field.send_keys("student")
    time.sleep(3)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Password")
    time.sleep(3)

    login_button = driver.find_element(By.CLASS_NAME, "btn")
    login_button.click()
    time.sleep(3)
    error_field = wait.until(EC.presence_of_element_located((By.ID, "error")))
    assert error_field.is_displayed() == True, "Error : error is displayed!"
    print("The error field is displayed : ", error_field.text )
    time.sleep(3)

finally :
    driver.quit()

