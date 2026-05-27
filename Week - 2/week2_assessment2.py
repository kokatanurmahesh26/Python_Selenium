# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
try : 
    driver.get("https://practice.expandtesting.com/dropdown")
    driver.maximize_window()
    time.sleep(2)
    wait = WebDriverWait(driver,10)
    country_dd = wait.until(EC.visibility_of_element_located((By.ID, "country")))
    select = Select(country_dd)
    select.select_by_visible_text("India")
    print("Selected Country by Visible text method :", select.first_selected_option.text)
    time.sleep(2)
    select.select_by_value("IS")
    print("Selected Country by value method :", select.first_selected_option.text)
    time.sleep(2)
    select.select_by_index(20)
    print("Selected Country by index method :", select.first_selected_option.text)
    time.sleep(2)
finally : 
    driver.quit()