# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Launch Chrome browser
driver = webdriver.Chrome()

# ---------------- IMPLICIT WAIT ----------------
# Selenium will wait up to 10 seconds
# before throwing an exception

# driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)


driver.get("https://www.saucedemo.com/")

# Maximize browser
driver.maximize_window()

# ---------------- LOGIN ----------------

try : 
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    assert "inventory.html" in driver.current_url
    print("QA Test result Passed - successfully logged in")
except AssertionError:
    print("QA Test Result failed - did not navigate to saucedemo.com")

finally :
    driver.quit()
