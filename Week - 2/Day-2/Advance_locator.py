from selenium import webdriver #importing the webdriver
from selenium.webdriver.common.keys import Keys #keys class provide keys into the keyboard
from selenium.webdriver.common.by import By #By class to locate element
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

try : 
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)
    user_field = driver.find_element(By.XPATH, "//input[@id = 'user-name']")
    user_field.send_keys("standard_user")
# WebDriverWait(driver,10)
    time.sleep(5)

    password_field = driver.find_element(By.XPATH, "//input[@id = 'password']") #Xpath
    password_field.send_keys("secret_sauce")
# WebDriverWait(driver,10)
    time.sleep(5)

    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button") #Css locator
    login_button.click()
    time.sleep(5)

    link = driver.find_element(By.LINK_TEXT, "LinkedIn") #Link Text
    print("Link Test discovered : ", link.get_attribute("href"))    
    time.sleep(5)

    # partial_link = []
    partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Sauce Labs") #Link Text
    print("Link Test discovered : ", partial_link.text)

finally :
    driver.quit()

