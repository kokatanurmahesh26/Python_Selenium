from selenium import webdriver #importing the webdriver
from selenium.webdriver.common.keys import Keys #keys class provide keys into the keyboard
from selenium.webdriver.common.by import By #By class to locate element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
expected_title = "Logged In Successfullyrt"
try : 
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
#scenari -1 for Valid credentials
    user_field = wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("student")
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("Password123")
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn"))).click()
    time.sleep(3)
    login_success = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "post-title")))
    login_title = login_success.text
    assert login_title == expected_title, "Error : invalid credentials!"
    time.sleep(3)
    
finally :
    driver.close()
    driver.quit()

