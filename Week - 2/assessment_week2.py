from selenium import webdriver #importing the webdriver
from selenium.webdriver.common.keys import Keys #keys class provide keys into the keyboard
from selenium.webdriver.common.by import By #By class to locate element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try : 
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
#scenari -1 for Valid credentials
    user_field = wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("student")
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("Password123")
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn"))).click()


    login_success = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "post-title")))
    assert login_success.is_displayed() == True, "Error : invalid credentials!"
    print("The error field is displayed : ", login_success.text )
    time.sleep(3)
    
    #scenari -2 for invalid credentials
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    time.sleep(3)

    # user_field1 = driver.find_element(By.ID, "username")
    # user_field1.send_keys("student")
    # time.sleep(3)

    # password_field1 = driver.find_element(By.NAME, "password")
    # password_field1.send_keys("Password")
    # time.sleep(3)

    # login_button1 = driver.find_element(By.CLASS_NAME, "btn")
    # login_button1.click()
    # time.sleep(3)
    user_field1 = wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("student")
    password_field1 = wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("Password")
    login_button1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn"))).click()
    time.sleep(3)
    error_field = wait.until(EC.presence_of_element_located((By.ID, "error")))
    assert error_field.is_displayed() == True, "Error : error is displayed!"
    print("The error field is displayed : ", error_field.text )
    time.sleep(3)

    # driver.close()
finally :
    driver.quit()

