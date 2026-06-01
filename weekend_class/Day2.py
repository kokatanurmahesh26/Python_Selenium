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
    driver.get("https://www.w3schools.com/html/html_tables.asp")
    driver.maximize_window()
    # driver.find_element(By.XPATH, "//span[text() = '✕']").click()
    rows = driver.find_elements(By.XPATH, "//table[@id = 'customers']//tr")
    print(len(rows))
    time.sleep(3)
    for row in rows :
        print(row.text)
    time.sleep(3)

#find company name based on country name 
    company_name = driver.find_element(By.XPATH, "//td[text() = 'Germany']/preceding-sibling::td[2]")
    print(company_name.text)


finally : 
    driver.quit()

