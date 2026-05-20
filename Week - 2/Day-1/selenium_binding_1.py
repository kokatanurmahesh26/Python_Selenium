from selenium import webdriver #importing the webdriver
from selenium.webdriver.common.keys import Keys #keys class provide keys into the keyboard
from selenium.webdriver.common.by import By #By class to locate element
import time

driver = webdriver.Edge()
driver.get("https://www.python.org")
print(driver.title)
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
# time.sleep(500)
driver.implicitly_wait(50000)
elem.send_keys(Keys.RETURN)
assert "No result found " not in driver.page_source
driver.close()