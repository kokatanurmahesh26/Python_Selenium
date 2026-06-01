# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
try : 
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(3)
    # driver.find_element(By.XPATH, "//span[text() = '✕']").click()
    driver.find_element(By.XPATH, "//span[@role='button']").click()
    time.sleep(3)
    search_button = driver.find_element(By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")
    search_button.send_keys("Apple Iphone 15")
    search_button.send_keys(Keys.ENTER)
    time.sleep(3)
    title = driver.find_element(By.XPATH, "//div[contains(text(), 'Apple iPhone 15 (Black, 128 GB)')]")
    print(title.text)
    time.sleep(3)
    rating = driver.find_element(By.XPATH, "//div[contains(text(), 'Apple iPhone 15 (Black, 128 GB)')]//following-sibling::div[@class='a7saXW']//child::div[contains(text(), '4.6')]")
    print(rating.text)
    time.sleep(3)
finally : 
    driver.quit()

