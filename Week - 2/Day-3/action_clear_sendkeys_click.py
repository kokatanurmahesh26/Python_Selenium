from selenium import webdriver
from selenium.webdriver import ActionChains #import action class
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
try :
    driver.get("https://python.org/")
    time.sleep(3)
    search_field = driver.find_element(By.NAME, "q")
    search_field.clear()
    search_field.send_keys("Documentation")
    time.sleep(3)
    go_button = driver.find_element(By.ID, "submit")
    go_button.click()
    time.sleep(3)
    print("search executed successfully")

finally :
    driver.quit()
