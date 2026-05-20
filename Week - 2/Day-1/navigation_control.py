from selenium import webdriver #importing the webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


driver = webdriver.Chrome() 
# print(driver)
# driver = webdriver.Edge() #Edge browser
driver.get("https://google.com") 
# time.sleep(5)
WebDriverWait(driver, 10)
driver.get("https://youtube.com")
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.quit()
