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


driver.find_element(By.ID, "user-name").send_keys("standard_user")


driver.find_element(By.ID, "password").send_keys("secret_sauce")


driver.find_element(By.ID, "login-button").click()

# ---------------- VALIDATION ----------------

# Get page title after login
title = driver.title


print("Page Title is:", title)

# Check login success
if "Swag Labs" in title:
    print(" Login Successful")
else:
    print(" Login Failed")

add_cart1 = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
add_cart1.click()

add_cart2 = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-bike-light")))
add_cart2.click()

print("Added two items into cart")
time.sleep(3)

cart = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
cart.click()
print("clicked on cart")
time.sleep(3)

checoukt = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
checoukt.click()
print("clicked on checkout")
time.sleep(3)


wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("mahesh")
wait.until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys("kok")
wait.until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys("587315")
time.sleep(3)

wait.until(EC.presence_of_element_located((By.ID, "continue"))).click()
print("clicked on continue")
time.sleep(3)

total_price = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
print(total_price.text)
time.sleep(3)
# Close browser
driver.quit()